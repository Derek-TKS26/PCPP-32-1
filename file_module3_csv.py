#The CSV (Comma Separated Values) format is one of the most popular file formats used to store and transfer data between different programs.
# Currently, many database management tools and the popular Excel offer data import and export in this format.
# 可以用很多种不同的分隔符来分割csv文件中的不同数据，但是同一个文件至可以用一种。


# python 中用于处理csv文件的包叫做 csv
# 读取文件的信息通过 reader 对象来实现，reader 是可迭代对象
# 写入文件的信息通过 writer 对象来实现



#—————————————————— Reading data from csv document ————————————————————
import csv

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    # newline='' argument is not absolutely indispensable,
    # but it's good practice when working with CSV files in Python.

    for row in reader:
        print(','.join(row)) # 用join 函数把列表中的字符元素通过符号连起来