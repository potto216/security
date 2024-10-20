#!/bin/bash

# Examples to turn on and off the 3 relays different 
# ./relay.sh CH1 ON
# ./relay.sh CH2 ON
# ./relay.sh CH3 OFF

# Validate and set channel based on first argument
if [ "$1" == 'CH1' ]; then
 ch=26
elif [ "$1" == 'CH2' ]; then
 ch=20
elif [ "$1" == 'CH3' ]; then
 ch=21
else
 echo "Parameter error"
 exit 1
fi

# Validate and set state based on second argument
if [ "$2" == 'ON' ]; then
 state='dh'  # Drive High
elif [ "$2" == 'OFF' ]; then
 state='dl'  # Drive Low
else
 echo "Parameter error"
 exit 1
fi

# Set GPIO to output, no pull, and define state (High or Low)
pinctrl set $ch op pn $state

# Optionally, echo back the new pin states
pinctrl -e get $ch

echo "relay $1 set to $2"

