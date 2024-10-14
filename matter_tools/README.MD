## To create an apply patches to matter.js
```
cd matter.js
git diff > ~/security/matter_tools/patches/matter.js_log_crypto_code_only.2024-10-14.patch
git apply ~/security/matter_tools/patches/matter.js_log_crypto_code_only.2024-10-14.patch
```
To make sure the patches do not trailing have whitespaces
## Enable Whitespace Visualization:
* Press Ctrl+Shift+P to open Settings.
* In the search bar, type "Render Whitespace".
* Set Render Whitespace to "all".
This setting will display all whitespace characters in your file, making it easier to spot trailing spaces or tabs.

# Trim Trailing Whitespace
* Press Ctrl+Shift+P to open Settings.
* Search for "Trim Trailing Whitespace".

## Build Matter.js devices
```
cd matter.js/
npm install
npm run build
```

# Run the Matter.js devices
Setup the network capture. Because of sudo may not be able to create in the user home because of a permission denied error so create in tmp.
```
sudo tshark -i lo -w /tmp/matter_c1.pcap
```

Run the on off device and log the screen output
```
npm run matter-device -- -type socket --on="echo on >> /home/user/device_status.txt" --off="echo off >> /home/user/device_status.txt" -loglevel silly | tee ~/dev01_output.txt
```
Run the shell to commission and communicate with the on off device
```
npm run shell 2 -loglevel debug | tee ~/dev02_output.txt
```
 
In the shell  commission and run some commands. Assume the commissioned on off switch has a node id of 17837896651463445342
```
commission pair
commands onoff on 17837896651463445342 1
commands onoff off 17837896651463445342 1
attributes onoff read 17837896651463445342 1
commission unpair 17837896651463445342
```
Now move the capture into the home directory and make it modifable. 
```
sudo chmod 777 /tmp/matter_c1.pcap 
mv /tmp/matter_c1.pcap .
sudo mv /tmp/matter_c1.pcap ~
sudo chown user:user ~/matter_c1.pcap 
```
