def rail_fence_cipher(plain_text, num_rails):
    rails = ['' for _ in range(num_rails)]
    direction = 1  # Direction: 1 for downwards, -1 for upwards
    rail_index = 0
   
    for char in plain_text:
        rails[rail_index] += char
        rail_index += direction
       
        # Change direction when reaching top or bottom rail
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1

    cipher_text = ''.join(rails)
    return cipher_text

def main():
    print("******RAILFENCE CIPHER******")
    plain_text = input("Enter the plaintext: ")
    num_rails = int(input("Enter the number of Rails: "))
   
    cipher_text = rail_fence_cipher(plain_text, num_rails)
   
    print("The Cipher text is:")
    print(cipher_text)
    print("Length of cipher text:", len(cipher_text))

if __name__ == "__main__":
    main()
