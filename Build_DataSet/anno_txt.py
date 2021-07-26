import pandas as pd
import numpy as np
# row 생략 없이 출력
pd.set_option('display.max_rows', None)
# col 생략 없이 출력
pd.set_option('display.max_columns', None)
import sys

type = "train"
root = "D:/keras-retinanet/new-meta/"
filename ="check_"+type+".csv"

df =pd.read_csv(root+filename)



set_file_name = list(set(df["file"]))

row, col = len(set_file_name), 3
arr = [[0]*col for i in range(row)]

for idx,i in enumerate(set_file_name):
    is_file = df['file'] == i
    arr[idx][0] = i
    temp_list =[]
    temp_list.append(0)
    temp_list.append(0)

    for k in range(0,df[is_file].shape[0]):
        #print(df[is_file].iloc[k,2:6])

        for m in range(2,6):
            temp_list.append(np.array(df[is_file].iloc[k,m:m+1])[0])
        arr[idx][1] = np.array(df[is_file]['class'])[0]
    arr[idx][2] = temp_list

    #[idx][2] = df[is_file].iloc[k,7]

print(pd.DataFrame(arr))



root1 = "D:/keras-retinanet/new-meta/label_2/"
for idx,i in enumerate(set_file_name):
    f = open(root1 + arr[idx][0] + '.txt', 'w')
    print(arr[idx][1],str(arr[idx][2]).replace("[","").replace("]",""),file=f)

sys.stdout.close()
