import argparse
import serial
import time

def setup_serial(port):
    """Setup serial connection."""
    ser = serial.Serial(port, 9600, bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.5)
    ser.reset_input_buffer()  # Clear any old data
    return ser

def read_packet(ser, expected_length):
    """Read a packet of a specific expected length from the serial port."""
    buffer = b''
    while len(buffer) < expected_length:
        if ser.in_waiting:
            buffer += ser.read(ser.in_waiting)
        time.sleep(0.1)
    return buffer

def badge_type(remote_id):
    if 0 <= remote_id <= 537:
        return "General"
    elif 538 <= remote_id <= 613:
        return "VIP"
    elif 614 <= remote_id <= 699:
        return "Speaker"
    elif 700 <= remote_id <= 730:
        return "Vendor"
    elif 731 <= remote_id <= 756:
        return "Founder"
    elif 757 <= remote_id <= 767:
        return "Lifetime"
    else:
        return "Unknown"

def process_trade(ser):
    """Process the entire trade sequence based on interactions."""
    header = bytes.fromhex('534E444E21')
    
    # Read initial trade packet from hardware badge
    initiation_packet = read_packet(ser, 10)  # Expecting 10 bytes
    print(f"Raw packet: {initiation_packet.hex().upper()}")

    remote_id = int.from_bytes(initiation_packet[5:7], 'little')
    remote_item = initiation_packet[8]
    remote_type = badge_type(remote_id)
    print(f'Badge ID: {remote_id}  Type: {remote_type}  Item: {remote_item}')

def main(port):
    ser = setup_serial(port)
    try:
        process_trade(ser)
    finally:
        ser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Respond to badge trading protocol, print out Badge ID, Type and Item number")
    parser.add_argument('--port', required=True, help="Serial port, e.g., COM3 or /dev/ttyUSB0")
    args = parser.parse_args()

    print("\nOn your badge, press the 'Pick' button to enter trade mode and then press 'Send' on an item\n")

    try:
        while True:
            main(args.port)
    except KeyboardInterrupt:
        print("Exiting")
