import cv2
import os
import pandas as pd

# img = cv2.imread("7.png")

# distx = abs(163.1164779 - 172.3105396) /3
# disty = abs(578.0171026 - 127.8148042) /3

# delta = 250

# wristx = 292
# wristy = 817

# print(img.shape)

# cropimage = img[wristy:wristy+delta, wristx:wristx+delta]

# cropimage = img[wristy-delta:wristy:, wristx:wristx+delta]


# cv2.imshow("cropped", cropimage)
# # cv2.imshow("s", img)
# cv2.waitKey(0)

#path_to_videos = "C:\\Users\\tazer\\Documents\\ASU\\CSE-535\\ASL_Project\\Juan-ASL-Alphabet\\"

delta = 200
# files = os.listdir(path_to_videos)
# for file in files:
#     img = cv2.imread(file)

col_list= ['Frames#', 'rightWrist_x', 'rightWrist_y']
df = pd.read_csv("key_points.csv", usecols=col_list)

col_count = df.shape[0]
for i in range(col_count):
    img_name = str(i) + ".png"
    img = cv2.imread(img_name)

    wristy = int(df['rightWrist_y'][i])
    wristx = int(df['rightWrist_x'][i])
    cropimage = img[wristy-delta:wristy:, wristx:wristx+delta]
    cv2.imshow(str(i)+".png", cropimage)
    cv2.waitKey(1)
