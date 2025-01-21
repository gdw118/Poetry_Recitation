from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import streamlit as st

# 指定 Chromedriver 路径
chromedriver_path = r"D:\Program\ChromeDriver\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chromedriver_path)

chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置无头模式
chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速
chrome_options.add_argument("window-size=1200x600")  # 指定窗口尺寸

# 创建 WebDriver 实例
driver = webdriver.Chrome(options=chrome_options, service=service)


# 登录网站
def crawl_search(title, author):
    try:
        driver.get("https://www.gushiwen.cn/")
        # 定位到搜索框
        search_box = driver.find_element(By.ID, "txtKey")
        # 输入搜索内容
        search_box.send_keys(title + " " + author)
        # 模拟回车键提交搜索
        search_box.send_keys(Keys.RETURN)

        # 使用XPath定位到具有特定style的textarea
        textarea = driver.find_element(By.XPATH, '//textarea[contains(@style, "background-color:#F0EFE2;")]')
        # 获取textarea中的文本内容
        textarea_content = textarea.get_attribute('value')

        driver.quit()

        return textarea_content

    except Exception as e:
        st.error(e)


if __name__ == '__main__':
    crawl_search("赠汪伦", "李白")
