# Overview
To have commands run automatically after your Raspberry Pi starts up, you can use the crontab or create a custom systemd service. Each method has its benefits, with the systemd approach being more robust and offering better handling for processes that need to keep running or restart on failure.

# Using Crontab
Edit the crontab: Open the terminal and type:
```
crontab -e
```
Add a new entry: To run your script at reboot, add the following line at the end of the crontab file:

```
@reboot cd /home/user/matter/matter.js/packages/matter-node.js-examples/ && npm run matter-device -- -type socket --on="/home/user/relay.sh CH1 OFF" --off="/home/user/relay.sh CH1 ON" -loglevel debug 2>&1 | tee -a /home/user/matter_output.log
```
Save and exit: After adding the line, save the file and exit the editor. The crontab will automatically apply the new settings.

# Using Systemd Service
Creating a systemd service offers more control over the process management.
Create a systemd service file: Open a new file in `/etc/systemd/system/`, for example `matter-device.service`, using a text editor like nano:

```
sudo nano /etc/systemd/system/matter-device.service
```
Add the following line
```
[Unit]
Description=Start Matter Device Service at boot
After=network.target

[Service]
Type=simple
User=user
WorkingDirectory=/home/user/matter/matter.js/packages/matter-node.js-examples/
ExecStart=/usr/bin/npm run matter-device -- -type socket --on="/home/user/relay.sh CH1 OFF" --off="/home/user/relay.sh CH1 ON" -loglevel debug
StandardOutput=append:/home/user/matter_output.log
StandardError=inherit
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Reload systemd to read new service file:

```
sudo systemctl daemon-reload
```
Enable the service to start at boot:

```
sudo systemctl enable matter-device.service
```
Start the service to test:

```
sudo systemctl start matter-device.service
```
Check the status of your service:

```
sudo systemctl status matter-device.service
```
Considerations
Permissions: Make sure the scripts have the appropriate permissions and that the user specified in the systemd service (User=user) has the necessary permissions to execute the scripts and write to the log file.
Environment: For the systemd service, you might need to add Environment= lines if your script requires specific environment variables.
Logging: Both methods will append the output to /home/user/matter_output.log. Ensure that you have the correct paths and permissions set up for logging.
Using systemd is generally preferred for production environments due to its robustness and features like auto-restarting on failure and dependency management.

# Creating the sound file
In Windows PowerShell
```
Add-Type -AssemblyName System.speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile("C:\Users\potto\Documents\output.wav")
$synth.Speak("Matter is fun.")
$synth.Dispose()
```