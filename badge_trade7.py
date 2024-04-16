import argparse
import serial
import time

def calculate_checksum(packet_bytes):
    """Calculate checksum by summing all bytes in the packet."""
    return (0x100 - sum(packet_bytes) & 0xFF) % 0x100

def setup_serial(port):
    """Setup serial connection."""
    ser = serial.Serial(port, 9800, bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.5)
    ser.reset_input_buffer()  # Clear any old data
    return ser

def generate_packet(header, badge_id, command, item, remote_id=None, remote_item=None):
    """Generate different types of packets based on the command."""
    badge_id_bytes = badge_id.to_bytes(2, byteorder='little')
    packet = header + badge_id_bytes + bytes([command])

    if command == 0x03:  # Respond to trade
        packet += bytes([item]) + remote_id.to_bytes(2, 'little') + bytes([remote_item])
    elif command == 0x01:  # End of transmission
        pass  # No additional data

    checksum = calculate_checksum(packet)
    packet += checksum.to_bytes(1, 'big')
    return packet

def read_packet(ser, expected_length):
    """Read a packet of a specific expected length from the serial port."""
    buffer = b''
    while len(buffer) < expected_length:
        if ser.in_waiting:
            buffer += ser.read(ser.in_waiting)
        time.sleep(0.1)
    return buffer

def process_trade(ser, local_id, local_item):
    """Process the entire trade sequence based on interactions."""
    header = bytes.fromhex('534E444E21')
    
    # Read initial trade packet from hardware badge
    initiation_packet = read_packet(ser, 10)  # Expecting 10 bytes
    print(f"Received initiation packet: {initiation_packet.hex().upper()}")

    remote_id = int.from_bytes(initiation_packet[5:7], 'little')
    remote_item = initiation_packet[8]

    # Generate and send response packet
    response_packet = generate_packet(header, local_id, 0x03, remote_item, remote_id, local_item)
    ser.write(response_packet)
    print(f"Response packet sent: {response_packet.hex().upper()}")

    # Read echo and actual response (total 26 bytes)
    reply_buffer = read_packet(ser, 26)  # Buffer to include echo + new response
    actual_response = reply_buffer[13:]  # Skip the first 13 bytes (echo of your packet)
    print(f"Actual response packet: {actual_response.hex().upper()}")

    # Generate and send end of transmission packet
    end_packet = generate_packet(header, local_id, 0x01, None)
    ser.write(end_packet)
    print(f"End of transmission packet sent: {end_packet.hex().upper()}")

def main(port, local_id, local_item):
    ser = setup_serial(port)
    try:
        print("Starting badge trade process...")
        process_trade(ser, local_id, local_item)
    finally:
        ser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Respond to badge trading protocol.")
    parser.add_argument('--port', required=True, help="Serial port, e.g., COM3 or /dev/ttyUSB0")
    parser.add_argument('--local_id', type=int, required=True, help="Local badge ID")
    parser.add_argument('--local_item', type=int, required=True, help="Item number the local badge is trading")
    args = parser.parse_args()

    main(args.port, args.local_id, args.local_item)
