from PIL import Image
import os

# Get the current directory of the script
script_dir = os.path.dirname(__file__)

# Define the relative path to the image
image_path = os.path.join(script_dir, 'Example.jpg')

# Open the image file
image = Image.open(image_path)

# Display the image
image.show()
