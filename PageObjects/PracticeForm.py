from BaseApp import BasePage
from selenium.webdriver.common.by import By


class PracticeFormLocators:
    LOCATOR_FIRSTNAME_TEXTFIELD = (By.ID, "name-input")
    LOCATOR_PASSWORD_TEXTFIELD = (By.CSS_SELECTOR, "label:nth-of-type(2) > input")

    # Локаторы favorite drink
    LOCATOR_WATER_CHECKBOX = (By.XPATH, "//label[contains(text(), 'Water')]")
    LOCATOR_MILK_CHECKBOX = (By.XPATH, "//label[contains(text(), 'Milk')]")
    LOCATOR_COFFEE_CHECKBOX = (By.XPATH, "//label[contains(text(), 'Coffee')]")
    LOCATOR_WINE_CHECKBOX = (By.XPATH, "//label[contains(text(), 'Wine')]")
    LOCATOR_CTRL_ALT_DELIGHT_CHECKBOX = (By.XPATH, "//label[contains(text(), 'Ctrl-Alt-Delight')]")

    # Локаторы favorite color
    LOCATOR_RED_RADIO = (By.XPATH, "//label[contains(text(), 'Red')]")
    LOCATOR_BLUE_RADIO = (By.XPATH, "//label[contains(text(), 'Blue')]")
    LOCATOR_YELLOW_RADIO = (By.XPATH, "//label[contains(text(), 'Yellow')]")
    LOCATOR_GREEN_RADIO = (By.XPATH, "//label[contains(text(), 'Green')]")
    LOCATOR_FFC0CB_RADIO = (By.XPATH, "//label[contains(text(), '#FFC0CB')]")

    # Локаторы Do you like automation?
    LOCATOR_DYL_DROPDOWN = (By.XPATH, "//select[@id='automation']")
    LOCATOR_DYL_YES = (By.XPATH, "//*[@id='automation']/option[2]")
    LOCATOR_DYL_NO = (By.XPATH, "//*[@id='automation']/option[3]")
    LOCATOR_DYL_UNDECIDED = (By.XPATH, "//*[@id='automation']/option[4]")

    LOCATOR_EMAIL_TEXTFIELD = (By.XPATH, "//input[@id='email']")

    LOCATOR_MESSAGE_TEXTFIELD = (By.XPATH, "//textarea[@id='message']")

    LOCATOR_TOOLS = (By.XPATH, "//*[@id='feedbackForm']/ul")

    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit-btn']")


class PracticeFormMethods(BasePage):
    def enter_firstname(self, firstname):
        self.find_element(PracticeFormLocators.LOCATOR_FIRSTNAME_TEXTFIELD).send_keys(firstname)


    def enter_password(self, password):
        self.find_element(PracticeFormLocators.LOCATOR_PASSWORD_TEXTFIELD).send_keys(password)


    def enter_email(self, email):
        self.find_element(PracticeFormLocators.LOCATOR_EMAIL_TEXTFIELD).send_keys(email)


    def click_drink(self, drink):
        drink_dict = {
            "Water": PracticeFormLocators.LOCATOR_WATER_CHECKBOX,
            "Milk": PracticeFormLocators.LOCATOR_MILK_CHECKBOX,
            "Coffee": PracticeFormLocators.LOCATOR_COFFEE_CHECKBOX,
            "Wine": PracticeFormLocators.LOCATOR_WINE_CHECKBOX,
            "Ctrl-Alt-Delight": PracticeFormLocators.LOCATOR_CTRL_ALT_DELIGHT_CHECKBOX
        }

        if drink_locator := drink_dict.get(drink):
            element = self.find_element(drink_locator)
            element.click()
        else:
            raise ValueError('Wrong drink option Value!')


    def click_color(self, color):
        color_dict = {
            "Red": PracticeFormLocators.LOCATOR_RED_RADIO,
            "Blue": PracticeFormLocators.LOCATOR_BLUE_RADIO,
            "Yellow": PracticeFormLocators.LOCATOR_YELLOW_RADIO,
            "Green": PracticeFormLocators.LOCATOR_GREEN_RADIO,
            "Ctrl-Alt-Delight": PracticeFormLocators.LOCATOR_FFC0CB_RADIO
        }

        if color_locator := color_dict.get(color):
            element = self.find_element(color_locator)
            self.driver.execute_script("arguments[0].click();", element)  # здесь и далее использую
            # джаваскрипт для кликов, так как стандартный способ вызывает click intercepted.
        else:
            raise ValueError('Wrong color option Value!')


    def enter_dyl(self, dyl):
        dyl_dict = {
            "Yes": PracticeFormLocators.LOCATOR_DYL_YES,
            "No": PracticeFormLocators.LOCATOR_DYL_NO,
            "Undecided": PracticeFormLocators.LOCATOR_DYL_UNDECIDED
        }

        if dyl_locator := dyl_dict.get(dyl):
            element = self.find_element(dyl_locator)
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise ValueError('Wrong DYL option Value!')


    def count_tools(self):
        parent_tools_element = self.find_element(PracticeFormLocators.LOCATOR_TOOLS)
        return len(parent_tools_element.find_elements("xpath", './li'))


    def find_longest_tool(self):
        parent_tools_element = self.find_element(PracticeFormLocators.LOCATOR_TOOLS)
        tools = [i.text for i in parent_tools_element.find_elements("xpath", './li')]
        return max(tools, key=len)


    def enter_message(self, message):
        self.find_element(PracticeFormLocators.LOCATOR_MESSAGE_TEXTFIELD).send_keys(message)


    def click_submit(self):
        element = self.find_element(PracticeFormLocators.LOCATOR_SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)


    def check_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text
