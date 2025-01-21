import csv
import constant


def save_correct_rate(correct_num, time, correct_rate):
    data = [correct_num, time, correct_rate]
    # 写入 CSV 文件
    with open(constant.file_path222, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
