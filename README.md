# lumos-table (working title)

Include the module into your python script with "include lumos".

Use one of these functions:

lumos.push(frame[string],repeat[bolean])	> Push frame to the matrix (top left -> bottom right)

lumos.clear()				> Turn all pixels off

lumos.pixel_brightness(hex_color,brightness_offset) 

## Frame

A frame consists of a string containing all the hex values for each pixel, for example "FFFFFF000000FFFFFF" makes the first and third led light up. The order of the pixels is from the top left to the bottom right. 
