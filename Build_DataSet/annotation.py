import pandas as pd
import numpy as np

type = "train_valid"
root = "D:/keras-retinanet/size_256/"
filename ="bbox_metadata_"+type+".csv"

df =pd.read_csv(root+filename)
dir_part = "/train/"

file_name_list= []

for i in range(0,df.shape[0]):
    dff  = df.loc[i][0][len("D:/keras-retinanet/train/"):-len(".jpg")]
    b1 = df.loc[i][1]
    b2 = df.loc[i][2]
    b3 = df.loc[i][3]
    b4 = df.loc[i][4]
    Class = df.loc[i][5]

    file_name_list.append([dff,b1,b2,b3,b4,Class])

print(file_name_list)
pd.DataFrame(file_name_list,columns=["file","b1","b2","b3","b4","class"]).to_csv("D:/keras-retinanet/new-meta/check_"+type+".csv")

