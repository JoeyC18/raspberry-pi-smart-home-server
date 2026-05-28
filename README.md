# Raspberry Pi Smart Home Server

A Raspberry Pi-based smart home server built using Flask, Node-RED, and Arduino integration. The project combines web development, system monitoring, file management, and hardware control into a single local dashboard.

---

# Features

## System Monitoring

* Real-time CPU usage monitoring
* RAM usage tracking
* Disk/storage monitoring
* System uptime display
* Local IP address display
* Auto-refreshing dashboard

---

## File Management

* Upload files directly to the Raspberry Pi
* Persistent file storage system
* Dynamic file listing
* File deletion
* Total folder storage calculation
* Individual file size formatting (KB / MB / GB)

---

## Hardware Control

* LED ON/OFF control through web interface
* Servo motor control
* Custom servo angle input
* Arduino integration through serial communication
* Node-RED HTTP endpoint control system

---

# System Architecture

```text
Frontend (HTML/CSS + Jinja)
        ↓
Flask Web Server (Python)
        ↓
HTTP Requests (requests library)
        ↓
Node-RED (running on Raspberry Pi)
        ↓
Serial Communication (USB)
        ↓
Arduino (hardware controller)
        ↓
Physical Devices (LED, Servo)
```

---

# Technologies Used

## Backend

* Python
* Flask
* psutil
* requests
* os

## Frontend

* HTML
* CSS
* Jinja Templates

## Hardware / Systems

* Raspberry Pi
* Arduino
* Node-RED
* Serial Communication

---

# File Structure

```text
Project1/
│
├── app.py
├── templates/
│   ├── flaskapp.html
│   ├── status.html
│   ├── files.html
│   └── controls.html
│
├── UploadedFiles/
│
├── static/
│
└── README.md
```

---

# Key Concepts Learned

* Flask routing and templating
* Backend-to-frontend data flow
* System monitoring with psutil
* File uploads and storage management
* HTTP requests and API communication
* Node-RED automation flows
* Serial communication between Raspberry Pi and Arduino
* Embedded hardware control
* Git/GitHub version control workflow

---

# Example Data Flow

```text
Button Click
    ↓
Flask Route Triggered
    ↓
HTTP Request Sent to Node-RED
    ↓
Node-RED Sends Serial Command
    ↓
Arduino Receives Command
    ↓
LED / Servo Responds
```

---

# Future Improvements

* Camera streaming integration
* Authentication/login system
* Real-time updates without page refresh
* Sensor feedback system
* Database integration
* Remote access support
* Mobile-responsive UI

---

# Setup Instructions

## Install Dependencies

```bash
pip3 install flask psutil requests pyserial
```

---

## Run Flask Server

```bash
python3 app.py
```

---

## Access Dashboard

```text
http://YOUR_PI_IP:5000
```

---

# Project Status

Currently in active development.

Core dashboard, file management system, Node-RED integration, and Arduino hardware controls are functional.
