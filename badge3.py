import argparse
import serial
import time

def generate_packet(badge_id: int) -> bytes:
    """ Generates a packet to send to a badge using its ID. """
    header = bytes.fromhex('534E444E21')
    badge_id_bytes = badge_id.to_bytes(2, 'little')
    command_byte = bytes.fromhex('00')
    packet_without_checksum = header + badge_id_bytes + command_byte
    checksum = (0x100 - sum(packet_without_checksum)) & 0xFF
    final_packet = packet_without_checksum + checksum.to_bytes(1, 'big')
    return final_packet

def setup_serial(port: str) -> serial.Serial:
    """ Sets up serial communication with the given port. """
    ser = serial.Serial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    return ser

def send_packet(ser: serial.Serial, packet: bytes):
    """ Sends a packet through the serial port. """
    if not ser.isOpen():
        ser.open()
    ser.write(packet)
    ser.flush()

def send_badges(ser, badge_ids, delay_ms):
    """ Sends packets to a list of badge IDs via serial port. """
    try:
        for badge_id in badge_ids:
            packet = generate_packet(badge_id)
            send_packet(ser, packet)
            print(f"Sent packet to badge ID: {badge_id}")
            time.sleep(delay_ms / 1000.0)  # Convert milliseconds to seconds
    finally:
        ser.close()

def main():
    parser = argparse.ArgumentParser(description="Send packets to badges via serial port using a list of badge IDs.")
    parser.add_argument('port', type=str, help="Serial port (e.g., COM3 or /dev/ttyUSB0)")
    parser.add_argument('--delay', type=int, default=100, help="Delay between sends in milliseconds (default: 100ms)")
    parser.add_argument('badge_ids', type=str, help="Comma-separated list of badge IDs to send packets to")
    
    args = parser.parse_args()

    badge_ids = list(map(int, args.badge_ids.split(',')))  # Convert the comma-separated string to a list of integers
    ser = setup_serial(args.port)
    send_badges(ser, badge_ids, args.delay)

if __name__ == "__main__":
    main()
