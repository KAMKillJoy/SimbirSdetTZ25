import allure

from PracticeForm import PracticeFormMethods
import testData.Users as Users
from confest import browser


def test_practice_form(browser):
    allure.dynamic.title("Тест заполнения формы")
    allure.dynamic.description("Тест заполняет форму, отправляет, "
                               "проверяет что появилось алерт с текстом 'Message received!'")
    allure.dynamic.tag("GUI_test", "Simbirsoft", "StudentForm")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    allure.dynamic.link("https://practice-automation.com/form-fields/", name="Website")

    practice_form = PracticeFormMethods(browser)
    user = Users.StudentVasia

    with allure.step("Открытие сайта"): practice_form.go_to_site()
    with allure.step("Введение имени"): practice_form.enter_firstname(user["firstname"])
    with allure.step("Введение пароля"): practice_form.enter_password(user["password"])
    with allure.step("Выбор напитка"): practice_form.click_drink(user["drink"])
    with allure.step("Выбор цвета"): practice_form.click_color(user["color"])
    with allure.step("Выбор ответа на вопрос 'Do you like automation?'"):
        practice_form.enter_dyl(user["DYL"])
    with allure.step("Введение email"): practice_form.enter_email(user["email"])
    with allure.step("Введение сообщения"): practice_form.enter_message()
    with allure.step("Отправка формы"): practice_form.click_submit()

    with allure.step("Проверка наличия алерта с текстом 'Message received!'"):
        alert = practice_form.driver.switch_to.alert
        assert "Message received!" in alert.text
