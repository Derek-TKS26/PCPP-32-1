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

    # for row in reader:
    #     print(','.join(row)) # 用join 函数把列表中的字符元素通过符号连起来

    names = ['Name', 'Phone','age'] #定义表头的不同名字
    reader = csv.DictReader(csvfile,fieldnames=names) # DirectReader 直接把第一行作为表头，第一个参数是文件的名字而第二个参数则是标头
    for row in reader:
        print(row['Name'],row['Phone'],row['age']) #打印不同表头下的数据


#—————————————————— Writing data from csv document ————————————————————

with open('new_contacts.csv','w',newline='') as csv_new:
    writer = csv.writer(csv_new,delimiter=',',quotechar='?')
    writer.writerow(names)
    writer.writerow(['mother', '222-555-101']) #写入数据的行。
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105']) # 如果不用？则默认带有Comma 的项会被特殊引用

    fieldnames = names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # 和上面的DirectReader 一样，DirectWriter 也需要输入两个参数：文件名和表头行




