# lumos-table (working title)

Include the module into your python script with "include lumos".


---
#functions

```lumos.push(frame,repeat)```

> Send a hexadeximal frame to the output, for example: "FF0000FFFFFF000000FFFF0000FF00....."

> Choose if the rest of the screen needs to be black (False) or needs to repeat the image (True)


```lumos.clear()```

> Turn all pixels off



```lumos.brightness(frame,offset)```

> Change hex color brightness, offset in percentages (50 is half, 200 is double brightness)



```lumos.master_brightness(offset)```				

> Change general brightness



```lumos.console(message) ```

> Get your message/error on the console together with the others

