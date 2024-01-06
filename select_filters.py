from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

def select_filters(filter_option, filter_cat_value):
    filter_dropdown = "//div[contains(@class,'product-filters')]//div[contains(@class,'filters')]//legend[contains(text(),'{{filter_name}}')]//following-sibling::tmo-icon//mat-icon"
    filter_category_checkbox = "//span[contains(text(),'{{filter_category_value}}')]//parent::span[contains(@class,'mat-checkbox')]//preceding-sibling::span[contains(@class,'mat-checkbox-inner-container')]"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.t-mobile.com/tablets")
    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(),"Tablets")]')))
    
    title = driver.title
    print(title)
    for filter_op in filter_option:
        filter_dropdown = filter_dropdown.replace("{{filter_name}}", filter_op)
        print(filter_dropdown)
        filter_dropdown_element = driver.find_element(By.XPATH, filter_dropdown)
        filter_dropdown_element.click()

    for filter_cat in filter_cat_value:
        filter_category_checkbox = filter_category_checkbox.replace("{{filter_category_value}}", filter_cat)
        wait.until(EC.visibility_of_element_located((By.XPATH, filter_category_checkbox)))
        filter_category_checkbox_element = driver.find_element(By.XPATH, filter_category_checkbox)
        filter_category_checkbox_element.click()
    
    time.sleep(5)

select_filters(["Deals","Brands"], ["New","Apple","TCL"])
