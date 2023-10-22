import os
text = ''

with open('code.txt', 'r') as file:
    with open('test.py', 'w') as write:
        for i in file:
            a = len(i)
            b = list(i)
            al = a - 1
            print(b, a, al)
            print(b[al])
            for t in range(0, a):

                write.write(b[t])


# os.system('python test.py')

# os.system('del test.py')

