from PIL import Image
import os

# Defining the path where the images are located and getting the name of the files
path = 'images'
saving_path = '/opt/icons/'
file_names = os.listdir(path)

# Iterating over all files which are tiff images
for image in file_names:
  if "48dp" in image: # This selects all images from other existing files
    file = Image.open(path+"/"+image)
    rotate_image = file.rotate(270) # Rotating image as client requested
    resized_image = rotate_image.resize((128, 128))
    reformatted_image = resized_image.convert("RGB")
    reformatted_image.save(saving_path + image + ".jpeg")
  else:
    continue