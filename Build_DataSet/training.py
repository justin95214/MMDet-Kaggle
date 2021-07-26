import numpy as np
import pandas as pd
import os
import cv2
import sys


#train/ test 경로의 이미지를 로드해서 txt로 변경
#한줄 당 이미지이름만 툭! 확장자도 제거
type = "train"
type1 = "val"
root = "D:/keras-retinanet"
path = root +'/'+type+'/'

file_list = os.listdir(path)
file_list_img = [file[:-len('.jpg')] for file in file_list]

f = open(root+'/new-meta/'+type+'.txt', 'w')
f1 = open(root+'/new-meta/'+type1+'.txt', 'w')

for idx,i in enumerate(file_list_img):
    if int(len(file_list_img)*0.7) >idx:
        print(i,file=f)
    else:
        print(i, file=f1)

sys.stdout.close()