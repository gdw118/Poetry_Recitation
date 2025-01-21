from utils.save_to_csv import save_to_csv


def split_res(text):
    # 分割出诗文和剩余部分
    parts = text.split("——")
    poem_content = parts[0]
    remaining = parts[1]

    # 分割出作者信息和网址
    author_info, details_url = remaining.rsplit('》', 1)

    author_dynasty, author_remaining = author_info.split('·')
    author_name, poem_title = author_remaining.split('《')

    save_to_csv(poem_title, author_dynasty, author_name, poem_content, details_url)


if __name__ == '__main__':
    example_text = "李白乘舟将欲行，忽闻岸上踏歌声。桃花潭水深千尺，不及汪伦送我情。——唐代·李白《赠汪伦》https://so.gushiwen.cn/shiwenv_ca9eaf40a6ce.aspx"
    split_res(example_text)
