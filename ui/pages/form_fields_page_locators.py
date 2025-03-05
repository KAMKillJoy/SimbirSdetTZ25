from selenium.webdriver.common.by import By


class FormFieldsPageLocators:
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
