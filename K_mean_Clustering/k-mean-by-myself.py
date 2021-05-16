from random import random
import math 
import numpy as np

n = input("Nhập n = ")

list_point = []
for i in range(int(n)):
    list_point.append([random(),random()])

print(list_point)

list_k_mean = [[0.1,0.1] , [0.2, 0.2] , [0.3 , 0.3] , [0.4 , 0.4] , [0.5, 0.5] , [0.6, 0.6] , [0.7, 0.7] , 
                [0.8 , 0.8] , [0.9 , 0.9] , [1 , 1] ]

print(len(list_k_mean))

list_save_k_mean = []

# print(list_point[0]) # in ra vị trí list số thứ nhất
# print(list_point[0][1]) # in ra vị trí thứ 2 của số thứ nhất 

for i in range(int(n)):
    list_temp_min = []
    for j in range(len(list_k_mean)):
        distance = math.sqrt(pow(list_k_mean[j][0] - list_point[i][0],2) + pow(list_k_mean[j][1] - list_point[i][1],2))
        list_temp_min.append(distance)
    min_of_list = min(list_temp_min)
    for location_min in range(len(list_temp_min)):
        if list_temp_min[location_min] == min_of_list : 
            list_save_k_mean.append(location_min)

print(list_save_k_mean)

list_k_0 = []
list_k_1 = []
list_k_2 = []
list_k_3 = []
list_k_4 = []
list_k_5 = []
list_k_6 = []
list_k_7 = []
list_k_8 = []
list_k_9 = []

# phân cụm dữ liệu 
for i in range(len(list_point)):
    if list_save_k_mean[i] == 0 :
        list_k_0.append(list_point[i])
    elif list_save_k_mean[i] == 1 :
        list_k_1.append(list_point[i])
    elif list_save_k_mean[i] == 2 :
        list_k_2.append(list_point[i])
    elif list_save_k_mean[i] == 3 :
        list_k_3.append(list_point[i])
    elif list_save_k_mean[i] == 4 :
        list_k_4.append(list_point[i])
    elif list_save_k_mean[i] == 5 :
        list_point.append(list_point[i])
    elif list_save_k_mean[i] == 6 :
        list_point.append(list_point[i])
    elif list_save_k_mean[i] == 7 :
        list_point.append(list_point[i])
    elif list_save_k_mean[i] == 8 :
        list_point.append(list_point[i])
    elif list_save_k_mean[i] == 9 :
        list_point.append(list_point[i])

print(list_k_0)
print(list_k_1)
print(list_k_2)
print(list_k_3)
print(list_k_4)
print(list_k_5)
print(list_k_6)
print(list_k_7)
print(list_k_8)
print(list_k_9)

# vị trí trung bình của 9 cụm lần 1 : 
if len(list_k_0) > 0 : print(np.mean(list_k_0))
if len(list_k_1) > 0 : print(np.mean(list_k_1))
if len(list_k_2) > 0 : print(np.mean(list_k_2))
if len(list_k_3) > 0 : print(np.mean(list_k_3))
if len(list_k_4) > 0 : print(np.mean(list_k_4))
if len(list_k_5) > 0 : print(np.mean(list_k_5))
if len(list_k_6) > 0 : print(np.mean(list_k_6))
if len(list_k_7) > 0 : print(np.mean(list_k_7))
if len(list_k_8) > 0 : print(np.mean(list_k_8))
if len(list_k_9) > 0 : print(np.mean(list_k_9))

# tính cho 1 cụm :

while(True): 
    for i in range(len(list_k_2)):
        distance = math.sqrt(pow(list_k_mean[j][0] - list_point[i][0],2) + pow(list_k_mean[j][1] - list_point[i][1],2))

    



