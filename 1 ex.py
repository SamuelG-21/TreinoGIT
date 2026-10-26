f = open(r'c:/users/Lab0307/Desktop/teste.txt1', 'w')
for linha in range(1,101):
    f.write(f'{linha}\n')
    # alteração
f.close()