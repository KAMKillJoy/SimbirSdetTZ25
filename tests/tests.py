import allure

from ui.pages.form_fields_page import FormFieldsPageMethods
import test_data.users as users
from conftest import browser


def test_form_fields(browser):
    allure.dynamic.title("Тест заполнения формы")
    allure.dynamic.description("Тест заполняет форму, отправляет, "
                               "проверяет что появилось алерт с текстом 'Message received!'")
    allure.dynamic.tag("GUI_test", "Simbirsoft", "StudentForm")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    allure.dynamic.link("https://practice-automation.com/form-fields/", name="Website")

    form_fields = FormFieldsPageMethods(browser)
    user = users.Vasia

    with allure.step("Открытие сайта"): form_fields.go_to_site()
    form_fields.enter_firstname(user["firstname"])
    form_fields.enter_password(user["password"])
    for drink in user["drinks"]:
        form_fields.click_drink(drink)
    for color in user["colours"]:
        form_fields.click_color(color)
    form_fields.enter_dyl(user["DYL"])
    form_fields.enter_email(user["email"])
    form_fields.enter_message( f"{form_fields.count_tools()}\n"
                               f"{form_fields.find_longest_tool()}")
    form_fields.click_submit()
    assert "Message received!" in form_fields.check_alert()
