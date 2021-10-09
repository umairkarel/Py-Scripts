# Basic Steganography with Python
## Approach
Every image file ends at FFD9 (hex code) i.e the image reader reads image until this code is encountered. so, we can append any data (text, image, exe) to the target image after the hex code 'FFD9' which will remain hidden and won't affect the target image file.