# Raspberry Pi Smart Home Server

A Raspberry Pi-based smart home server developed using Flask, Node-RED, and Arduino integration. The project combines system monitoring, file management, and physical hardware control into one browser-based dashboard.

![Raspberry Pi Smart Home Server](docs/images/Smart%20Home%20Server%20Main%20Screen.png)

## Features

### System Monitoring

* Real-time CPU usage monitoring
* RAM usage tracking
* Disk and storage monitoring
* System uptime display
* Local IP address display
* Automatically refreshing system information

### File Management

* Upload files directly to the Raspberry Pi
* Store files locally on the server
* Dynamically display uploaded files
* Delete files through the web interface
* Display individual file sizes
* Calculate total uploaded-folder storage

### Hardware Control

* Turn a connected LED on and off
* Control a servo motor through the dashboard
* Enter a custom servo angle
* Send commands from Flask to Node-RED
* Communicate with an Arduino through USB serial communication

## Screenshots

### Main Dashboard

The main dashboard provides navigation to the system-status, file-management, and device-control sections of the server.

![Smart Home Server Main Screen](docs/images/Smart%20Home%20Server%20Main%20Screen.png)

### System Status

The system-status page displays live Raspberry Pi information, including CPU usage, memory usage, disk usage, uptime, and local IP address.

![Smart Home Server System Status](docs/images/Smart%20Home%20Server%20System%20Status.png)

### File Management

The file-management page allows users to upload, view, and delete files stored on the Raspberry Pi.

![Smart Home Server File Hub](docs/images/Smart%20Home%20Server%20File%20Hub.png)

### Device Controls

The device-controls page allows users to control an LED and servo motor connected through an Arduino.

![Smart Home Server Device Controls](docs/images/Smart%20Home%20Server%20Device%20Controls.png)

## System Architecture

```text
Web Browser
     ↓
HTML, CSS, and Jinja Templates
     ↓
Flask Web Server
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

## Example Hardware-Control Flow

```text
User clicks a control button
          ↓
Flask route is triggered
          ↓
Flask sends an HTTP request to Node-RED
          ↓
Node-RED sends a serial command
          ↓
Arduino receives the command
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

### Frontend

* HTML
* CSS
* Jinja templates

### Hardware and Systems

* Raspberry Pi
* Arduino
* Node-RED
* USB serial communication
* LED
* Servo motor

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Arduino IDE

## Project Structure

```text
raspberry-pi-smart-home-server/
│
├── app.py
├── HomeServerProject_ArduinoCode.ino
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── flaskapp.html
│   ├── status.html
│   ├── files.html
│   └── controls.html
│
├── UploadedFiles/
│
└── docs/
    └── images/
        ├── Smart Home Server Main Screen.png
        ├── Smart Home Server System Status.png
        ├── Smart Home Server File Hub.png
        └── Smart Home Server Device Controls.png
```

## Key Concepts Learned

* Flask routing and web-server development
* Jinja template rendering
* Backend-to-frontend data flow
* Raspberry Pi system monitoring with psutil
* File upload and storage management
* HTTP communication between Flask and Node-RED
* Serial communication between Raspberry Pi and Arduino
* Embedded hardware control
* Servo-angle validation
* Git and GitHub version-control workflow
* Python virtual environments and dependency management

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JoeyC18/raspberry-pi-smart-home-server.git
cd raspberry-pi-smart-home-server
```

### 2. Install Virtual-Environment Support

Raspberry Pi OS protects its system-managed Python installation. The project should therefore be run inside a virtual environment.

```bash
sudo apt update
sudo apt install python3-venv python3-full -y
```

### 3. Create the Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

```bash
source venv/bin/activate
```

After activation, the terminal should begin with:

```text
(venv)
```

### 5. Install the Required Packages

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Run the Flask Server

```bash
python app.py
```

### 7. Open the Dashboard

Open the following address in a browser:

```text
http://YOUR_PI_IP:5000
```

Replace `YOUR_PI_IP` with the local IP address of the Raspberry Pi.

The IP address can be found by running:

```bash
hostname -I
```

### 8. Stop the Server

Press:

```text
Ctrl + C
```

### 9. Deactivate the Virtual Environment

```bash
deactivate
```

Each time the project is restarted, activate the environment again:

```bash
cd ~/projects/Project1
source venv/bin/activate
python app.py
```

## Python Requirements

The required Python packages are stored in:

```text
requirements.txt
```

To recreate the dependency file after installing or updating packages, run:

```bash
python -m pip freeze > requirements.txt
```

To view the saved dependencies:

```bash
cat requirements.txt
```

## Arduino Setup

1. Open `HomeServerProject_ArduinoCode.ino` in the Arduino IDE.
2. Select the correct Arduino board.
3. Select the correct USB port.
4. Confirm that the LED and servo pins match the physical wiring.
5. Upload the program to the Arduino.
6. Connect the Arduino to the Raspberry Pi using USB.

To check the connected Arduino port on the Raspberry Pi, run:

```bash
ls /dev/ttyACM*
```

The Arduino may appear as:

```text
/dev/ttyACM0
```

## Node-RED Setup

Start Node-RED by running:

```bash
node-red-start
```

Open Node-RED in a browser:

```text
http://YOUR_PI_IP:1880
```

Confirm that:

* The required HTTP endpoints are configured
* The serial node is connected to the correct Arduino port
* The serial baud rate matches the Arduino program
* The Node-RED flow has been deployed
* The Flask application uses the correct Node-RED URLs

## Security Notes

* Do not upload passwords, API keys, or private credentials to GitHub
* Do not upload `.env` files
* Do not commit the `venv` folder
* Do not commit Python `__pycache__` folders
* Do not store private uploaded files in the public repository
* Add authentication before enabling remote access
* Use secure network settings when exposing the server outside the local network

## Current Limitations

* The project currently operates primarily on a local network
* Device controls depend on Node-RED and the Arduino being connected
* Uploaded files are stored locally rather than in a database
* The dashboard does not currently include user authentication
* Hardware connection errors may require restarting the serial connection

## Future Improvements

* Raspberry Pi camera streaming
* User authentication and login system
* Real-time updates without refreshing the page
* Database integration
* Live hardware connection status
* Additional sensors and smart-home devices
* Secure remote access
* Improved mobile responsiveness
* Automated testing
* GitHub Actions integration
* Docker deployment
* Expanded error handling

## Project Status

This project is currently in active development.

The main dashboard, system-monitoring page, file-management system, Node-RED communication, and Arduino hardware controls are functional.

## Author

Developed by **Joey Coifman**

GitHub: `JoeyC18`
