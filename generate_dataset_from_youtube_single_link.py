import pafy
import cv2
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from shutil import copyfile
import zipfile
import traceback
import time



face_cascade = cv2.CascadeClassifier('D:\\python\\Attendance_system_4th_year\\image\\haarcascade_frontalface_default.xml')


fh = open('error.csv','a')
try:
  link = input('URL: ')
  name = input('Name: ')

  for i in os.listdir():
    if '.jpg' in i or '.mp4' in i or '.temp' in i:
      try:
        os.remove(i)
      except:
        pass

  vPafy = pafy.new(link)
  vid = vPafy.getbest(preftype="mp4")
  vid_file = vid.download(quiet=True)
  time.sleep(0.5)
  cap = cv2.VideoCapture(vid_file)
  c = 0
  err = 0
  while True:
    try:
      _,frame = cap.read()
      frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
      #faces = face_cascade.detectMultiScale(gray, 1.1, 5)
      faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.5,  #1.1
            minNeighbors=5, #5
            minSize=(2,2),  #(1,1)
            flags = cv2.CASCADE_SCALE_IMAGE
        )
    
      for (x, y, w, h) in faces:
          face = frame[y:y+h, x:x+w]
          try:
            face = cv2.resize(face,(94,110),interpolation = cv2.INTER_CUBIC)
            cv2.imwrite("{}_{}.jpg".format(name,c),cv2.cvtColor(face,cv2.COLOR_RGB2BGR))
            print(c)
            c += 1
          except Exception as e:
            print("From for in faces: "+ str(e))
            traceback.print_exc()
            pass
      if c > 3000:
        break
    except:
      traceback.print_exc()
      if err > 10:
        err = 0
        break
      else:
        err += 1
      pass

  if os.path.exists(vid_file):
    cap.release()
    os.remove(vid_file)
  try:
    ziph = zipfile.ZipFile('{}.zip'.format(name), 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(os.getcwd()):
      for file in files:
        print(file)
        if '.jpg' in file and name in file:
          ziph.write(file)
          if os.path.exists(file):
            os.remove(file)

    ziph.close()
    


  except Exception as f:
    print("Exception Zipping : "+ str(f))
    traceback.print_exc()
    pass

except Exception as exc:
  print(str(exc))
  traceback.print_exc()
  for i in os.listdir():
    if '.jpg' in i or '.mp4' in i:
      try:
        os.remove(i)
      except:
        traceback.print_exc()
        pass
  fh.write('{},{}\n'.format(link,name))
  pass
fh.close()
