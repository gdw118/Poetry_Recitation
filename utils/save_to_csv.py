import csv
import constant


def is_csv_empty(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            # 尝试读取第一行
            first_line = file.readline()
            if not first_line:
                return True  # 文件是空的
            else:
                return False  # 文件不为空
    except FileNotFoundError:
        return True  # 文件不存在，视为“空”


def is_poem_repeated(file_path, title, name):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过表头
        for row in reader:
            # title在第一列, name在第三列
            if title == row[0] and name == row[2]:
                return True

    return False


def save_to_csv(poem_title, author_dynasty, author_name, poem_content, details_url):
    # 数据组织成列表
    data = [poem_title, author_dynasty, author_name, poem_content, details_url]

    # 写入 CSV 文件
    # 如果文件是空的，就写入头部信息
    if is_csv_empty(constant.file_path111):
        with open(constant.file_path111, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['诗歌标题', '朝代', '诗人', '诗歌内容', '解析'])
    # 如果文件中没有重复的数据项，就写入数据
    if not is_poem_repeated(constant.file_path111, poem_title, author_name):
        with open(constant.file_path111, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)


if __name__ == '__main__':
    save_to_csv('赠汪伦', '唐代', '李白', '李白乘舟将欲行，忽闻岸上踏歌声。桃花潭水深千尺，不及汪伦送我情。',
                'https://so.gushiwen.cn/shiwenv_ca9eaf40a6ce.aspx')
