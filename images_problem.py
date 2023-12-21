def picture_to_grayscale(filename:str) -> None: 
    """Convert a picture to grayscale"""

    # Open up the image 
    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel 
        for y in range(im.height): 
            for x in range(im.width):
                pixel = im.getpixel((x,y))
                # Take that pixel and convert it to gray
                gray_pixel = colour_helper.pixel_to_grayscale(pixel)
                
                im.putpixel((x,y), gray_pixel)
