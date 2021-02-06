import sys
sys.path.append('..')
from pages.page_header import PageHeader
from pages.functions import header_assertions
import inspect
# pytest -v --driver Chrome --driver-path C:/Windows/chromedriver.exe test_page_header.py


# тестирование Заголовка страницы (Корзина, Избранное, Ссылки на группы товаров, Лого)
def test_about(selenium):
    page = PageHeader(selenium)
    page.about.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]   # получаем имя текущей функции без 'test_'
    header_assertions(test_obj, curr_page)


def test_dostavka(selenium):
    page = PageHeader(selenium)
    page.dostavka.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_garantii(selenium):
    page = PageHeader(selenium)
    page.garantii.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_chat(selenium):
    page = PageHeader(selenium)
    tmall = selenium.current_window_handle
    page.chat.click()
    page.wait_page_loaded()
    new_window = [w for w in selenium.window_handles if w != tmall]
    selenium.switch_to.window(new_window[0])
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
    selenium.close()
    selenium.switch_to.window(tmall)


def test_basket(selenium):
    page = PageHeader(selenium)
    page.authorization(selenium)
    page.basket.click()   # переход в Корзину покупок
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_favorite(selenium):
    page = PageHeader(selenium)
    page.authorization(selenium)
    page.favorite.click()   # переход в Избранное
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_elektonika(selenium):
    page = PageHeader(selenium)
    page.electronics.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_texnika(selenium):
    page = PageHeader(selenium)
    page.texnika.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_domsad(selenium):
    page = PageHeader(selenium)
    page.domsad.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_mama(selenium):
    page = PageHeader(selenium)
    page.mama.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_moda(selenium):
    page = PageHeader(selenium)
    page.moda.click()
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)


def test_logo(selenium):
    page = PageHeader(selenium)
    page.moda.click()
    page.wait_page_loaded()
    page.logo.click()   # переход на Главную по клику на Лого
    page.wait_page_loaded()
    curr_page = page.get_current_url()
    test_obj = inspect.stack()[0][3][5:]
    header_assertions(test_obj, curr_page)
