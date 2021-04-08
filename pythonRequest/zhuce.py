from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://list.duia.com/8")
sleep(1)
driver.maximize_window()
sleep(1)
#点击注册
driver.find_element_by_css_selector("#course > div:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > div:nth-child(4)").click()
sleep(2)
#handle=driver.current_window_handle
#print(handle)  ##获取当前句柄并打印
handles=driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element_by_css_selector("div.c_info_buyBtn:nth-child(1)").click()
#例如：获取所有句柄：handles=driver.window_handles
#切换至第一个窗口：driver.switch_to.window(handles[0])
#切换至第二个窗口：driver.switch_to.window(handles[1]).



