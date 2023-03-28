# read load.csv file
# read all.csv file
#   find avarage consumption data


import csv
import numpy as np

#  ------------------------------------------------------------------------------------------------
load_list1 = []


time_list = []


with open ('Copy of AZ0228 Load Profile Data.xlsx - Sheet2.csv', newline='') as sample_load:
    reader = csv.reader(sample_load)
    for row in reader:
        load_list1.append(row[1])
        time_list.append(row[0])

house_ind_list = []
house_pole_list = []
house_avg_load = []

with open ('ALL1.csv', newline='') as house_data:
    house_reader = csv.reader(house_data)
    for rw in house_reader:
        if rw[0] != '':
            house_ind_list.append(rw[0])
            house_pole_list.append(rw[1])
            house_avg_load.append(rw[3])


house_ind_list.pop(0)
house_pole_list.pop(0)
load_list1.pop(0)
time_list.pop(0)
house_avg_load.pop(0)
# -----------------------------------------------------------------------------------------------------------

def extra_load_make(extra_load, time_slot ):
    pass




# -----------------------------------------------------------------------------------------------------------


house_avg_load_int = list(map(lambda i:int(i),house_avg_load))





# convert int to load_list valus
load_list_int = list(map(lambda i:int(i),load_list1))
load_arr = np.array(load_list_int)

daily_load = (np.sum(load_arr))/1000

time_slot = 24*4
count = 0
max_kw = {}
for indx in range(len(house_avg_load_int)) :
    dail_avg = house_avg_load_int[indx]
    if dail_avg > daily_load :
        extra_load = (dail_avg - daily_load)*1000
        new_load_array = (load_arr+int(extra_load/time_slot))*(4/1000)
        last_load_arr = new_load_array/np.max(new_load_array)
        max_kw[house_ind_list[indx]] = np.max(new_load_array)
    else:
        last_load_arr = load_arr/np.max(load_arr)
        max_kw[house_ind_list[indx]] = np.max(load_arr)*(4/1000)


# print(load_arr)
# print(new_load_array)
# print(np.sum(new_load_array))

    name=house_ind_list[indx]+".csv"
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["house", "load"])
        for row_num in range(len(time_list)):
            writer.writerow([time_list[row_num],last_load_arr[row_num]])

    count += 1

print(count)
print(len(house_avg_load_int))
for i in max_kw:

    if i == "105889707" :
        print(i , "  " ,  max_kw[i])

print(len(max_kw))