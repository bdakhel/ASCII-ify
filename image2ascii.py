# Image to ASCII converter

import ascii_magic

# Ask user for image file
image = input("Enter image file: ")

output = ascii_magic.from_image_file(image,columns=148)
ascii_magic.to_terminal(output)


