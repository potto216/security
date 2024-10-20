import argparse
import re
import time

# Updated regular expression to capture hex values in different log formats
pattern1 = re.compile(r"AES_CCM_(encrypt|decrypt) (key|nonce) = 0x([0-9a-fA-F]+)")
pattern2 = re.compile(r"CRYPTOGRAPHIC_KEY_MATERIAL Key: ([0-9a-fA-F]+), Nonce: ([0-9a-fA-F]+)")

# Lists to hold the extracted hex values
keys = []
source_node_ids = []

def process_line(line):
    # Check first pattern
    match = pattern1.search(line)
    if match:
        operation, type_, value = match.groups()
        if type_ == 'key':
            if value not in keys:
                keys.append(value)
        elif type_ == 'nonce':
            source_node_id = value[-16:]  # Extract the source node id from the nonce
            source_node_id = ''.join(reversed([source_node_id[i:i+2] for i in range(0, len(source_node_id), 2)]))
            if source_node_id not in source_node_ids:
                source_node_ids.append(source_node_id)
    
    # Check second pattern
    match = pattern2.search(line)
    if match:
        key, nonce = match.groups()
        if key not in keys:
            keys.append(key)
        source_node_id = nonce[-16:]
        source_node_id = ''.join(reversed([source_node_id[i:i+2] for i in range(0, len(source_node_id), 2)]))
        if source_node_id not in source_node_ids:
            source_node_ids.append(source_node_id)

def update_file(update_file_name):
    with open(update_file_name, "w") as f:
        f.write("[SessionKeys]\n")
        for index, key in enumerate(keys, start=1):
            f.write(f"Key{index} = {key}\n")
        f.write("[NodeIDs]\n")
        for index, node_id in enumerate(source_node_ids, start=1):
            f.write(f"SourceNodeID{index} = {node_id}\n")

def main(args):
    last_update_time = time.time() - args.min_duration

    if args.input_file:
        with open(args.input_file, 'r') as file:
            lines = file.readlines()
    else:
        import serial
        ser = serial.Serial(args.serial_port, args.baud_rate, timeout=None)
        lines = iter(lambda: ser.readline().decode('utf-8'), '')

    with open(args.output_file_name, "w") as file:
        try:
            for line in lines:
                file.write(line)
                process_line(line)
                print(line.strip())
                current_time = time.time()
                if current_time - last_update_time >= args.min_duration:
                    update_file(args.update_file_name)
                    last_update_time = current_time
        except KeyboardInterrupt:
            print("Interrupted by the user")
            update_file(args.update_file_name)

    update_file(args.update_file_name)
    print("Collected keys:", keys)
    print("Collected nonces:", source_node_ids)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read data and extract hex values.")
    parser.add_argument("--serial_port", default='COM1', help="Serial port to use (default: COM1).")
    parser.add_argument("--baud_rate", type=int, default=115200, help="Baud rate for serial communication (default: 115200).")
    parser.add_argument("--min_duration", type=int, default=10, help="Minimum duration in seconds between updates (default: 10).")
    parser.add_argument("--update_file_name", default="hex_values.txt", help="File name for the hex values output (default: hex_values.txt).")
    parser.add_argument("--output_file_name", default="output.txt", help="File name for the serial data output (default: output.txt).")
    parser.add_argument("--input_file", help="Optional input file to read from instead of serial port.")
    
    args = parser.parse_args()
    main(args)
