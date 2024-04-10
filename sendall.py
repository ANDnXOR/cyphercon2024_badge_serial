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

def setup_serial(port: str, delay_ms: int) -> serial.Serial:
    timeout_s = delay_ms / 1000.0  # Convert milliseconds to seconds for timeout
    ser = serial.Serial(port, baudrate=9800, bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        timeout=timeout_s)
    return ser

def send_packet_and_wait_for_reply(ser: serial.Serial, packet: bytes) -> bool:
    if not ser.isOpen():
        ser.open()
    ser.write(packet)
    ser.flush()
    # Wait for a reply within the timeout period
    reply = ser.read(size=len(packet))  # Assuming the reply packet has the same length
    return len(reply) > 0

def send_badges(port: str, start_badge_id: int, end_badge_id: int, delay_ms: int):
    ser = setup_serial(port, delay_ms)
    try:
        for badge_id in range(start_badge_id, end_badge_id + 1):
            packet = generate_packet(badge_id)
            if send_packet_and_wait_for_reply(ser, packet):
                print(f"Packet sent and acknowledged by badge ID: {badge_id}")
            else:
                print(f"No reply received from badge ID: {badge_id}")
            # Additional delay if needed, otherwise it goes to the next badge ID immediately
            time.sleep(delay_ms / 1000.0)
    finally:
        ser.close()

def main():
    parser = argparse.ArgumentParser(description="Send packets to a range of badges via serial port and wait for replies.")
    parser.add_argument('port', type=str, help="Serial port (e.g., COM3 or /dev/ttyUSB0)")
    parser.add_argument('--delay', type=int, default=100, help="Delay between sends in milliseconds (default: 100ms)")
    parser.add_argument('start_badge_id', type=int, help="Start of the badge ID range (inclusive)")
    parser.add_argument('end_badge_id', type=int, help="End of the badge ID range (inclusive)")
    
    args = parser.parse_args()

    send_badges(args.port, args.start_badge_id, args.end_badge_id, args.delay)

if __name__ == "__main__":
    main()
