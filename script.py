def binary_to_64bit_hex(binary_value):
	return hex(int(binary_value, 2))[2:].zfill(16)


# Enter the facility bit number from PofZ book
bitNumber = int(input("Enter Facility Bit Number: "))
if bitNumber < 0 or bitNumber > 200:
	print("No facility exist for this bit")
	exit(1)
_feature_index = bitNumber // 64
bitToSet = bitNumber % 64

print(f'_feature array index: {_feature_index}')
print(f'bit position to set: {bitToSet}')

# Create a 64-bit binary string with the specified bit set
bitString = ''.join('1' if i == bitToSet else '0' for i in range(64))

print(f'bit string: {bitString}')

# Convert to 64-bit hexadecimal and format the final mask
final_mask_value = f'0x{binary_to_64bit_hex(bitString)}UL'
print("Mask: ", final_mask_value, end='\n')
