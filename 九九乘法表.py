path = "九九乘法表.txt"
with open(path, 'w') as f:
    for b in range(2, 10):
        f.write(f'{b}        |')
    f.write("\n")
    f.write("".join(["-" * 9 + "|" for _ in range(2, 10)]))
    f.write("\n")

    for a in range(2, 10):
        for b in range(2, 10):
            f.write(f' {b}x{a}={a * b:<2}  |')
        f.write("\n")