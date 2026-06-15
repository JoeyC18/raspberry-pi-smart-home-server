# Raspberry Pi Smart Home Server

A full-stack Raspberry Pi project that combines system monitoring, local file management, and Arduino hardware control inside one browser-based dashboard.

The application uses Flask as the web server, Node-RED as the communication layer, and USB serial communication to control an LED and servo motor connected to an Arduino.

## Project Demonstrations

### Software Walkthrough

The software walkthrough demonstrates the main dashboard, live Raspberry Pi system information, file management tools, and hardware-control interface.

[![Watch the Software Walkthrough](docs/images/Smart%20Home%20Server%20Main%20Screen.png)](https://youtu.be/jApAIk-ZR-c)

[Watch the Software Walkthrough on YouTube](https://youtu.be/jApAIk-ZR-c)

### Full Hardware Demonstration

The hardware demonstration shows the complete system operating from end to end. Commands are sent from the Flask dashboard to Node-RED and then transferred to the Arduino through USB serial communication to control the LED and servo motor.

[![Watch the Full Hardware Demonstration](docs/images/Smart%20Home%20Server%20Device%20Controls.png)](https://youtube.com/shorts/GVCfA7g-HXs?feature=share)

[Watch the Full Hardware Demonstration on YouTube](https://youtube.com/shorts/GVCfA7g-HXs?feature=share)

## Project Overview

This project was developed to explore how web applications, system utilities, automation platforms, and embedded hardware can be connected within one local network.

The dashboard provides three primary functions:

* Monitoring Raspberry Pi system performance
* Managing files stored on the Raspberry Pi
* Controlling physical hardware through an Arduino

## Features

### System Monitoring

* Live CPU usage
* RAM usage tracking
* Disk and storage monitoring
* System uptime display
* Local IP address display
* Automatically refreshing system information

### File Management

* Upload files through the browser
* Store files locally on the Raspberry Pi
* Display uploaded files dynamically
* Delete files through the dashboard
* Display individual file sizes
* Calculate total folder storage usage

### Hardware Control

* Turn an LED on and off
* Move a servo motor to preset positions
* Enter a custom servo angle
* Preserve device-state information
* Send HTTP requests from Flask to Node-RED
* Send serial commands from Node-RED to Arduino

## Screenshots

### Main Dashboard

The main dashboard provides access to system monitoring, file management, and device controls.

![Smart Home Server Main Screen](docs/images/Smart%20Home%20Server%20Main%20Screen.png)

### System Status

The system-status page displays live Raspberry Pi information, including CPU usage, memory usage, disk usage, uptime, and local IP address.

![Smart Home Server System Status](docs/images/Smart%20Home%20Server%20System%20Status.png)

### File Management

The file hub allows users to upload, view, and delete files stored on the Raspberry Pi.

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
User selects a control
          ↓
Flask route processes the request
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

### Software

* Python
* Flask
* psutil
* requests
* pyserial
* Node-RED
* HTML
* CSS
* Jinja

### Hardware

* Raspberry Pi
* Arduino
* Breadboard
* LED
* Servo motor
* USB serial connection
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

## Installation and Setup

### Prerequisites

Before running the project, make sure the following are available:

* Raspberry Pi running Raspberry Pi OS
* Python 3
* Arduino and USB cable
* Node-RED
* Arduino IDE
* Internet connection for initial package installation

### 1. Clone the Repository

```bash
git clone https://github.com/JoeyC18/raspberry-pi-smart-home-server.git
cd raspberry-pi-smart-home-server
```

### 2. Install Python Virtual-Environment Support

Raspberry Pi OS uses a system-managed Python environment, so the project should run inside a virtual environment.

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

The terminal should now begin with:

```text
(venv)
```

### 5. Install Python Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 6. Start Node-RED

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

Confirm that the serial node is connected to the correct Arduino port.

### 7. Upload the Arduino Program

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

### 8. Run the Flask Application

```bash
python app.py
```

### 9. Open the Dashboard

Find the Raspberry Pi IP address:

```bash
hostname -I
```

Open the dashboard in a browser:

```text
http://YOUR_PI_IP:5000
```

Replace `YOUR_PI_IP` with the Raspberry Pi's local IP address.

### 10. Stop the Application

Press:

```text
Ctrl + C
```

Then deactivate the virtual environment:

```bash
deactivate
```

## Running the Project Again

After the initial setup, restart the project using:

```bash
cd raspberry-pi-smart-home-server
source venv/bin/activate
node-red-start
python app.py
```

## Node-RED Configuration

The included Node-RED flow handles communication between Flask and the Arduino.

Before deploying the flow, confirm that:

* The HTTP endpoints match the URLs used in `app.py`
* The serial node uses the correct Arduino port
* The serial baud rate matches the Arduino program
* The Arduino is connected before deploying the flow
* The flow has been successfully deployed

## Python Dependencies

The required packages are stored in:

```text
requirements.txt
```

Install them using:

```bash
python -m pip install -r requirements.txt
```

To update the dependency file after installing new packages:

```bash
python -m pip freeze > requirements.txt
```

## Security Considerations

This project is designed primarily for use on a trusted local network.

Before allowing remote access:

* Add user authentication
* Protect all hardware-control routes
* Validate uploaded file types
* Set upload-size limits
* Use environment variables for private configuration
* Avoid exposing Node-RED directly to the public internet
* Use HTTPS and secure network configuration

The repository excludes virtual environments, generated Python files, private state files, and other local development files through `.gitignore`.

## Current Limitations

* The application is primarily designed for local-network use
* Device controls require Node-RED and the Arduino to remain connected
* Uploaded files are stored locally rather than in a database
* User authentication has not yet been implemented
* Hardware connection failures may require restarting the serial connection
* The system currently controls only an LED and servo motor

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
* Improved error logging and recovery

## Skills Demonstrated

* Full-stack web development
* Flask routing and template rendering
* Raspberry Pi system monitoring
* File-upload and storage management
* HTTP communication
* Node-RED automation
* Arduino programming
* Serial communication
* Embedded hardware control
* Input validation
* Device-state management
* Git and GitHub workflow
* Python virtual environments
* Technical documentation

## Project Status

The current prototype is functional.

The following components have been implemented and tested:

* Main dashboard
* Live system monitoring
* File uploading and deletion
* LED control
* Preset servo control
* Custom servo-angle control
* Flask-to-Node-RED communication
* Node-RED-to-Arduino serial communication

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

Developed by **Joey Coifman**

GitHub: [JoeyC18](https://github.com/JoeyC18)
