from selenium import webdriver
import time

# 启动 Edge 浏览器
driver = webdriver.Edge()

# 打开百度首页
driver.get('https://www.baidu.com')

# 等待页面加载，确保元素可被定位（可根据实际情况调整等待时间）
time.sleep(2)

# 定位到搜索框元素，并输入"北京天气"
driver.find_element_by_id('kw').send_keys('北京天气')

# 定位到搜索按钮并点击
driver.find_element_by_id('su').click()

# 等待搜索结果页面加载（可根据实际情况调整等待时间）
time.sleep(2)

# 关闭浏览器
driver.quit()