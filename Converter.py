from PIL import Image
import numpy as np
import os

# Get the current directory of the script
script_dir = os.path.dirname(__file__)
# Define the relative path to the image
image_path = os.path.join(script_dir, 'Example.jpg')
new_array_len = 0




def image_to_array(image_path):
    """ takes in the path to the image and returns its array"""
    """ Each cell contains three numbers representing rgb values"""

  
    with Image.open(image_path) as img:
      
        img_array = np.array(img)
        global new_array_len
        new_array_len = len(img_array) //2
        print(img_array[0][0][1])
    


def create_new_array():
     """ creates a new array full of zeros that is 1/2 the size of the origional array     """
     """" takes in no input, uses global new_array_len int   """
     """returns the new array"""
    
     global new_array_len
     new_array = [[]]
     for i in range(new_array_len):
         new_array.append([255,226,227])
     return new_array
  
def color_averager(img_array,new_array):
    """ examines origional array, find average color for group of two pixels, and then assigns it to the new array"""   

    #  TIP -->to change a specific r g or b  value use a third index ie to access the blue value for a pixel use array[0][0][2] = 220

  
        
        

def array_to_image(array):
    # Convert a numpy array back to an image
    return Image.fromarray(array)




def main():
  image_to_array(image_path)
  print(new_array_len)

    
    
    
    
    # new_image = array_to_image(copied_array)
    # new_image.show()

  

if __name__ == '__main__':
     main()

