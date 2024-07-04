from PIL import Image
import os
import numpy as np

# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Define the relative path to the image
image_path = os.path.join(script_dir, 'Example.jpg')

def image_to_array(image_path):
    # Open an image file

    # debugging statements to print image deatails
    with Image.open(image_path) as img:
       
        print(f"Image mode: {img.mode}")
        print(f"Image size: {img.size}")
        
        # Convert the image to a numpy array
        img_array = np.array(img)
    return img_array



def reconstruct_new_image():
    img_array = image_to_array(image_path)
    new_array_size=len(img_array) // 2
    new_array =[]

    for i in range(new_array_size):
        new_array.append([0,0,0])
    print(new_array)


 

def main():
    
    # Use the image_path defined earlier
    img_array = image_to_array(image_path)

    reconstruct_new_image()

if __name__ == '__main__':
    main()
