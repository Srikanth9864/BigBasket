from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
driver.implicitly_wait(5)
element = driver.find_element("xpath","//a[@class = 'dropdown-toggle meganav-shop']")
a = ActionChains(driver)
a.move_to_element(element).perform()
element2 = driver.find_element("xpath","(//a[text() = 'Organic Fruits & Vegetables'])[2]")
a.move_to_element(element2).perform()
sleep(2)
driver.find_element("xpath","(//a[text()='Organic Vegetables'])[3]").click()
driver.find_element("xpath","//a[text()='Chilli - Green, Organically Grown (Loose)']").click()
driver.find_element("xpath","//span[text()='ADD TO BASKET']").click()
driver.close()
















































