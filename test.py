from selenium import webdriver
import time

# driver = webdriver.Chrome(executable_path="C:\\Users\\aseld\\LentaParser\\yandexdriver")

options = webdriver.ChromeOptions()

binary_yandex_driver_file = 'C:\\Users\\aseld\\LentaParser\\yandexdriver\\yandexdriver.exe' # path to YandexDriver

driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
driver.get('https://2ip.ru')
time.sleep(15)
driver.quit()