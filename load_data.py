import numpy as np
import csv

# make load list
load_list1 = []
load_list2 = []
load_list3 = []
load_list4 = []
load_list5 = []
load_list6 = []
load_list7 = []
load_list8 = []
load_list9 = []
load_list0 = []

# make time list
time_list = []

# read csv files
def read_csv(row_num, csv_file_path):
    load_list = []
    with open (csv_file_path, newline='') as sample_load:
        reader = csv.reader(sample_load)
        for row in reader:
            try:
                if row_num != 0:
                    load_list.append(int(row[row_num]))
                else:
                    load_list.append((row[row_num]))

            except:
                continue

    if row_num == 0:
        load_list.pop(0)
    
    return load_list

# ---------------------------------------
# return max kw and load_curve 
def load_make(dail_avg, daily_load, load_arr):
    max_kw = 0
    time_slot = 24*4
    extra_load = (dail_avg - daily_load)*1000
    new_load_array = (load_arr+int(extra_load/time_slot))*(4/1000)
    last_load_arr = new_load_array
    max_kw = np.max(new_load_array)

    return [max_kw, last_load_arr]

# add values to list
load_list1 = read_csv(1,"new_load1.csv")
load_list2 = read_csv(1,"new_load2.csv")
load_list3 = read_csv(1,"new_load3.csv")
load_list4 = read_csv(1,"new_load4.csv")
load_list5 = read_csv(1,"new_load5.csv")
load_list6 = read_csv(1,"new_load6.csv")
load_list7 = read_csv(1,"new_load7.csv")
load_list8 = read_csv(1,"new_load8.csv")
load_list9 = read_csv(1,"new_load9.csv")
load_list0 = read_csv(1,"new_load10.csv")

time_list = read_csv(0,"new_load1.csv")

# make load arrays
load_arr1 = np.array(load_list1)
load_arr2 = np.array(load_list2)
load_arr3 = np.array(load_list3)
load_arr4 = np.array(load_list4)
load_arr5 = np.array(load_list5)
load_arr6 = np.array(load_list6)
load_arr7 = np.array(load_list7)
load_arr8 = np.array(load_list8)
load_arr9 = np.array(load_list9)
load_arr0 = np.array(load_list0)

# ----------------------------------------------------------------
# find daily confumption
daily_load1 = (np.sum(load_arr1))/1000
daily_load2 = (np.sum(load_arr2))/1000
daily_load3 = (np.sum(load_arr3))/1000
daily_load4 = (np.sum(load_arr4))/1000
daily_load5 = (np.sum(load_arr5))/1000
daily_load6 = (np.sum(load_arr6))/1000
daily_load7 = (np.sum(load_arr7))/1000
daily_load8 = (np.sum(load_arr8))/1000
daily_load9 = (np.sum(load_arr9))/1000
daily_load0 = (np.sum(load_arr0))/1000

# -------------------------------------------------------------------



house_ind_list = []
house_pole_list = []
house_avg_load = []
with open ('ALL1.csv', newline='') as house_data:
    house_reader = csv.reader(house_data)
    for rw in house_reader:
        if rw[0] != '':
            house_ind_list.append(rw[0])
            house_pole_list.append(rw[2])
            house_avg_load.append(rw[4])


house_ind_list.pop(0)
house_pole_list.pop(0)
house_avg_load.pop(0)


house_avg_load_int = list(map(lambda i:float(i),house_avg_load))

max_kw = {}


for indx in range(len(house_avg_load_int)) :
    dail_avg = house_avg_load_int[indx]

    if dail_avg > daily_load9 :
        rtn_list = load_make(dail_avg, daily_load9, load_arr9)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load8:
        rtn_list = load_make(dail_avg, daily_load8, load_arr8)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load7:
        rtn_list = load_make(dail_avg, daily_load7, load_arr7)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load6:
        rtn_list = load_make(dail_avg, daily_load6, load_arr6)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load5:
        rtn_list = load_make(dail_avg, daily_load5, load_arr5)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load4:
        rtn_list = load_make(dail_avg, daily_load4, load_arr4)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load3:
        rtn_list = load_make(dail_avg, daily_load3, load_arr3)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load2:
        rtn_list = load_make(dail_avg, daily_load2, load_arr2)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    elif  dail_avg > daily_load1:
        rtn_list = load_make(dail_avg, daily_load1, load_arr1)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]
    else :
        rtn_list = load_make(dail_avg, daily_load0, load_arr0)
        max_kw[house_pole_list[indx]] = np.max(rtn_list[0])
        last_load_arr = rtn_list[1]


    name=house_pole_list[indx]+".csv"
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["house", "load"])
        for row_num in range(len(time_list)):
            x = round(last_load_arr[row_num],1)
            writer.writerow([row_num,float(x)])

# count = 0
# for i in max_kw:
#     if max_kw[i] > 0.5:
#         print(i , "  " ,  max_kw[i])
#         count += 1


with open("max_details.csv",'w',newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(["house", "load"])
    for i in max_kw:
        writer.writerow([i, max_kw[i]])
