import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print("I am in the file")
for product in products:
        product_name = product.find_element(By.XPATH,"div/h4/a").text
        print(product_name)
        if product_name == "Blackberry":
            print("I am here")
            product.find_element(By.XPATH,"div/button").click()

print("Update for Repository_25")
print("Second commit on Repository_25")
print("This change made in GitStart to be transferred to Repository_25")

print("Made changes in branch developer")
time.sleep(2)

driver.close()