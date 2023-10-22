import os
text = ''

with open('code.txt', 'r') as file:
    with open('test.py', 'w') as write:
        for i in file:
            write.write(i)
os.system('python test.py')
os.system('del test.py')