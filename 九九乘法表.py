path = '九九乘法表.txt'
with open(path, 'a') as f:
    for a in range(1,10):
        for b in range(1,10):
            f.write(f'|{b} x {a} = {a*b}|')
        f.write("\n")
print('good')