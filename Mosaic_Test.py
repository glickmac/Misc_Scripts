#!/usr/bin/python
#Importing the required libraries
import os, random, argparse
from PIL import Image
import imghdr
import numpy as np

## This tests to make sure the dimensions of all the photos are the same
for filename in os.listdir("images/"):
  print(filename)
  path = "test/"+filename
  x = Image.open(path)
  im = np.array(x)
  w, h, d = im.shape
  

  print(d)

