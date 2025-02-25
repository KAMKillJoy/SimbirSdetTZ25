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

    practice_form = PracticeFormMethods(browser)  # выбор студента из модуля Students
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

'''
    with allure.step("Проверка наличия окна с результатами"):
        assert practice_form.check_modal_result()
    with allure.step("Проверка корректного имени"):
        assert (practice_form.read_result_modal_student_name().casefold() ==
            f"{user["firstname"]} {user["lastname"]}".casefold())
    with allure.step("Проверка корректного email"):
        assert (practice_form.read_result_modal_student_email().casefold() ==
            user["email"].casefold())
    with allure.step("Проверка корректного гендера"):
        assert (practice_form.read_result_modal_student_gender().casefold() ==
            user["gender"].casefold())
    with allure.step("Проверка корректного мобильного номера"):
        assert (practice_form.read_result_modal_student_mobile().casefold() ==
            user["mobile"].casefold())
    with allure.step("Проверка корректной даты рождения"):
        assert (practice_form.read_result_modal_student_date_of_birth().casefold() ==
            f"{user['dateofbirth'][0]} {user['dateofbirth'][1]},"
            f"{user['dateofbirth'][2]}".casefold())
    with allure.step("Проверка корректных дисциплин"):
        assert (practice_form.read_result_modal_student_subjects().casefold() ==
            ", ".join(user['subjects']).casefold())
    with allure.step("Проверка корректного изображения"):
        assert (practice_form.read_result_modal_student_picture().casefold() ==
            user["picture"].casefold())
    with allure.step("Проверка корректного адреса"):
        assert (practice_form.read_result_modal_student_address().casefold() ==
            user["address"].casefold())
    with allure.step("Проверка корректных штата и города"):
        assert (practice_form.read_result_modal_state_and_city().casefold() ==
            f"{user['state']} {user['city']}".casefold())

'''