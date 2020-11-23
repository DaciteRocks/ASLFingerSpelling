import cv2
import os
import pandas as pd

delta = 200
ldelta = 60

col_list= ['Frames#', 'rightWrist_x', 'rightWrist_y']
df = pd.read_csv("key_points.csv", usecols=col_list)

col_count = df.shape[0]
for i in range(col_count):
    img_name = str(i) + ".png"
    img = cv2.imread(img_name)

    # These are the points at which the wrist starts. 
    wristy = int(df['rightWrist_y'][i])
    wristx = int(df['rightWrist_x'][i])

    # cropimage = img[wristy-delta:wristy:, wristx:wristx+delta]
    cropimage = img[  wristy-delta:wristy+ldelta,   wristx-ldelta:wristx+delta+ldelta]

    cv2.imshow(str(i)+".png", cropimage)
    cv2.waitKey(1)
