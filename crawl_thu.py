from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd

# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path="D:/SONG/CODE/chromedriver/chromedriver.exe")

#2. Mo thu 1 trang web
url = 'https://www.thantai.net/so-ket-qua'
browser.get(url)

# 3. Dien ngay vao o ngay
end = browser.find_element_by_id("end")
end.clear()
end.send_keys("04-04-2020") 




   