from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import psutil
import socket
import time
import os
from werkzeug.utils import secure_filename
import requests
import json

UPLOAD_FOLDER = 'UploadedFiles'
STATE_FILE = 'device_state.json'
APP_PORT = 5000

current_led_status = "OFF"
current_servo_position = "0°"

NODE_RED_BASE_URL = "http://10.0.0.7:1880"


def load_state():
    """Load device state from file"""
    global current_led_status, current_servo_position
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
                current_led_status = state.get('led_status', 'OFF')
                current_servo_position = state.get('servo_position', '0°')
        except Exception:
            current_led_status = "OFF"
            current_servo_position = "0°"


def save_state():
    """Save device state to file"""
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump({
                'led_status': current_led_status,
                'servo_position': current_servo_position
            }, f)
    except Exception:
        pass


def format_size(size_bytes):
    if size_bytes >= 1024**3:
        return f"{round(size_bytes / (1024**3), 2)} GB"
    elif size_bytes >= 1024**2:
        return f"{round(size_bytes / (1024**2), 2)} MB"
    elif size_bytes >= 1024:
        return f"{round(size_bytes / 1024, 2)} KB"
    else:
        return f"{size_bytes} bytes"


def get_connected_devices(port=APP_PORT):
    try:
        remote_ips = set()
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == psutil.CONN_ESTABLISHED and conn.raddr and conn.laddr:
                if conn.laddr.port == port:
                    remote_ips.add(conn.raddr.ip)
        return len(remote_ips)
    except Exception:
        return 0


app = Flask(__name__)
load_state()


@app.route('/')
def index():
    connected_devices = get_connected_devices()
    return render_template('flaskapp.html', connected_devices=connected_devices)


@app.route('/status')
def status():
    cpu = psutil.cpu_percent(interval=1)

    ram_used = psutil.virtual_memory().used * 10**-9
    ram_total = psutil.virtual_memory().total * 10**-9
    disk_used = psutil.disk_usage('/').used * 10**-9
    disk_total = psutil.disk_usage('/').total * 10**-9

    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    local_ip = socket.gethostbyname(socket.gethostname())

    uptime_seconds = time.clock_gettime(time.CLOCK_BOOTTIME)
    uptime_hours = uptime_seconds / 3600

    connected_devices = get_connected_devices()

    return render_template(
        'status.html',
        cpu=round(cpu, 2),
        ram_percent=round(ram_percent, 2),
        ram_used=round(ram_used, 2),
        ram_total=round(ram_total, 2),
        disk_percent=round(disk_percent, 2),
        disk_used=round(disk_used, 2),
        disk_total=round(disk_total, 2),
        ip_address=local_ip,
        uptime_hours=round(uptime_hours, 2),
        uptime=round(uptime_hours, 2),
        connected_devices=connected_devices
    )


@app.route('/files', methods=['GET', 'POST'])
def files():
    if request.method == 'POST':
        uploaded_file = request.files.get('file')

        if uploaded_file and uploaded_file.filename != '':
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)

            filename = secure_filename(uploaded_file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(save_path)

            return redirect(url_for('files'))

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    files = []
    total_size = 0

    for filename in os.listdir(UPLOAD_FOLDER):
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.isfile(filepath):
            size_bytes = os.path.getsize(filepath)
            total_size += size_bytes

            files.append({
                'name': filename,
                'size': format_size(size_bytes)
            })

    if total_size > 1024**3:
        total_display = round(total_size / (1024**3), 2)
        unit_total = "GB"
    else:
        total_display = round(total_size / (1024**2), 2)
        unit_total = "MB"

    return render_template(
        'files.html',
        files=files,
        total_size=total_display,
        unit=unit_total
    )


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@app.route('/delete/<filename>')
def delete_file(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for('files'))


def render_controls_page():
    return render_template(
        'controls.html',
        led_status=current_led_status,
        servo_position=current_servo_position
    )


@app.route('/controls/')
@app.route('/controls')
def controls():
    return render_controls_page()


@app.route('/controls/LED/ON')
def led_on():
    global current_led_status

    requests.get(f"{NODE_RED_BASE_URL}/led/on")
    current_led_status = "ON"
    save_state()

    return render_controls_page()


@app.route('/controls/LED/OFF')
def led_off():
    global current_led_status

    requests.get(f"{NODE_RED_BASE_URL}/led/off")
    current_led_status = "OFF"
    save_state()

    return render_controls_page()


@app.route('/controls/Servo/0')
def servo_0():
    global current_servo_position

    requests.get(f"{NODE_RED_BASE_URL}/servo/0")
    current_servo_position = "0°"
    save_state()

    return render_controls_page()


@app.route('/controls/Servo/90')
def servo_90():
    global current_servo_position

    requests.get(f"{NODE_RED_BASE_URL}/servo/90")
    current_servo_position = "90°"
    save_state()

    return render_controls_page()


@app.route('/controls/Servo/180')
def servo_180():
    global current_servo_position

    requests.get(f"{NODE_RED_BASE_URL}/servo/180")
    current_servo_position = "180°"
    save_state()

    return render_controls_page()


@app.route('/controls/Servo/Custom', methods=['POST'])
def servo_custom():
    global current_servo_position

    angle = request.form.get('angle')

    try:
        angle = int(angle)
    except:
        angle = 0

    if angle < 0:
        angle = 0

    if angle > 180:
        angle = 180

    requests.get(f"{NODE_RED_BASE_URL}/servo/{angle}")

    current_servo_position = f"{angle}°"
    save_state()

    return render_controls_page()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)