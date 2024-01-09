







from PIL import Image 

import colour_helper 

# Visit every pixel in the image
jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height): 
    for x in range(jelly_bean_img.width): 
        # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x, y))

        # If this pixel is red
        if colour_helper.pixel_to_name(current_pixel) == 'red': 
            # Store its location somewhere
            red_pixels.append((x, y))

print(red_pixels)