from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    flat_array = img_array.flatten()

    # Repeat the key to match the length of the flat array
    key_array = np.tile(key, len(flat_array) // len(key) + 1)[:len(flat_array)]
    
    # Perform XOR operation between the image array and the key
    encrypted_array = flat_array ^ key_array
    
    # Reshape the encrypted array back to the original image shape
    encrypted_img_array = encrypted_array.reshape(img_array.shape)
    encrypted_img = Image.fromarray(encrypted_img_array.astype('uint8'))
    
    # Save the encrypted/decrypted image
    encrypted_img.save(output_path)

def get_user_input(prompt):
    return input(prompt)

def main():
    while True:
        choice = get_user_input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

        if choice == 'q':
            print("Exiting the program.")
            break

        if choice not in ['e', 'd']:
            print("Invalid choice. Please try again.")
            continue

        input_path = get_user_input("Enter the path to the input image: ")
        output_path = get_user_input("Enter the path for the output image: ")
        key = get_user_input("Enter the encryption/decryption key (a string of numbers): ")

        try:
            key = [int(k) for k in key.split()]
        except ValueError:
            print("Invalid key format. Please enter a string of numbers separated by spaces.")
            continue

        try:
            encrypt_decrypt_image(input_path, output_path, key)
            print(f"Image {'encrypted' if choice == 'e' else 'decrypted'} successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
