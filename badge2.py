import argparse
import serial
import time

def generate_packet(badge_id: int) -> bytes:
    header = bytes.fromhex('534E444E21')
    badge_id_bytes = badge_id.to_bytes(2, 'little')
    command_byte = bytes.fromhex('00')
    packet_without_checksum = header + badge_id_bytes + command_byte
    checksum = (0x100 - sum(packet_without_checksum)) & 0xFF
    final_packet = packet_without_checksum + checksum.to_bytes(1, 'big')
    return final_packet

def setup_serial(port: str) -> serial.Serial:
    ser = serial.Serial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    return ser

def send_packet(ser: serial.Serial, packet: bytes):
    if not ser.isOpen():
        ser.open()
    ser.write(packet)
    ser.flush()

def send_badges(port: str, start_badge_id: int, end_badge_id: int, delay_ms: int):
    ser = setup_serial(port)
    try:
        for badge_id in range(start_badge_id, end_badge_id + 1):
            packet = generate_packet(badge_id)
            send_packet(ser, packet)
            print(f"Sent packet to badge ID: {badge_id}")
            time.sleep(delay_ms / 1000.0)  # Convert milliseconds to seconds
    finally:
        ser.close()

def main():
    parser = argparse.ArgumentParser(description="Send packets to a range of badges via serial port.")
    parser.add_argument('port', type=str, help="Serial port (e.g., COM3 or /dev/ttyUSB0)")
    parser.add_argument('--delay', type=int, default=100, help="Delay between sends in milliseconds (default: 100ms)")
    parser.add_argument('start_badge_id', type=int, help="Start of the badge ID range (inclusive)")
    parser.add_argument('end_badge_id', type=int, help="End of the badge ID range (inclusive)")
    
    args = parser.parse_args()

    send_badges(args.port, args.start_badge_id, args.end_badge_id, args.delay)

if __name__ == "__main__":
    main()
