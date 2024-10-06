key = [0x4C, 0x50, 0x43, 0x45,0x52, 0x30]

# Open the challenge3 file in binary read mode and create a new file for the output
with open('challenge3', 'rb') as infile, open('output_file', 'wb') as outfile:
    byte = infile.read(1)
    key_length = len(key)
    index = 0
    
    while byte:
        # Convert the byte to an integer
        byte_value = ord(byte)
        
        # XOR with the corresponding key value
        xor_value = byte_value ^ key[index % key_length]
        
        # Write the result to the output file
        outfile.write(bytes([xor_value]))
        
        # Move to the next byte
        byte = infile.read(1)
        index += 1