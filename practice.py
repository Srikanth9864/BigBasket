
from selenium import webdriver
from time import sleep
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.bigbasket.com/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# element = driver.find_element("xpath","//a[@class = 'dropdown-toggle meganav-shop']")
# a = ActionChains(driver)
# a.move_to_element(element).perform()
# element2 = driver.find_element("xpath","(//a[text() = 'Organic Fruits & Vegetables'])[2]")
# a.move_to_element(element2).perform()
# driver.find_element("xpath","(//a[text()='Organic Vegetables'])[3]").click()
# def brand_ckbx(item_name):
#     driver.find_element("xpath",f"(//span[text() = 'Brand'])[1]/../..//span[text() = '{item_name}']").click()
# items = ['Gopalan Organic', 'Fresho','Organic']
# for item in items:
#     brand_ckbx(item)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
driver.implicitly_wait(5)
elements = driver.find_elements("xpath","//div[@qa='product_name']|//div[@qa='product_name']/../..//span[@class='discnt-price']")
price = driver.find_element("xpath","//div[@qa='product_name']/../..//span[@class = 'discnt-price']")
for element in elements:
    if price.text=="17.50":
        print(element.text)

driver.close()













# def prime(start,end):
#     for num in range(start,end + 1):
#         if num > 1:
#             for i in range(2,num):
#                 if (num%i)==0 :
#                     break
#             else:
#                 print(num)

# p = prime(20,70)

# def fibonacii(num,n):
#     a = 0
#     b = 1
#     res = []
#     for _ in range(0,n):
#         _sum = a+b
#         a = b
#         b = _sum
#         res.append(_sum)
#         if num in res:
#             return True
#         else:
#             return False
        
    



