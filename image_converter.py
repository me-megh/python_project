from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format.upper())  # इमेज को नए फॉर्मेट में सेव करना
            print(f'Image successfully converted to {output_format.upper()} and saved as {output_path}')
    except Exception as e:
        print(f"Error: {e}")

def image_converter():
    print("Image Converter")
    input_path = input("Enter the path of the image (e.g., image.jpg): ").strip()

    if not os.path.exists(input_path):  # चेक करें कि इमेज का पाथ सही है
        print("The file does not exist. Please check the path and try again.")
        return

    print("Choose the output format:")
    print("1. JPEG")
    print("2. PNG")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        output_format = "JPEG"
    elif choice == "2":
        output_format = "PNG"
    else:
        print("Invalid choice, please select 1 or 2.")
        return

    # Extract file name and set output path
    base_name = os.path.splitext(input_path)[0]  # पुरानी एक्सटेंशन हटा दो
    output_path = f"{base_name}_converted.{output_format.lower()}"  # नया नाम और फॉर्मेट सेट करें

    convert_image(input_path, output_path, output_format)

if __name__ == "__main__":
    image_converter()