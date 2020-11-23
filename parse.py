import pandas as pd

col_list= ['Frames#', 'rightWrist_x', 'rightWrist_y']
df = pd.read_csv("key_points.csv", usecols=col_list)

print( df.shape[0])

col_count = df.shape[0]
for i in range(col_count):
    print("image #", df['Frames#'][i], int(df['rightWrist_x'][i]), int(df['rightWrist_y'][i]) )