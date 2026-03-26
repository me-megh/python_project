
import os
from PIL import Image
def filter_image(input_path,output_path):
    try:
        with Image.open(input_path) as img:
            bw_img=img.convert('L')
            bw_img.save(output_path)
            print(f"Image successfully converted to Black & White and saved as {output_path}")
    except Exception as e:
        print(f"error:{e}")
    
def img_to_pdf(input_path,output_path):
    try:
        with Image.open(input_path) as img:
            img=img.convert("RGB")
            img.save(output_path,"PDF")
            print(f"Image successfully converted to PDF and saved as {output_path}")
    except Exception as e:
        print(f"error:{e}")
        
def resize_image(input_path,output_path,width,height):
    try:
        with Image.open(input_path) as img:
            img=img.resize((width,height))
            img.save(output_path)
            print(f"Image successfully resized and saved as {output_path}")
    except Exception as e:
        print(f"error:{e}")
        
def convert_image(input_path,output_path,output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path,format=output_format.upper() )
            print(f"image Successfully converted to {output_format.upper()} as saved {output_path} ")
    except Exception as e:
        print(f"Error:{e}")
    
def image_converter():
    print("Welcome ! Image Converter")
    input_path= input("Enter your image path").strip()
    if not os.path.exists(input_path):
        print("the File does not exist, plz try again")
        return
    
    print("Enter your Choice or select any of them: ")
    print("1. Jpeg")
    print("2. png")
    print("3. resize image")
    print("4. image Black n White filter")
    print("5. Convert IMG to PDF")
    choice=input("enter your choice ").strip()
    if choice == "1":
        output_format="jpeg"
    elif choice == "2":
        output_format="png"
    elif choice == "3":
        output_path=input("enter the path where you want to save resize image.").strip()
        width=int(input("Enter width"))
        height=int(input("Enter height"))
        resize_image(input_path,output_path,width,height)
        return
    elif choice == "4":
        output_path=input("enter the path of image you want to add filter.").strip()
        filter_image(input_path,output_path)
        return
    elif choice == "5":
        base_path=os.path.splitext(input_path)[0]
        output_path=f"{base_path}_converted.pdf"
        img_to_pdf(input_path,output_path)
        return
    else:
        print("invalid choice! please enter correct choice")
        return
    base_path=os.path.splitext(input_path)[0]
    output_path=f"{base_path}_converter.{output_format}"
    print(output_path)
    
    convert_image(input_path,output_path,output_format)
image_converter()
