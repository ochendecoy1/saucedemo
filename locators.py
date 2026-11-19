from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.saucedemo.com/")

# By.ID
print("DEBUG: ищем By.ID -> user-name")
driver.find_element(By.ID, "user-name")
print("DEBUG: ищем By.ID -> password")
driver.find_element(By.ID, "password")
print("DEBUG: ищем By.ID -> login-button")
driver.find_element(By.ID, "login-button")

# By.NAME
print("DEBUG: ищем By.NAME -> user-name")
driver.find_element(By.NAME, "user-name")
print("DEBUG: ищем By.NAME -> password")
driver.find_element(By.NAME, "password")

# By.CLASS_NAME
print("DEBUG: ищем By.CLASS_NAME -> login_logo")
driver.find_element(By.CLASS_NAME, "login_logo")
print("DEBUG: ищем By.CLASS_NAME -> form_group")
driver.find_element(By.CLASS_NAME, "form_group")
print("DEBUG: ищем By.CLASS_NAME -> btn_action")
driver.find_element(By.CLASS_NAME, "btn_action")

# By.TAG_NAME
print("DEBUG: ищем By.TAG_NAME -> form")
driver.find_element(By.TAG_NAME, "form")
print("DEBUG: ищем By.TAG_NAME -> input")
driver.find_element(By.TAG_NAME, "input")

# By.LINK_TEXT и By.PARTIAL_LINK_TEXT на странице логина не нашёл, после авторизации будут


# XPath: поиск по атрибуту
print("DEBUG: ищем XPath -> //input[@placeholder='Username']")
driver.find_element(By.XPATH, "//input[@placeholder='Username']")
print("DEBUG: ищем XPath -> //input[@placeholder='Password']")
driver.find_element(By.XPATH, "//input[@placeholder='Password']")

# XPath: частичное совпадение атрибута
print("DEBUG: ищем XPath -> //input[contains(@placeholder,'User')]")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'User')]")

# XPath оси
print("DEBUG: ищем XPath -> ancestor::form")
driver.find_element(By.XPATH, "//input[@id='user-name']/ancestor::form")
print("DEBUG: ищем XPath -> descendant::input")
driver.find_element(By.XPATH, "//form/descendant::input")
print("DEBUG: ищем XPath -> following::input")
driver.find_element(By.XPATH, "//input[@id='user-name']/following::input")
# parent::div у поля пароля (гарантированно работает)
print("DEBUG: ищем XPath -> parent::div (для password)")
driver.find_element(By.XPATH, "//input[@id='password']/parent::div")
print("DEBUG: ищем XPath -> preceding::input")
driver.find_element(By.XPATH, "//input[@id='password']/preceding::input")

# XPath с условием and
print("DEBUG: ищем XPath -> input[@name='user-name' and @type='text']")
driver.find_element(By.XPATH, "//input[@name='user-name' and @type='text']")

# CSS-селекторы
print("DEBUG: ищем CSS -> .login_logo")
driver.find_element(By.CSS_SELECTOR, ".login_logo")
print("DEBUG: ищем CSS -> .submit-button.btn_action")
driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")
print("DEBUG: ищем CSS -> .login_wrapper .form_group")
driver.find_element(By.CSS_SELECTOR, ".login_wrapper .form_group")
print("DEBUG: ищем CSS -> #user-name")
driver.find_element(By.CSS_SELECTOR, "#user-name")
print("DEBUG: ищем CSS -> input")
driver.find_element(By.CSS_SELECTOR, "input")
print("DEBUG: ищем CSS -> [placeholder='Username']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']")
print("DEBUG: ищем CSS -> [class~='btn_action']")
driver.find_element(By.CSS_SELECTOR, "[class~='btn_action']")
print("DEBUG: ищем CSS -> [lang|=en]")
driver.find_element(By.CSS_SELECTOR, "[lang|=en]")

# [attribute^=value], [attribute$=value], [attribute*=value] — на странице логина подходящих нет.

# После авторизации

print("DEBUG: выполняем авторизацию")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


# By.ID
print("DEBUG: ищем By.ID -> shopping_cart_container")
driver.find_element(By.ID, "shopping_cart_container")

# By.TAG_NAME
print("DEBUG: ищем By.TAG_NAME -> a")
driver.find_element(By.TAG_NAME, "a")

# By.LINK_TEXT
print("DEBUG: ищем By.LINK_TEXT -> Sauce Labs Backpack")
driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")

# By.PARTIAL_LINK_TEXT
print("DEBUG: ищем By.PARTIAL_LINK_TEXT -> Backpack")
driver.find_element(By.PARTIAL_LINK_TEXT, "Backpack")

# XPath: по атрибуту, по тексту, частичное совпадение
print("DEBUG: ищем XPath -> //a[@id='item_4_title_link']")
driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
print("DEBUG: ищем XPath -> //span[text()='Products']")
driver.find_element(By.XPATH, "//span[text()='Products']")
print("DEBUG: ищем XPath -> //button[contains(@data-test,'add-to-cart')]")
driver.find_element(By.XPATH, "//button[contains(@data-test,'add-to-cart')]")
print("DEBUG: ищем XPath -> //div[contains(text(),'Sauce Labs')]")
driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs')]")

# XPath оси на каталоге
print("DEBUG: ищем XPath -> ancestor::div[@class='inventory_item']")
driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/ancestor::div[@class='inventory_item']")
print("DEBUG: ищем XPath -> descendant::button")
driver.find_element(By.XPATH, "//div[@class='inventory_item']/descendant::button")
print("DEBUG: ищем XPath -> following::button")
driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/following::button")
print("DEBUG: ищем XPath -> parent::a")
driver.find_element(By.XPATH, "//div[@data-test='inventory-item-name']/parent::a")
print("DEBUG: ищем XPath -> preceding::div")
driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']/preceding::div")

# CSS-селекторы на каталоге
print("DEBUG: ищем CSS -> div.inventory_item")
driver.find_element(By.CSS_SELECTOR, "div.inventory_item")
print("DEBUG: ищем CSS -> [data-test^='add-to-cart']")
driver.find_element(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
print("DEBUG: ищем CSS -> [id$='_title_link']")
driver.find_element(By.CSS_SELECTOR, "[id$='_title_link']")
print("DEBUG: ищем CSS -> [data-test*='cart']")
driver.find_element(By.CSS_SELECTOR, "[data-test*='cart']")


driver.quit()
print("Все локаторы найдены")
