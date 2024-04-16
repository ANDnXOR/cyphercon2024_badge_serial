def calculate_intel_hex_checksum(badge_id):
    # Convert the badge ID to a 2-byte little-endian format
    badge_id_bytes = badge_id.to_bytes(2, 'little')
    
    # Construct the record content before checksum
    # Start with :02000000 which is the standard header for this type of record
    header = ':02000000'
    # Convert each byte to a two-character hex string and uppercase it
    data = ''.join(f'{b:02X}' for b in badge_id_bytes)
    record_without_checksum = header + data
    
    # Calculate the checksum:
    # Convert all bytes including header to integers
    byte_values = [
        int(record_without_checksum[i:i+2], 16) for i in range(1, len(record_without_checksum), 2)
    ]
    # Sum all byte values
    total_sum = sum(byte_values)
    # Get the least significant byte of the sum
    lsb = total_sum & 0xFF
    # Compute the two's complement of the LSB
    checksum = (~lsb + 1) & 0xFF
    
    # Complete the record with the checksum
    full_record = record_without_checksum + f'{checksum:02X}'
    
    return full_record

# Example usage:
badge_id = 757
record = calculate_intel_hex_checksum(badge_id)
print("Generated Intel HEX Record:", record)

