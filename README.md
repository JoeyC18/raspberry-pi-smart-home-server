# Raspberry Pi Smart Home Server

A full-stack Raspberry Pi project that combines real-time system monitoring, local file management, and Arduino hardware control within one browser-based dashboard.

The application uses Flask as the web server, Node-RED as the communication layer, and USB serial communication to control an LED and servo motor connected to an Arduino.

## Project Demonstrations

### Software Walkthrough

The software walkthrough demonstrates the main dashboard, live Raspberry Pi system information, file-management tools, and hardware-control interface.

[![Watch the Software Walkthrough](docs/images/Smart%20Home%20Server%20Main%20Screen.png)](https://youtu.be/jApAIk-ZR-c)

[Watch the Software Walkthrough on YouTube](https://youtu.be/jApAIk-ZR-c)

### Full Hardware Demonstration

The hardware demonstration shows the complete system operating from end to end. Commands are sent from the Flask dashboard to Node-RED and transferred to the Arduino through USB serial communication to control the LED and servo motor.

[![Watch the Full Hardware Demonstration](docs/images/Smart%20Home%20Server%20Device%20Controls.png)](https://youtube.com/shorts/GVCfA7g-HXs?feature=share)

[Watch the Full Hardware Demonstration on YouTube](https://youtube.com/shorts/GVCfA7g-HXs?feature=share)

## Project Overview

This project explores how web development, system utilities, automation platforms, and embedded hardware can be connected within one local network.

The dashboard provides three main functions:

* Monitoring Raspberry Pi system performance
* Managing files stored locally on the Raspberry Pi
* Controlling physical hardware through an Arduino

The Node-RED server address is stored in an environment variable rather than being hardcoded into the application. This makes the project portable across different Raspberry Pis, computers, and network configurations without requiring changes to the Python source code.

## Features

### System Monitoring

* Live CPU usage
* RAM usage tracking
* Disk and storage monitoring
* System uptime display
* Local IP address display
* Connected-device count
* Automatically refreshing system information

### File Management

* Upload files through the browser
* Store files locally on the Raspberry Pi
* Display uploaded files dynamically
* Download stored files
* Delete files through the dashboard
* Display individual file sizes
* Calculate total folder storage usage
* Sanitize uploaded filenames

### Hardware Control

* Turn an LED on and off
* Move a servo motor to preset positions
* Enter a custom servo angle
* Restrict custom servo positions to the valid range
* Preserve device-state information locally
* Send HTTP requests from Flask to Node-RED
* Send serial commands from Node-RED to Arduino

### Portable Configuration

* Store the Node-RED server address in a local `.env` file
* Provide a safe `.env.example` configuration template
* Change network settings without modifying `app.py`
* Keep local configuration files outside version control

## Screenshots

### Main Dashboard

The main dashboard provides access to system monitoring, file management, and hardware controls.

![Smart Home Server Main Screen](docs/images/Smart%20Home%20Server%20Main%20Screen.png)

### System Status

The system-status page displays live Raspberry Pi information, including CPU usage, memory usage, disk usage, uptime, local IP address, and connected-device information.

![Smart Home Server System Status](docs/images/Smart%20Home%20Server%20System%20Status.png)

### File Management

The file hub allows users to upload, view, download, and delete files stored on the Raspberry Pi.

![Smart Home Server File Hub](docs/images/Smart%20Home%20Server%20File%20Hub.png)

### Device Controls

The device-control page allows users to control an LED and servo motor connected through an Arduino.

![Smart Home Server Device Controls](docs/images/Smart%20Home%20Server%20Device%20Controls.png)

## System Architecture

```text
Web Browser
     ↓
HTML, CSS, and Jinja Templates
     ↓
Flask Web Server
     ↓
Environment-Based Node-RED URL
     ↓
HTTP Requests
     ↓
Node-RED
     ↓
USB Serial Communication
     ↓
Arduino
     ↓
LED and Servo Motor
```

## Hardware-Control Flow

```text
User selects a hardware control
              ↓
Flask route processes the request
              ↓
Flask reads the Node-RED URL from .env
              ↓
Flask sends an HTTP request to Node-RED
              ↓
Node-RED creates the required serial command
              ↓
Arduino receives and processes the command
              ↓
The LED or servo motor responds
```

## Technologies Used

### Backend

* Python
* Flask
* psutil
* requests
* pyserial
* python-dotenv
* Werkzeug

### Frontend

* HTML
* CSS
* Jinja templates

### Automation and Communication

* Node-RED
* HTTP requests
* USB serial communication
* JSON-based device-state storage

### Hardware

* Raspberry Pi
* Arduino
* Breadboard
* LED
* Servo motor
* USB cable
* Jumper wires

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Arduino IDE

## Repository Structure

```text
raspberry-pi-smart-home-server/
│
├── app.py
├── HomeServerProject_ArduinoCode.ino
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── templates/
│   ├── flaskapp.html
│   ├── status.html
│   ├── files.html
│   └── controls.html
│
├── UploadedFiles/
│
├── node-red/
│   └── flows.json
│
└── docs/
    └── images/
        ├── Smart Home Server Main Screen.png
        ├── Smart Home Server System Status.png
        ├── Smart Home Server File Hub.png
        └── Smart Home Server Device Controls.png
```

The local `.env`, virtual environment, generated device-state file, Python cache files, and uploaded user files are excluded from version control.

## Installation and Setup

### Prerequisites

Before running the project, make sure the following are available:

* Raspberry Pi running Raspberry Pi OS
* Python 3
* Arduino and USB cable
* Node-RED
* Arduino IDE
* Git
* Internet connection for initial package installation

## 1. Clone the Repository

```bash
git clone https://github.com/JoeyC18/raspberry-pi-smart-home-server.git
cd raspberry-pi-smart-home-server
```

## 2. Install Python Virtual-Environment Support

Raspberry Pi OS uses a system-managed Python environment. The project should therefore run inside a virtual environment rather than installing packages system-wide.

```bash
sudo apt update
sudo apt install python3-venv python3-full -y
```

## 3. Create the Virtual Environment

```bash
python3 -m venv venv
```

## 4. Activate the Virtual Environment

```bash
source venv/bin/activate
```

After activation, the terminal should begin with:

```text
(venv)
```

## 5. Install Python Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The dependencies include `python-dotenv`, which allows the application to load local configuration values from a `.env` file.

## 6. Configure Environment Variables

Create a local `.env` file from the included example:

```bash
cp .env.example .env
```

Open the new file:

```bash
nano .env
```

The default configuration should contain:

```env
NODE_RED_BASE_URL=http://127.0.0.1:1880
```

Use `127.0.0.1` when Flask and Node-RED are running on the same Raspberry Pi.

When Node-RED is running on a different device, replace the address with that device's IP address:

```env
NODE_RED_BASE_URL=http://192.168.1.100:1880
```

Save the file in `nano` using:

```text
Ctrl + O
Enter
Ctrl + X
```

The `.env` file is excluded from Git and should not be committed. The `.env.example` file is safe to commit because it contains only an example configuration.

## 7. Start Node-RED

Start Node-RED before using the hardware-control features:

```bash
node-red-start
```

Open Node-RED in a browser:

```text
http://YOUR_PI_IP:1880
```

Import the included flow:

```text
node-red/flows.json
```

Confirm that:

* The flow has been deployed
* The HTTP endpoints match the routes expected by `app.py`
* The serial node uses the correct Arduino port
* The baud rate matches the Arduino program

To automatically start Node-RED when the Raspberry Pi boots:

```bash
sudo systemctl enable --now nodered.service
```

Check the Node-RED service status with:

```bash
sudo systemctl status nodered
```

## 8. Upload the Arduino Program

1. Open `HomeServerProject_ArduinoCode.ino` in the Arduino IDE.
2. Select the correct Arduino board.
3. Select the correct USB port.
4. Confirm that the LED and servo connections match the pins defined in the program.
5. Upload the program to the Arduino.
6. Connect the Arduino to the Raspberry Pi through USB.

Check the Arduino serial port with:

```bash
ls /dev/ttyACM*
```

The device will commonly appear as:

```text
/dev/ttyACM0
```

If the device appears under a different port, update the Node-RED serial node before deploying the flow.

## 9. Run the Flask Application

```bash
python app.py
```

The Flask development server runs on port `5001`.

## 10. Open the Dashboard

Find the Raspberry Pi IP address:

```bash
hostname -I
```

Open the dashboard in a browser:

```text
http://YOUR_PI_IP:5001
```

Replace `YOUR_PI_IP` with the Raspberry Pi's local IP address.

When opening the dashboard directly on the Raspberry Pi, use:

```text
http://127.0.0.1:5001
```

## 11. Stop the Application

Press:

```text
Ctrl + C
```

Then deactivate the virtual environment:

```bash
deactivate
```

## Running the Project Again

After completing the initial setup, restart the project using:

```bash
cd raspberry-pi-smart-home-server
source venv/bin/activate
node-red-start
python app.py
```

Then open:

```text
http://YOUR_PI_IP:5001
```

## Environment Configuration

The application loads the Node-RED server address using:

```python
NODE_RED_BASE_URL = os.getenv(
    "NODE_RED_BASE_URL",
    "http://127.0.0.1:1880"
).rstrip("/")
```

This provides two benefits:

1. The Node-RED address can be changed without editing `app.py`.
2. The local configuration can remain private and separate from the source code.

The default fallback is:

```text
http://127.0.0.1:1880
```

This fallback is used when the environment variable is missing.

### `.env.example`

The repository includes:

```text
.env.example
```

Its contents are:

```env
NODE_RED_BASE_URL=http://127.0.0.1:1880
```

A new user should copy this file rather than editing it directly:

```bash
cp .env.example .env
```

## Node-RED Configuration

The included Node-RED flow handles communication between Flask and the Arduino.

Before deploying the flow, confirm that:

* The HTTP endpoints match the URLs used in `app.py`
* The serial node uses the correct Arduino port
* The serial baud rate matches the Arduino program
* The Arduino is connected before deploying the flow
* The Node-RED flow has been successfully deployed

The Flask application expects Node-RED routes such as:

```text
/led/on
/led/off
/servo/0
/servo/90
/servo/180
/servo/<custom-angle>
```

## Python Dependencies

The required packages are stored in:

```text
requirements.txt
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

To update the dependency file after installing a new package:

```bash
python -m pip freeze > requirements.txt
```

To confirm that `python-dotenv` is installed:

```bash
python -m pip show python-dotenv
```

## Troubleshooting

### Node-RED Connection Refused

An error similar to the following means Flask cannot connect to Node-RED:

```text
ConnectionRefusedError: [Errno 111] Connection refused
```

Confirm that Node-RED is running:

```bash
node-red-start
```

Test the connection:

```bash
curl http://127.0.0.1:1880
```

Check the service:

```bash
sudo systemctl status nodered
```

Also confirm that the value in `.env` is correct:

```bash
cat .env
```

Expected local configuration:

```env
NODE_RED_BASE_URL=http://127.0.0.1:1880
```

### Arduino Serial Port Not Found

Check the available serial devices:

```bash
ls /dev/ttyACM*
ls /dev/ttyUSB*
```

Reconnect the Arduino and confirm that the Node-RED serial node uses the detected port.

### Python Packages Cannot Be Installed

Make sure the virtual environment is active:

```bash
source venv/bin/activate
```

The terminal should begin with:

```text
(venv)
```

Then run:

```bash
python -m pip install -r requirements.txt
```

Do not use `--break-system-packages`.

### `.env.example` Is Ignored by Git

The `.gitignore` file should contain:

```gitignore
.env
.env.*
!.env.example
```

This ignores private environment files while allowing `.env.example` to be committed.

## Security Considerations

This project is designed primarily for use on a trusted local network.

Before allowing remote access:

* Add user authentication
* Protect hardware-control routes
* Validate uploaded file types
* Set upload-size limits
* Keep private configuration in environment variables
* Do not commit `.env`
* Avoid exposing Node-RED directly to the public internet
* Use HTTPS and secure network configuration
* Disable Flask debug mode in a production deployment

The repository excludes virtual environments, generated Python files, runtime state files, private environment files, and uploaded user content through `.gitignore`.

## Current Limitations

* The application is primarily designed for local-network use
* Device controls require Node-RED and the Arduino to remain connected
* Uploaded files are stored locally rather than in a database
* User authentication has not yet been implemented
* Hardware connection failures may require restarting the serial connection
* The system currently controls only an LED and servo motor
* Flask uses its development server rather than a production WSGI server

## Future Improvements

* Raspberry Pi camera streaming
* User authentication and authorization
* Real-time updates through WebSockets
* Database-backed file and device records
* Live hardware connection status
* Additional sensors and smart-home devices
* Secure remote access
* Improved mobile responsiveness
* Automated testing
* GitHub Actions integration
* Docker deployment
* Production deployment using Gunicorn
* Improved error logging and recovery
* User-friendly hardware connection error messages

## Skills Demonstrated

* Full-stack web development
* Flask routing and template rendering
* Raspberry Pi system monitoring
* File-upload and storage management
* HTTP communication
* Environment-variable configuration
* Portable application design
* Node-RED automation
* Arduino programming
* Serial communication
* Embedded hardware control
* Input validation
* Device-state management
* Git and GitHub workflow
* Python virtual environments
* Dependency management
* Technical documentation

## Project Status

The current prototype is functional.

The following components have been implemented and tested:

* Main dashboard
* Live system monitoring
* File uploading, downloading, and deletion
* LED control
* Preset servo control
* Custom servo-angle control
* Device-state preservation
* Flask-to-Node-RED HTTP communication
* Node-RED-to-Arduino serial communication
* Environment-based Node-RED configuration

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Developed by **Joey Coifman**

GitHub: [JoeyC18](https://github.com/JoeyC18)
