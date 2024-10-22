def write_diary():
    file_name = 'diary.txt'
    f = open(file_name, 'a')
    date = input('Please enter the date of your diary: ')
    text = input('Please enter the text of your diary: ')
    f.write('$$$$\n') # page breaker icon
    f.write(date + '\n')
    f.write(text + '\n')

    f.close()
    return True


def read_diary(date = '-1'):
    file_name = 'diary.txt'
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    if date != '-1':
        list1 = content.split('$$$$\n')
        for i in list1:
            if i.strip()[:len(date)] == date:
                print(i)
                return True
        return False
    else:
        list1 = content.split('$$$$\n')
        for i in list1:
            print(i.strip())
        return True

def quit():
    print('Welcome to use the system next time!')

def menu():

    while True:
        print('*' * 50)
        print('''1.Write a diary;\n2.Read a diary;\n3.Exit the diary book.''')
        print('*' * 50)
        op = input('Please enter your option: ')

        if op == '1':
            write_diary()

            if True:
                print('The new dairy has been written into the diary book.')
            else:
                print('Please write your diary.')

        elif op == '2':
            date = input('Please enter the date of you want to review (-1 for reviewing all dairies): ')
            read_diary(date)
            if read_diary(date):
                print('The diary has been loaded.')
            else:
                print('The content has not been founded.')


        elif op == '3':
            quit()
            break

        else:
            print('Your entry is invalid, please make it again.')

menu()