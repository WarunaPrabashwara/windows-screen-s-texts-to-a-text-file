# pip install opencv-python pyautogui numpy pytesseract
import cv2
import numpy as np
import pyautogui
import time
'''
SCREEN_SIZE = (1920, 1080)
fource = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fource, 20.0, (SCREEN_SIZE))

fps =30
prev = 0

while True:
    time_elapsed = time.time()-prev
    img = pyautogui.screenshot()
    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    cv2.waitKey(1000)

'''


SCREEN_SIZE = (1920, 1080)
#fource = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.mp4', fource, 20.0, (SCREEN_SIZE))

fps =30
prev = 0

from PIL import Image
from pytesseract import pytesseract
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# documentation eka balanna . eke tyenwa meeka ta daana path eka mokadda kiyala 
# r Means 'Raw String'
# Normally, Python uses backslashes as escape characters. Prefacing the string definition with 'r' is a useful way to define a string where you need the backslash to be an actual backslash and not part of an escape code that means something else in the string.
# nattham pAtalena seen ekak tyenne
pytesseract.tesseract_cmd = path_to_tesseract
while True:
    time_elapsed = time.time()-prev
   # img = pyautogui.screenshot('saved.png')
    img = pyautogui.screenshot()
    #image_path = r"saved.png"
    #img = Image.open(image_path)
    if time_elapsed > 1.0/fps:
        prev = time.time()
      #  frame = np.array(img)
     #   frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      #  out.write(frame)
        text = pytesseract.image_to_string(img)
        with open("output.txt", "a") as f:
            f.write( str( text  ) +  "\n\n\n\n" )
      #  with open("my_file2.txt", "a") as f:
     #       f.write( str( frame ) +  "\n\n\n\n" )
     #   with open("my_file3.txt", "a") as f:
     #       f.write( str( frame2 ) +  "\n\n\n\n" )                        
    cv2.waitKey(1000)


