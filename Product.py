from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

'''Checking and Verifying the Each Element of a Particular Product '''


'''open the browser'''
driver = webdriver.Chrome(ChromeDriverManager().install())

'''Enter the URL'''
driver.get("https://www.bigbasket.com/")

'''maximize window'''
driver.maximize_window()

'''Matching the speed with selenium'''
driver.implicitly_wait(5)

''' Move to shop by category dropdown link'''
element = driver.find_element("xpath","//a[@class = 'dropdown-toggle meganav-shop']")

'''Using Actions class to mouse hover'''
a = ActionChains(driver)
a.move_to_element(element).perform()

''' Click on Organic Fruits & Vegetables link'''
element2 = driver.find_element("xpath","(//a[text() = 'Organic Fruits & Vegetables'])[2]")
a.move_to_element(element2).perform()

'''Click on Organic Fruits link'''
driver.find_element("xpath","(//a[text()='Organic Fruits'])[2]").click()

'''Verifying that product has a image or not '''
image = driver.find_element("xpath","(//img[@class = 'img-responsive blur-up lazyautosizes lazyloaded'])[1]")

'''Verifying that product has name label or not '''
label = driver.find_element("xpath","//a[text() = 'Banana - Yelakki, Organically Grown']")

'''Verifying that product has drop-down toggle to display different prices according to weight'''
drp_dwn = driver.find_element("xpath","(//button[@class = 'btn btn-default dropdown-toggle form-control'])[1]")

'''Verifying the price tag for that particular product'''
price = driver.find_element("xpath","(//span[@class = 'discnt-price'])[1]")

'''Checking that product is available for discount''' 
discount  = driver.find_element("xpath","(//div[@class = 'save-price ng-scope'])[1]")

''' Verifying that product has quantity box to change the quantity'''
qty = driver.find_element("xpath","(//div[@class='input-group'] //span[text()='Qty'])[1]")

'''Verifying the product has "add to cart" option or not'''
add_button = driver.find_element("xpath","(//span[@class = 'input-group-addon'])[1]")

'''Storing all the variables in a tuple'''   
var_list = (image, label, drp_dwn, price, discount, qty, add_button)

'''iterating over every variable and checking the element is displayed or not '''
for var in var_list:
    if isinstance(var,WebElement):                                                                                                  
        if var.is_displayed()==True:
            print("Pass")
        else:
            print("Fail")


'''Closing the browser'''
driver.close()





