

with open('code.txt', 'r') as file:
    with open('code2.txt', 'w') as write:
        for i in file:
            a = len(i)
            b = list(i)
            al = a - 1
            print(b, a, al)
            print(b[al])
            for t in range(0, a):
                if b[t] == 'H':
                    txt = 'h'
                elif b[t] == 'E':
                    txt = 'e'
                elif b[t] == 'L':
                    txt = 'l'
                elif b[t] == 'O':
                    txt = 'o'
                elif b[t] == '_':
                    txt = ' '
                elif b[t] == 'W':
                    txt = 'w'
                elif b[t] == 'R':
                    txt = 'r'
                elif b[t] == 'D':
                    txt = 'd'
                write.write(txt)