from selenium.webdriver.common.by import By


def test_cart(browser):

    print("Открываем страницу")
    browser.get("https://www.saucedemo.com/")

    print("[STEP] Вводим логин и пароль")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Получаем данные товара ДО добавления
    print("Читаем название и цену товара на странице каталога")
    name_on_page = browser.find_element(By.CSS_SELECTOR, "div.inventory_item_name").text
    price_on_page = browser.find_element(By.CSS_SELECTOR, "div.inventory_item_price").text
    print(f"Товар: '{name_on_page}', цена: '{price_on_page}'")

    # Добавляем в корзину
    print("Добавляем товар в корзину")
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    #Переход в корзину
    print("Переходим в корзину")
    browser.find_element(By.ID, "shopping_cart_container").click()

    # Получаем данные из корзины
    print("Читаем название и цену из корзины")
    name_in_cart = browser.find_element(By.CSS_SELECTOR, "div.inventory_item_name").text
    price_in_cart = browser.find_element(By.CSS_SELECTOR, "div.inventory_item_price").text
    print(f"В корзине: товар '{name_in_cart}', цена '{price_in_cart}'")

    #Проверки (assert)
    print("Сравниваем названия")
    assert name_in_cart == name_on_page, (
        f"Не совпало название. В корзине: '{name_in_cart}', на странице: '{name_on_page}'"
    )
    print("Названия совпали")


    assert price_in_cart == price_on_page, (
        f"Цена не совпала. В корзине: '{price_in_cart}', на странице: '{price_on_page}'"
    )
    print("Цены совпали")

