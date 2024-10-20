#!/bin/bash

# Path to the text file
FILE="device_status.txt"

# Path to the sound file
SOUND="/home/user/media/on.wav"

# Ensure inotifywait is installed
if ! command -v inotifywait &> /dev/null; then
    echo "inotifywait could not be found, please install inotify-tools."
    exit 1
fi

# Monitor the file for modifications
echo "Monitoring $FILE for changes..."
while inotifywait -e modify "$FILE"; do
    # Check if the last modification introduced the word 'on'
    if tail -n1 "$FILE" | grep -qw "on"; then
        # Play the sound file if 'on' is found
        echo "Word 'on' detected! Playing sound..."
        if command -v paplay &> /dev/null; then
            paplay "$SOUND"
        elif command -v aplay &> /dev/null; then
            aplay "$SOUND"
        else
            echo "No audio player found (aplay or paplay)."
        fi
    fi
done

