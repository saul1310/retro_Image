from PIL import Image
import os
import numpy as np

# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Define the relative path to the image
image_path = os.path.join(script_dir, 'Example.jpg')

def image_to_array(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Convert the image to grayscale (optional, for simplicity)
        img = img.convert('L')
        # Convert the image to a numpy array
        img_array = np.array(img)
    return img_array

def main():
    # Use the image_path defined earlier
    img_array = image_to_array(image_path)
    print(img_array)

if __name__ == '__main__':
    main()
