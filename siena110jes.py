from google.colab import files
import numpy
import keras
import matplotlib.pyplot
from PIL import Image
import math

import numpy as np
from IPython.display import Audio
from scipy.io import wavfile

class Pixel:
  def __init__(self, img, row, col):
    self.row = row
    self.col = col
    self.img = img
  

def makePicture( filename ):
  img = keras.preprocessing.image.load_img("/content/"+filename)
  img_array = keras.preprocessing.image.img_to_array(img)
  img_array = img_array/255.0
  #img_array = Image.open("/content/"+filename)
  return img_array

def show( pic ):
  matplotlib.pyplot.axis('off')
  matplotlib.pyplot.imshow(pic)
  matplotlib.pyplot.show()

def pickAFile():
  uploaded = files.upload() 
  #temp = uploaded.keys()
  temp = list(uploaded)
  return temp[0]

def getWidth( pic ):
  return pic.shape[1]

def getHeight( pic ):
  return pic.shape[0]

def getPixel( pic, r, c ):
  return Pixel(pic, r, c)

def getPixels( pic ):
  allpixels = []
  for row in range(0, getHeight( pic )):
    for col in range(0, getWidth( pic )):
      allpixels.append( getPixel(pic, row, col) )
  return allpixels

def setRed( pix, red ):
  pix.img[pix.row, pix.col, 0] = red

def setBlue( pix, blue ):
  pix.img[pix.row, pix.col, 2] = blue

def setGreen( pix, green ):
  pix.img[pix.row, pix.col, 1] = green

def getRed( pix ):
  return pix.img[pix.row, pix.col, 0]

def getBlue( pix ):
  return pix.img[pix.row, pix.col, 2]

def getGreen( pix ):
  return pix.img[pix.row, pix.col, 1]

def getColor( pix ):
  return pix.img[pix.row, pix.col]
def setColor( pix, color ):
  pix.img[pix.row, pix.col, 0] = color[0]
  pix.img[pix.row, pix.col, 1] = color[1]
  pix.img[pix.row, pix.col, 2] = color[2]

def getX(pix):
  return pix.col

def getY(pix):
  return pix.row

def makeColor(r,g,b):
  return [r,g,b]

def makeDarker( color ):
  color[0] = color[0]*0.80
  color[1] = color[1]*0.80
  color[2] = color[2]*0.80

def makeLighter( color ):
  color[0] = color[0]*1.10
  color[1] = color[1]*1.10
  color[2] = color[2]*1.10

