from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
driver.implicitly_wait(5)
element = driver.find_element("xpath","//a[@class = 'dropdown-toggle meganav-shop']")
a = ActionChains(driver)
a.move_to_element(element).perform()
element2 = driver.find_element("xpath","(//a[text() = 'Organic Fruits & Vegetables'])[2]")
b = ActionChains(driver)
b.move_to_element(element2).perform()
driver.find_element("xpath","(//a[text()='Organic Fruits'])[2]").click()
driver.find_element("xpath","//a[text()='Banana - Yelakki, Organically Grown']").click()
driver.find_element("xpath","//span[text()='ADD TO BASKET']").click()
driver.close()
