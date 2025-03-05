import allure
from ui.base.base_page import BasePage
from ui.pages.form_fields_page_locators import FormFieldsPageLocators


class FormFieldsPageMethods(BasePage):
    @allure.step("Вводим имя: {firstname}")
    def enter_firstname(self, firstname):
        self.find_element(FormFieldsPageLocators.LOCATOR_FIRSTNAME_TEXTFIELD).send_keys(firstname)


    @allure.step("Вводим пароль: {password}")
    def enter_password(self, password):
        self.find_element(FormFieldsPageLocators.LOCATOR_PASSWORD_TEXTFIELD).send_keys(password)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        self.find_element(FormFieldsPageLocators.LOCATOR_EMAIL_TEXTFIELD).send_keys(email)


    @allure.step("Выбираем напиток: {drink}")
    def click_drink(self, drink):
        drink_dict = {
            "Water": FormFieldsPageLocators.LOCATOR_WATER_CHECKBOX,
            "Milk": FormFieldsPageLocators.LOCATOR_MILK_CHECKBOX,
            "Coffee": FormFieldsPageLocators.LOCATOR_COFFEE_CHECKBOX,
            "Wine": FormFieldsPageLocators.LOCATOR_WINE_CHECKBOX,
            "Ctrl-Alt-Delight": FormFieldsPageLocators.LOCATOR_CTRL_ALT_DELIGHT_CHECKBOX
        }

        if drink_locator := drink_dict.get(drink):
            element = self.find_element(drink_locator)
            element.click()
        else:
            raise ValueError('Wrong drink option Value!')

    @allure.step("Выбираем цвет: {color}")
    def click_color(self, color):
        color_dict = {
            "Red": FormFieldsPageLocators.LOCATOR_RED_RADIO,
            "Blue": FormFieldsPageLocators.LOCATOR_BLUE_RADIO,
            "Yellow": FormFieldsPageLocators.LOCATOR_YELLOW_RADIO,
            "Green": FormFieldsPageLocators.LOCATOR_GREEN_RADIO,
            "Ctrl-Alt-Delight": FormFieldsPageLocators.LOCATOR_FFC0CB_RADIO
        }

        if color_locator := color_dict.get(color):
            element = self.find_element(color_locator)
            self.driver.execute_script("arguments[0].click();", element)  # здесь и далее использую
            # джаваскрипт для кликов, так как стандартный способ вызывает click intercepted.
        else:
            raise ValueError('Wrong color option Value!')

    @allure.step("Выбираем заинтересованность в автоматизировании: {dyl}")
    def enter_dyl(self, dyl):
        dyl_dict = {
            "Yes": FormFieldsPageLocators.LOCATOR_DYL_YES,
            "No": FormFieldsPageLocators.LOCATOR_DYL_NO,
            "Undecided": FormFieldsPageLocators.LOCATOR_DYL_UNDECIDED
        }

        if dyl_locator := dyl_dict.get(dyl):
            element = self.find_element(dyl_locator)
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise ValueError('Wrong DYL option Value!')


    def count_tools(self):
        parent_tools_element = self.find_element(FormFieldsPageLocators.LOCATOR_TOOLS)
        return len(parent_tools_element.find_elements("xpath", './li'))


    def find_longest_tool(self):
        parent_tools_element = self.find_element(FormFieldsPageLocators.LOCATOR_TOOLS)
        tools = [i.text for i in parent_tools_element.find_elements("xpath", './li')]
        return max(tools, key=len)

    @allure.step("Вводим сообщение: {message}")
    def enter_message(self, message):
        self.find_element(FormFieldsPageLocators.LOCATOR_MESSAGE_TEXTFIELD).send_keys(message)


    @allure.step("Нажимаем submit (отправляем форму)")
    def click_submit(self):
        element = self.find_element(FormFieldsPageLocators.LOCATOR_SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Проверка наличия алерта с текстом 'Message received!'")
    def check_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text
