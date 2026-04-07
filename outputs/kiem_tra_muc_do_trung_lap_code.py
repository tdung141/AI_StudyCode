import os
import difflib


def get_code_files(directory):
    code_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                code_files.append(os.path.join(root, file))
    return code_files


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def calculate_similarity(code1, code2):
    seq = difflib.SequenceMatcher(None, code1, code2)
    return seq.ratio() * 100


def compare_code_directories(dir1, dir2):
    files1 = get_code_files(dir1)
    files2 = get_code_files(dir2)
    total_similarity = 0
    count = 0

    for file1 in files1:
        for file2 in files2:
            code1 = read_file(file1)
            code2 = read_file(file2)
            similarity = calculate_similarity(code1, code2)
            total_similarity += similarity
            count += 1
            print(f'Trung lap giua {file1} va {file2}: {similarity:.2f}%')

    if count > 0:
        average_similarity = total_similarity / count
        print(f'Trung lap trung binh: {average_similarity:.2f}%')
    else:
        print('Khong co file de so sanh.')


# Vi du su dung
# compare_code_directories('duong_dan_thu_muc_1', 'duong_dan_thu_muc_2')