# Poetry_Recitation
一个诗词背诵demo，利用爬虫技术从古诗文网获取诗词数据，并通过数据分析和可视化功能，帮助学生记忆古诗词。

## 功能简介
- **诗词搜索与录入**  
  使用 Selenium 爬虫技术模拟浏览器行为，从 [古诗文网](https://www.gushiwen.cn/) 爬取诗词数据，支持精准的诗词搜索。
  
- **诗词背诵**  
  使用 `Jieba` 分词、`Pandas` 数据分析等工具处理爬取的诗词数据，随机生成填空题目，用户可以根据提示填空进行诗词背诵练习。

- **作答结果记录与可视化**  
  自动记录用户作答的正确率，使用 `Matplotlib` 绘制用户作答正确率变化趋势图，直观展示用户的学习进展。

- **易用的交互界面**  
  基于 Streamlit 框架构建简洁的网页应用，支持多功能切换。

## 安装与运行

### 环境依赖
确保你的环境安装了以下工具和库：
- Python >= 3.7
- Selenium
- Jieba
- Pandas
- Matplotlib
- Streamlit

### 安装步骤
1. 克隆仓库到本地：
   ```
   git clone https://github.com/gdw118/EnjoyPoetry.git
   cd EnjoyPoetry
   ```
2. 安装依赖库

3. 启动应用：
   ```streamlit run app.py```
