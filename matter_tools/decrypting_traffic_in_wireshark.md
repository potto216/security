# Decrypting Traffic in Wireshark
With the session keys now being logged, you can capture new traffic and use the keys to decrypt the messages in Wireshark.

## Capture New Traffic
1. Restart Wireshark Capture

Start a new Wireshark capture:
```
sudo tshark -i lo -w /path/to/save/new_dump.pcap
```
2. Run the Matter Nodes Again
* Start the commissioner and the device node as before.
* Perform the commissioning process.

3. Stop the Capture

After commissioning, stop the Wireshark capture.

## Retrieve Session Keys
1. Locate the Session Key Logs

The session keys are logged with the prefix CRYPTOGRAPHIC_KEY_MATERIAL. Search your logs for entries that look like this:
```
2024-02-14 18:13:29.055 DEBUG SecureSession        CRYPTOGRAPHIC_KEY_MATERIAL Session keys for establishment: decryptKey=be3f6f29d4557ee7332cf960e92f8226, encryptKey=cf4838d0465ad7a71ae1635a90639fd6, attestationKey=86eaf1de655cea2dafa29d6dd6231f53, peerNodeId=0016cc3d4f5e6a7b, peerSessionId=12345, context=someContext, id=67890, fabric=00aa11bb22cc33dd
```
2. Extract the Keys
* Decrypt Key: be3f6f29d4557ee7332cf960e92f8226
* Encrypt Key: cf4838d0465ad7a71ae1635a90639fd6
* Peer Node ID: 0016cc3d4f5e6a7b
* Peer Session ID: 12345
* Fabric ID: 00aa11bb22cc33dd

## Configure Wireshark for Decryption
1. Open Wireshark and load the new capture file.
2. Navigate to Protocol Preferences
* Go to Edit > Preferences.
* Expand the Protocols list.
* Scroll down and select Matter.
3. Add Session Keys
* In the Matter protocol preferences, find the section for adding encryption keys.
* Click on Edit or New to add a new key.
4. Enter Key Information
* Session Key: Enter the decryptKey value.
* Peer Node ID: Enter the corresponding peerNodeId value.
* Session ID: Enter the peerSessionId value.
* Fabric ID: Enter the fabricId value.
* Repeat this process for the encryptKey as well.
5. Apply and Close
* Click OK to save the keys.
* Close the preferences window.
## Verify Decryption
* Examine the Packet List: The encrypted Matter messages should now be decrypted, and you can view the plaintext contents within Wireshark.
* Look for Decrypted Messages: Check the packets that were previously encrypted to confirm that the Matter dissector is now displaying the decrypted data.