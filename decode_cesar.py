# cesar cypher -3
# hiztegia: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/: ,.
# kodea: 3
# testua: enperadorea.txt

def decrypt(text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/: ,."
    decrypted_text = ""
    
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - 3) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
            
    return decrypted_text

if __name__ == "__main__":
    with open("step_4/enperadorea.txt", 'r') as f:
        content = f.read()
    
    decrypted_content = decrypt(content)
    print("\nDecrypted content:")
    print(decrypted_content)