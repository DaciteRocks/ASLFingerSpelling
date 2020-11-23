import cv2
import os
import pandas as pd

path_to_video_files = "C:\\Users\\tazer\\Documents\\ASU\\CSE-535\\ASL_Project\\Juan-ASL-Alphabet\\"


video_dir = os.listdir(path_to_video_files)
print(video_dir)

delta = 200
ldelta = 60


for folder in video_dir:

    if os.path.isdir(path_to_video_files + folder):
        
        col_list= ['Frames#', 'rightWrist_x', 'rightWrist_y']
        keypoints = path_to_video_files + folder + "\\key_points.csv"
        # df = pd.read_csv("key_points.csv", usecols=col_list)
        df = pd.read_csv(keypoints, usecols=col_list)

        col_count = df.shape[0]
        for i in range(col_count):
            img_name = str(i) + ".png"
            # img = cv2.imread(img_name)
            img = cv2.imread(path_to_video_files + folder + "\\" + img_name)

            # These are the points at which the wrist starts. 
            wristy = int(df['rightWrist_y'][i])
            wristx = int(df['rightWrist_x'][i])

            # cropimage = img[wristy-delta:wristy:, wristx:wristx+delta]
            cropimage = img[  wristy-delta:wristy+ldelta,   wristx-ldelta:wristx+delta+ldelta]

            cv2.imshow(str(i)+".png", cropimage)
            cv2.waitKey(1)
    cv2.destroyAllWindows()
    if os.path.isdir(path_to_video_files + folder):
        input("Press Enter to continue...")
