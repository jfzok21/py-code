def d_to_h(d):
    if d == 0:
        return '0'
    
    h_chars = "0123456789ABCDEF"
    h_result = ""

    while d > 0:
        remainder = d % 16
        h_result = h_chars[remainder] + h_result
        d //= 16

    return h_result
    
num = int(input())
print(d_to_h(num))