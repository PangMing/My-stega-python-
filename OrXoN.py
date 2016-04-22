#!/usr/bin/python
#https://poerhiza.github.io/ctf/2014/10/05/tinyCTF-write_ups-erik_baleog_and_olaf/
import numpy, Image
  
 def dumpEachLayer(imageName):
   a1 = numpy.asarray(Image.open(imageName)) # pass Image
   for x in range(0, 255):
     Image.fromarray(numpy.asarray(map(lambda i: i & x, a1)), 'RGB').save('%d.png' % x)
 
 def orEachUpperLower(func, imageOne, imageTwo, imageOut):
   a1 = numpy.asarray(Image.open(imageOne)) # pass Image
   a2 = numpy.asarray(map(lambda i: i & 0x0f, a1)) # lower 4 bits: 0x0f = 00001111
   a1 = numpy.asarray(Image.open(imageTwo)) # decoy Image
   a3 = numpy.asarray(map(lambda i: i & 0xf0, a1)) # higher 4 bits: 0xf0 = 11110000
   a4 = func(a2,a3) # bitwise or of both the images to reproduce 8 bit image.
   img = Image.fromarray(a4, 'RGB')
   img.save(imageOut)
 
 def allBits(func, imageOne, imageTwo, imageOut):
   a1 = numpy.asarray(Image.open(imageOne)) # pass Image
   a2 = numpy.asarray(Image.open(imageTwo)) # decoy Image
   Image.fromarray(func(a1, a2), 'RGB').save(imageOut)
 
 def sub(a1, a2):
   return a1 - a2
 
 # Let's start out dumping all the layer's to see if there is anything there...
 dumpEachLayer('stego100')
 # Nope, all we got was a bunch of images...useless...
 
 # Perhaps there is some funny things going on in the bits?
 orEachUpperLower(numpy.bitwise_or, '22kUrzm.png', 'stego100', 'testOr.png')
 orEachUpperLower(numpy.bitwise_xor, '22kUrzm.png', 'stego100', 'testXor.png')
 orEachUpperLower(numpy.bitwise_and, '22kUrzm.png', 'stego100', 'testAnd.png')
 # Nope...
 
 # Okay...Hmmm, how about playing with all of the bits?
 allBits(numpy.bitwise_or, '22kUrzm.png', 'stego100', 'testOr.png')
 allBits(numpy.bitwise_xor, '22kUrzm.png', 'stego100', 'testXor.png')
 allBits(numpy.bitwise_and, '22kUrzm.png', 'stego100', 'testAnd.png')
 # Nope...
 
 # Welp, we've two images - hell, let's subtract them.
 allBits(sub, '22kUrzm.png', 'stego100', '22kUrzm-stego100.png')
 allBits(sub, 'stego100', '22kUrzm.png', 'stego100-22kUrzm.png')
 # MONEY!