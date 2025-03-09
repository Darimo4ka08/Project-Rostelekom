from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://b2c.passport.rt.ru"

    # Локаторы
    register_button = (By.XPATH, "//*[@id='kc-register']")  # Кнопка "Зарегистрироваться"
    name_input = (By.NAME, "firstName")  # Поле ввода имени
    surname_input = (By.NAME, "lastName")  # Поле ввода фамилии
    dropdown_button = (By.CSS_SELECTOR, "svg.rt-base-icon.rt-select__arrow")  # Кнопка выпадающего списка для региона
    region_option = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[2]/div[2]/div[2]/div/div[40]")  # Опция региона "Москва"
    email_input = (By.ID, "address")  # Поле ввода email
    password_input = (By.ID, "password")  # Поле ввода пароля
    confirm_password_input = (By.ID, "password-confirm")  # Поле подтверждения пароля
    submit_button = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/button")  # Кнопка отправки формы
    error_message = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[1]/span")  # Сообщение об ошибке (общее)
    email_phone_error_message = (By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")  # Сообщение об ошибке для поля "E-mail или мобильный телефон"
    surname_error_message = (By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")  # Сообщение об ошибке для фамилии
    password_error_message = (By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")  # Сообщение об ошибке для пароля
    mismatched_password_error_message = (By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")  # Сообщение "Пароли не совпадают"
    existing_account_message = (By.CSS_SELECTOR, "h2.card-modal__title") # сообщение об уже существующей учётной записи

    # Методы
    def open(self):
        self.browser.get(self.base_url)

    def click_register_button(self):
        """Клик на кнопку 'Зарегистрироваться'"""
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.register_button)
        ).click()

    def fill_name(self, name):
        """Заполнение поля 'Имя'"""
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.name_input)
        ).send_keys(name)

    def fill_surname(self, surname):
        """Заполнение поля 'Фамилия'"""
        self.browser.find_element(*self.surname_input).send_keys(surname)

    def select_region(self):
        """Выбор региона"""
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.dropdown_button)
        ).click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.region_option)
        ).click()

    def fill_email(self, email):
        """Заполнение поля 'Email'"""
        self.browser.find_element(*self.email_input).send_keys(email)

    def fill_password(self, password):
        """Заполнение поля 'Пароль'"""
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.password_input)
        ).send_keys(password)

    def fill_confirm_password(self, confirm_password):
        """Заполнение поля 'Подтверждение пароля'"""
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.confirm_password_input)
        ).send_keys(confirm_password)

    def click_submit_button(self):
        """Клик на кнопку отправки формы"""
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()

    def get_error_message(self):
        """Получение общего сообщения об ошибке"""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.error_message)
        ).text

    def get_surname_error_message(self):
        """Получение сообщения об ошибке для поля 'Фамилия'"""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.surname_error_message)
        ).text

    def get_password_error_message(self):
        """Получение сообщения об ошибке для поля 'Пароль'"""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.password_error_message)
        ).text

    def get_mismatched_password_error_message(self):
        """Получение сообщения 'Пароли не совпадают'"""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.mismatched_password_error_message)
        ).text

    def get_email_phone_error_message(self):
        """Получение сообщения об ошибке для поля 'E-mail или мобильный телефон'"""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.email_phone_error_message)
        ).text

    def get_existing_account_message(self):
        """Получение сообщения об уже существующей учётной записи"""
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.existing_account_message)
        ).text