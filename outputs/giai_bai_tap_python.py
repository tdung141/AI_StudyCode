def ma_hoa(van_ban, bang_ma):
    return ''.join(bang_ma.get(char, char) for char in van_ban)

def giai_ma(van_ban_ma, bang_ma):
    nguoc_bang_ma = {v: k for k, v in bang_ma.items()}
    return ''.join(nguoc_bang_ma.get(char, char) for char in van_ban_ma)

# Ví dụ sử dụng
bang_ma = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}
van_ban = 'abcde'
van_ban_ma = ma_hoa(van_ban, bang_ma)
print('Văn bản mã hóa:', van_ban_ma)
van_ban_giai_ma = giai_ma(van_ban_ma, bang_ma)
print('Văn bản giải mã:', van_ban_giai_ma)