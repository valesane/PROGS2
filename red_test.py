from selenium import webdriver


driver = webdriver.Chrome('C://chromedriver.exe')
driver.get(' http://127.0.0.1:8000/home')
print(driver.title)


# assert driver.title == 'valesane'