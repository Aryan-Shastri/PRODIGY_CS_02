from PIL import Image
import numpy as np

def main():
    while True:
        choice = input("Select (e)ncryption, (d)ecryption, or (q)uit: ").lower()
        if choice == 'e':
            encrypt_image()
        elif choice == 'd':
            decrypt_image()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def get_key():
    try:
        return int(input("Enter the encryption/decryption key: "))
    except ValueError:
        print("Invalid key. Please enter a valid integer.")
        return get_key()

def get_image_location():
    return input("Enter the image file path: ")

def process_image(image_location, key, operation):
    original_image = Image.open(image_location)
    image_array = np.array(original_image)
    processed_pixels = (image_array + operation * key) % 256
    processed_image = Image.fromarray(processed_pixels.astype('uint8'))
    return processed_image

def encrypt_image():
    key = get_key()
    image_location = get_image_location()
    encrypted_image = process_image(image_location, key, operation=1)
    encrypted_image.save('/content/encrypted.png')
    print("Image encryption completed.")

def decrypt_image():
    key = get_key()
    image_location = get_image_location()
    decrypted_image = process_image(image_location, key, operation=-1)
    decrypted_image.save('/content/decrypted.png')
    print("Image decryption completed.")

if __name__ == "__main__":
    main()