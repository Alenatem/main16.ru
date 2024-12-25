from selenium import webdriver
from selenium.webdriver import Keys
#from time import sleep
import datetime
from selenium.webdriver.common.by import By
file = open("log.txt", "w")

#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

 #функции

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    file.write("Success write login\n")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    file.write("Success write password\n")

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()
    file.write("Success click enter\n")

def login_enter():
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    file.write("Success write login\n")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    file.write("Success write password\n")

    password.send_keys(Keys.ENTER)
    file.write("Success enter login\n")


def fake_login():
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    file.write("Success write login\n")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce22")
    file.write("Success write fake password\n")

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()
    file.write("Success click enter\n")
def refresh_page():
    driver.refresh()
#конец функций
#
def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")

def test_context_after_login_is_correct():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    driver.save_screenshot(f"sc_real_login\\screenshot_test_context_after_login_is_correct_{datetime.datetime.now().date()}.png")

    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK\n")

def test_fake_login_label():
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    assert correct_text == current_text.text, "test_fake_login_label is Failed"
    file.write("test_fake_login_label is ok\n")

def sc_real_login():
    set_up()
    login()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_real_login_enter():
    set_up()
    login_enter()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_fake_login():
    set_up()
    fake_login()
    test_fake_login_label()

sc_real_login_enter()
file.close()
#driver.quit()