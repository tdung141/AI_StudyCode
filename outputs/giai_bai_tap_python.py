def save_personal_info():
    name = input('Nhap ten: ')
    age = input('Nhap tuoi: ')
    email = input('Nhap email: ')
    skype = input('Nhap skype: ')
    address = input('Nhap dia chi: ')
    workplace = input('Nhap noi lam viec: ')
    with open('setInfo.txt', 'w') as f:
        f.write(f'Ten: {name}\nTuoi: {age}\nEmail: {email}\nSkype: {skype}\nDia chi: {address}\nNoi lam viec: {workplace}')


def read_personal_info():
    with open('setInfo.txt', 'r') as f:
        content = f.read()
    print(content)


def count_words_in_file():
    with open('demo_file2.txt', 'r') as f:
        text = f.read()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


# Gọi các hàm
save_personal_info()
read_personal_info()
word_count_result = count_words_in_file()
print(word_count_result)