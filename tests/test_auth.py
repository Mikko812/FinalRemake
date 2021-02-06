from pages.auth_page import AuthPage, AuthPageCook
from pages.settings import email, password
# pytest -v --driver Chrome --driver-path C:/Windows/chromedriver.exe test_auth.py


def test_tmall_auth_page(selenium):
    page = AuthPage(selenium)
    page.login.click()
    login_page = page.get_current_url()

    msg = 'Не удалось перейти на страницу входа в ЛК.'
    assert 'login.aliexpress.com' in login_page, msg

    page.email = email
    page.password = password
    page.auth_btn.click()
    page.wait_page_loaded()
    acc_name = page.lk_in.get_attribute('innerText')

    assert acc_name == email.split('@')[0]


def test_tmall_auth_page_with_cookies(selenium):
    page = AuthPageCook(selenium)
    page.wait_page_loaded()
    acc_name = page.lk_in.get_attribute('innerText')

    assert acc_name == email.split('@')[0]
