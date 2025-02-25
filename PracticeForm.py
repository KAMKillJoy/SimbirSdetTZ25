import os

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

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
        if drink == "Water":
            self.find_element(PracticeFormLocators.LOCATOR_WATER_CHECKBOX).click()
        elif drink == "Milk":
            self.find_element(PracticeFormLocators.LOCATOR_MILK_CHECKBOX).click()
        elif drink == "Coffee":
            self.find_element(PracticeFormLocators.LOCATOR_COFFEE_CHECKBOX).click()
        elif drink == "Wine":
            self.find_element(PracticeFormLocators.LOCATOR_WINE_CHECKBOX).click()
        elif drink == "Ctrl-Alt-Delight":
            self.find_element(PracticeFormLocators.LOCATOR_CTRL_ALT_DELIGHT_CHECKBOX).click()
        else:
            raise ValueError('Wrong drink option Value!')

    def click_color(self, color):
        if color == "Red":
            element = self.find_element(PracticeFormLocators.LOCATOR_RED_RADIO)
            self.driver.execute_script("arguments[0].click();", element)
        elif color == "Blue":
            element = self.find_element(PracticeFormLocators.LOCATOR_BLUE_RADIO)
            self.driver.execute_script("arguments[0].click();", element)
        elif color == "Yellow":
            element = self.find_element(PracticeFormLocators.LOCATOR_YELLOW_RADIO)
            self.driver.execute_script("arguments[0].click();", element)
        elif color == "Green":
            element = self.find_element(PracticeFormLocators.LOCATOR_GREEN_RADIO)
            self.driver.execute_script("arguments[0].click();", element)
        elif color == "Ctrl-Alt-Delight":
            element = self.find_element(PracticeFormLocators.LOCATOR_FFC0CB_RADIO)
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise ValueError('Wrong color option Value!')


    def enter_dyl(self, dyl="Undecided"):
        element = self.find_element(PracticeFormLocators.LOCATOR_DYL_DROPDOWN)
        self.driver.execute_script("arguments[0].click();", element)
        if dyl == "Yes":
            self.find_element(PracticeFormLocators.LOCATOR_DYL_YES).click()
        elif dyl == "No":
            self.find_element(PracticeFormLocators.LOCATOR_DYL_NO).click()
        elif dyl == "Undecided":
            self.find_element(PracticeFormLocators.LOCATOR_DYL_UNDECIDED).click()
        else:
            raise ValueError('Wrong color option Value!')

    def count_tools(self):
        parent_tools_element = self.find_element(PracticeFormLocators.LOCATOR_TOOLS)
        return len(parent_tools_element.find_elements("xpath", './li'))

    def enter_message(self):
        self.find_element(PracticeFormLocators.LOCATOR_MESSAGE_TEXTFIELD).send_keys(PracticeFormMethods.count_tools(self))

    def click_submit(self):
        element = self.find_element(PracticeFormLocators.LOCATOR_SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)




    def check_modal_result(self):
        return self.check_exists(*PracticeFormLocators.LOCATOR_RESULT_MODAL_TABLE)

    def read_result_modal_title(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_TITLE))

    def read_result_modal_student_name(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_NAME))

    def read_result_modal_student_email(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_EMAIL))

    def read_result_modal_student_gender(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_GENDER))

    def read_result_modal_student_mobile(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_MOBILE))

    def read_result_modal_student_date_of_birth(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_DATE_OF_BIRTH))

    def read_result_modal_student_subjects(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_SUBJECTS))

    def read_result_modal_student_hobbies(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_HOBBIES))

    def read_result_modal_student_picture(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_PICTURE))

    def read_result_modal_student_address(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_ADDRESS))

    def read_result_modal_state_and_city(self):
        return self.read_element(self.find_element
                                 (PracticeFormLocators.LOCATOR_RESULT_MODAL_STUDENT_STATE_AND_CITY))
