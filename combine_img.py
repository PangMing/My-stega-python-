#!/usr/bin/env python
import Image

def main():
  new = Image.open('IMG_0001.png')
  w, h = new.size
  for i int range(2, 1122):
    im = Image.open('IMG_%04d.png' % i)
    data= im.split()
    for pixel, value in enumerate(im.getdata()):
      if value[3] !=0: # not transparent
        x, y = (pixel % w, pixel * 1. /w)
        new.putpixel((x,y),value)
  new.save('f200_result.png')
  new.shot()
  
if __name__ == '__main__':
  main()

