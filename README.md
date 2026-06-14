# Raspberry Pi Smart Home Server

A Raspberry Pi-based smart home server built using Flask, Node-RED, and Arduino integration. The project combines web development, system monitoring, file management, and hardware control into a single local dashboard.

## Features

### System Monitoring

* Real-time CPU usage monitoring
* RAM usage tracking
* Disk and storage monitoring
* System uptime display
* Local IP address display
* Auto-refreshing dashboard

### File Management

* Upload files directly to the Raspberry Pi
* Persistent file storage
* Dynamic file listing
* File deletion
* Total folder storage calculation
* Individual file-size formatting in KB, MB, and GB

### Hardware Control

* LED ON and OFF control through the web interface
* Servo motor control
* Custom servo-angle input
* Arduino integration through serial communication
* Node-RED HTTP endpoint control system

## System Architecture

```text
Frontend (HTML, CSS, and Jinja)
        ↓
Flask Web Server (Python)
        ↓
HTTP Requests
        ↓
Node-RED on Raspberry Pi
        ↓
USB Serial Communication
        ↓
Arduino
        ↓
LED and Servo Motor
```

## Technologies Used

### Backend

* Python
* Flask
* psutil
* requests
* pyserial
* os

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

## Project Structure

```text
raspberry-pi-smart-home-server/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── HomeServerProject_ArduinoCode.ino
│
├── templates/
│   ├── flaskapp.html
│   ├── status.html
│   ├── files.html
│   └── controls.html
│
├── static/
│   └── style.css
│
├── UploadedFiles/
│   └── .gitkeep
│
├── node-red/
│   └── flows.json
│
└── docs/
    └── images/
```

Some folders may be added as the project continues to develop.

## Key Concepts Learned

* Flask routing and templating
* Backend-to-frontend data flow
* System monitoring with psutil
* File uploads and storage management
* HTTP requests and API communication
* Node-RED automation flows
* Serial communication between Raspberry Pi and Arduino
* Embedded hardware control
* Git and GitHub version control

## Example Data Flow

```text
User clicks a dashboard button
        ↓
Flask route is triggered
        ↓
Flask sends an HTTP request to Node-RED
        ↓
Node-RED sends a serial command
        ↓
Arduino receives the command
        ↓
The LED or servo responds
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JoeyC18/raspberry-pi-smart-home-server.git
cd raspberry-pi-smart-home-server
```

### 2. Install Virtual Environment Support

On Raspberry Pi OS, Python packages should be installed inside a virtual environment.

```bash
sudo apt update
sudo apt install python3-venv python3-full -y
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

```bash
source venv/bin/activate
```

Your terminal should now begin with:

```text
(venv)
```

### 5. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Run the Flask Server

```bash
python app.py
```

### 7. Access the Dashboard

Open the following address in a browser:

```text
http://YOUR_PI_IP:5000
```

Replace `YOUR_PI_IP` with the Raspberry Pi's local IP address.

You can find the Raspberry Pi IP address using:

```bash
hostname -I
```

### 8. Deactivate the Virtual Environment

When finished, run:

```bash
deactivate
```

Each time the project is restarted, activate the virtual environment again:

```bash
cd ~/projects/Project1
source venv/bin/activate
python app.py
```

## Requirements

The required Python packages are stored in `requirements.txt`.

To update the file after installing new packages, run:

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
3. Select the correct USB serial port.
4. Confirm that the LED and servo pins match the hardware setup.
5. Upload the code to the Arduino.
6. Connect the Arduino to the Raspberry Pi through USB.

To check the Arduino serial port on the Raspberry Pi, run:

```bash
ls /dev/ttyACM*
```

The Arduino will commonly appear as:

```text
/dev/ttyACM0
```

## Node-RED Setup

1. Start Node-RED on the Raspberry Pi.

```bash
node-red-start
```

2. Open Node-RED in a browser:

```text
http://YOUR_PI_IP:1880
```

3. Import the project flow from:

```text
node-red/flows.json
```

4. Confirm that the serial node uses the correct Arduino port.

5. Deploy the flow.

6. Confirm that the Flask application is sending requests to the correct Node-RED endpoints.

## Hardware Setup

The Arduino is connected to the Raspberry Pi through USB serial communication.

Example components include:

* Raspberry Pi
* Arduino Uno
* LED
* 220-ohm resistor
* Servo motor
* Breadboard
* Jumper wires
* USB cable

The exact Arduino pins should match the values defined in `HomeServerProject_ArduinoCode.ino`.

## Screenshots

Screenshots of the dashboard will be added to the following folder:

```text
docs/images/
```

Planned screenshots include:

* Home dashboard
* System status page
* File manager
* Hardware controls
* Raspberry Pi and Arduino setup

## Security Notes

* Do not upload passwords or API keys to GitHub.
* Do not upload `.env` files.
* Do not store private user-uploaded files in the public repository.
* Use a `.gitignore` file to exclude virtual environments and generated files.
* Remote access should only be added with proper authentication and secure network configuration.

## Future Improvements

* Raspberry Pi camera streaming
* User authentication and login system
* Real-time updates without page refresh
* Sensor feedback and live device status
* Database integration
* Secure remote access
* Mobile-responsive design
* Additional smart-home devices
* Improved error handling
* Automated testing
* GitHub Actions workflow
* Docker deployment

## Project Status

This project is currently in active development.

The core dashboard, system monitoring, file management, Node-RED integration, and Arduino hardware controls are functional.

## Author

Developed by Joey Coifman.

GitHub: `JoeyC18`
