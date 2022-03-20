from selenium.webdriver.support.ui import WebDriverWait
import time
 
link = ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

def test_should_button_add_basket(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    btn_basket = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    # Проверка что кнопка находится, и одна одна, запускать с pytest -s --language=** test_items.py
    print(" КОЛ-ВО НАЙДЕННЫХ ЭЛЕМЕНТОВ = " + str(btn_basket))
    # Можно увеличить длительсноть показа старницы
    time.sleep(5)
    assert btn_basket != 0, "НЕТ КНОПКИ ДОБАВИТЬ В КОРЗИНУ!"
    