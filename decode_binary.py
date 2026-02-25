# decode binary string from step_6/binary.txt
# convert binary to text
def binary_to_text(binary_string):
    cleaned = ''.join(ch for ch in binary_string if ch in '01')
    binary_values = [cleaned[i:i + 8] for i in range(0, len(cleaned), 8)]
    ascii_characters = []
    for b in binary_values:
        if len(b) != 8:
            continue
        try:
            ascii_characters.append(chr(int(b, 2)))
        except (ValueError, OverflowError):
            # If conversion fails, append a placeholder character
            ascii_characters.append('?')
    return ''.join(ascii_characters)

if __name__ == "__main__":
    with open("step_6/binary.txt", 'r') as f:
        binary_string = f.read()
    
    text = binary_to_text(binary_string)
    print(text)