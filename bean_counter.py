







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

# Count all locations of red pixels 
red_pixel_count = len(red_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height

# Divide by the total pixels in the image
red_pixel_percentage = red_pixel_count / total_pixels * 100
print(f"{red_pixel_percentage}%")