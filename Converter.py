from PIL import Image
import numpy as np
import os

# Disable the decompression bomb warning
Image.MAX_IMAGE_PIXELS = None

# Get the current directory of the script
script_dir = os.path.dirname(__file__)

image_path = os.path.join(script_dir, 'Example.jpg')

def image_to_array(image_path):
    """Takes in the path to the image and returns its array"""
    with Image.open(image_path) as img:
        img_array = np.array(img)
        print(f"Original image array shape: {img_array.shape}")
        return img_array

def create_new_array(old_array):
    """Creates a new array with half the dimensions of the original array"""
    old_height, old_width, _ = old_array.shape
    new_height, new_width = old_height // 2, old_width // 2
    new_array = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    print(f"New image array shape: {new_array.shape}")
    return new_array

def color_averager(old_array, new_array):
    """Finds the average color for groups of four pixels and assigns it to the new array"""
    for i in range(0, old_array.shape[0], 2):
        for j in range(0, old_array.shape[1], 2):
            avg_color = np.mean(old_array[i:i+2, j:j+2], axis=(0, 1))
            new_array[i//2, j//2] = avg_color.astype(np.uint8)
    return new_array

def array_to_image(array, output_path):
    """Convert a numpy array back to an image and save it"""
    img = Image.fromarray(array)
    img.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    img_array = image_to_array(image_path)
    new_array = create_new_array(img_array)
    reduced_img_array = color_averager(img_array, new_array)

    output_path = os.path.join(script_dir, 'Reduced_Image.jpg')
    array_to_image(reduced_img_array, output_path)

if __name__ == '__main__':
    main()
