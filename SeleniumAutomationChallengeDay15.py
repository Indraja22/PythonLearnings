from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests as req


class SeleniumAutomationChallengeDay15:
     
    def test(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        response = req.get("https://randomuser.me/api/",timeout=60)
        # print(response.status_code)
        # print(response.json())
        resp_d = response.json()
        resp_dict = dict(resp_d)
        
        print(resp_dict['results'])
        gender = resp_dict['results'][0]['gender']
        gender_str = str(gender).capitalize()
        print(gender_str)
        first_name = resp_dict['results'][0]['name']['first']
        print(first_name)
        last_name = resp_dict['results'][0]['name']['last']
        print(last_name)
        phone = resp_dict['results'][0]['phone']
        print(phone)
        country = resp_dict['results'][0]['location']['country']
        print(country)
        city = resp_dict['results'][0]['location']['city']
        print(city)
        email = resp_dict['results'][0]['email']
        print(email)
        driver.find_element(By.XPATH, "//label[text()='First Name']//following-sibling::input").send_keys(first_name)
        driver.find_element(By.XPATH, "//label[text()='Last Name']//following-sibling::input").send_keys(last_name)
        driver.find_element(By.XPATH, "//label[text()='Phone']//following-sibling::input").send_keys(phone)
        driver.find_element(By.XPATH, "//label[text()='Country']//following-sibling::input").send_keys(country)
        driver.find_element(By.XPATH, "//label[text()='City']//following-sibling::input").send_keys(city)
        driver.find_element(By.XPATH, "//label[text()='Email Address']//following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH,f"//span[text()='Gender']//following-sibling::table//label[text()='{gender_str}']").click()
        driver.find_element(By.XPATH,"//label[text()='Friday']").click()
        best_time_to_contact = driver.find_element(By.XPATH,"//label[text()='Best Time to Contact']//following-sibling::select")
        select = Select(best_time_to_contact)
        select.select_by_visible_text('Morning')
        driver.find_element(By.ID,"FSsubmit").click()
        driver.quit()

sele = SeleniumAutomationChallengeDay15()
sele.test()
