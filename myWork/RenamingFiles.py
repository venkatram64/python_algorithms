
import os, sys

import random



# listing directories
print("The dir is: %s" % os.listdir(os.getcwd()))

temp = os.listdir(os.getcwd()) #being in parent directory
for i in range(len(temp)):
    if temp[i] == '2021':
        os.rename('2021', 'year=2021') #renaming the directory

os.chdir('year=2021')  #cd into new directory
print("dirs in 2021 are:{}", format(os.listdir(os.getcwd())))
month_list = os.listdir(os.getcwd())

for m in month_list:
    print("dirs in 2021 are:{}".format(os.listdir(os.getcwd())))
    m1 = 'month=' + str(m)
    os.rename(m, m1)  #renaming the directory
    os.chdir(m1)   #cd into new directory
    date_list = os.listdir(os.getcwd())
    for d in date_list:
        d1 = "date=" + str(d)
        os.rename(d, d1)  #renaming the directory

    print("dirs in 2021 are :{}".format(os.listdir(os.getcwd)))
    os.chdir('../')