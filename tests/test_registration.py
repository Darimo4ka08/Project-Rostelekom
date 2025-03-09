import pytest
from selenium.webdriver.common.by import By
from registration_page import RegistrationPage

### ТЕСТЫ ДЛЯ ПОЛЯ "ИМЯ"
## Позитивные тесты
# Тест для регистрации с именем из 2 символов
def test_registration_with_2_symbol_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("Ив")
    page.fill_surname("")  # Убираем фокус с поля "Имя"
    error_message = browser.find_elements(*page.error_message)
    assert len(error_message) == 0, "Ошибка: сообщение об ошибке отображается при вводе имени из 2 символов"

# Тест для регистрации с именем из 30 символов
def test_registration_with_30_symbol_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("А" * 30)
    page.fill_surname("")  # Убираем фокус с поля "Имя"
    error_message = browser.find_elements(*page.error_message)
    assert len(error_message) == 0, "Ошибка: сообщение об ошибке отображается при вводе имени из 30 символов"


## Негативные тесты
# Тест для регистрации с пустым именем
def test_registration_with_empty_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("")
    page.fill_surname("Иванов")
    page.select_region()
    page.fill_email("iv@example.com")
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()
    assert page.get_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при пустом имени"

# Тест для регистрации с именем из 1 символа
def test_registration_with_1_symbol_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("И")  # Имя из 1 символа
    page.fill_surname("")  # Перенос фокуса с поля "Имя"
    assert page.get_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе имени из 1 символа"

# Тест для регистрации с именем из 31 символа
def test_registration_with_31_symbol_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("А" * 31)  # Имя из 31 символа
    page.fill_surname("")  # Перенос фокуса с поля "Имя"
    assert page.get_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе имени из 31 символа"

# Тест для регистрации с именем, содержащим буквы и цифры
def test_registration_with_letters_and_numbers_in_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("Ан123")  # Имя с буквами и цифрами
    page.fill_surname("")  # Перенос фокуса с поля "Имя"
    assert page.get_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе имени, содержащего буквы и цифры"

# Тест для регистрации с именем, состоящим из английских букв
def test_registration_with_english_letters_in_name(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("John")  # Имя на английском
    page.fill_surname("")  # Перенос фокуса с поля "Имя"
    assert page.get_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе имени на английском языке"


### ТЕСТЫ ДЛЯ ПОЛЯ "ФАМИЛИЯ"
## Позитивные тесты
# Регистрация с фамилией из 2 символов
def test_registration_with_2_symbol_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_surname("Ан")  # Ввод фамилии из 2 символов
    page.fill_name("")  # Убираем фокус с поля "Фамилия"
    error_message = browser.find_elements(*page.error_message)
    assert len(error_message) == 0, "Ошибка: сообщение об ошибке отображается при вводе фамилии из 2 символов"

# Регистрация с фамилией из 30 символов
def test_registration_with_30_symbol_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_surname("И" * 30)  # Ввод фамилии из 30 символов
    page.fill_name("")  # Убираем фокус с поля "Фамилия"
    error_message = browser.find_elements(*page.error_message)
    assert len(error_message) == 0, "Ошибка: сообщение об ошибке отображается при вводе фамилии из 30 символов"

## Негативные тесты
# Регистрация с пустой фамилией
def test_registration_with_empty_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_name("Иван")  # Валидное имя
    page.fill_surname("")  # Пустая фамилия
    page.select_region()
    page.fill_email("example@example.com")
    page.fill_password("Password123")
    page.fill_confirm_password("Password123")
    page.click_submit_button()
    assert page.get_surname_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при пустой фамилии"

# Регистрация с фамилией из 1 символа
def test_registration_with_1_symbol_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_surname("А")  # Фамилия из 1 символа
    page.fill_name("")  # Перенос фокуса с поля "Фамилия"
    assert page.get_surname_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе фамилии из 1 символа"

# Регистрация с фамилией из 31 символа
def test_registration_with_31_symbol_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_surname("И" * 31)  # Фамилия из 31 символа
    page.fill_name("")  # Перенос фокуса с поля "Фамилия"
    assert page.get_surname_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе фамилии из 31 символа"

# Регистрация с фамилией, содержащей буквы и цифры
def test_registration_with_letters_and_numbers_in_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_surname("Ив123")  # Фамилия с буквами и цифрами
    page.fill_name("")  # Перенос фокуса с поля "Фамилия"
    assert page.get_surname_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе фамилии с буквами и цифрами"

# Регистрация с фамилией, состоящей из английских букв
def test_registration_with_english_letters_in_surname(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_surname("Smith")  # Фамилия на английском
    page.fill_name("")  # Перенос фокуса с поля "Фамилия"
    assert page.get_surname_error_message() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов.", \
        "Ошибка: сообщение об ошибке не отображается при вводе фамилии на английском языке"


### ТЕСТЫ ДЛЯ ПОЛЯ "ПАРОЛЬ"
## Позитивные тесты
# Тест для регистрации с паролем из 8 символов
def test_registration_with_8_symbol_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение пароля из 8 символов
    page.fill_password("Pass1234")
    page.fill_confirm_password("Pass1234")
    page.fill_name("")  # Перенос фокуса для вызова валидации

    # Проверка отсутствия сообщения об ошибке
    assert not page.browser.find_elements(*page.password_error_message), \
        "Ошибка: сообщение об ошибке отображается при вводе пароля из 8 символов"

# Тест для регистрации с паролем из 20 символов
def test_registration_with_20_symbol_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_password("Password1234567890!!")  # Пароль из 20 символов
    page.fill_confirm_password("Password1234567890!!")  # Подтверждение пароля
    page.fill_name("")  # Перенос фокуса
    assert not page.browser.find_elements(*page.password_error_message), \
        "Ошибка: сообщение об ошибке отображается при вводе пароля из 20 символов"

## Негативные тесты
# Тест для регистрации с паролем из 7 символов
def test_registration_with_7_symbol_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_password("Pass123")  # Пароль из 7 символов
    page.fill_confirm_password("Pass123")  # Подтверждение пароля
    page.fill_name("")  # Перенос фокуса
    assert page.get_password_error_message() == "Длина пароля должна быть не менее 8 символов", \
        "Ошибка: неверное сообщение об ошибке для пароля из 7 символов"

# Тест для регистрации с пустым полем "Пароль"
def test_registration_with_empty_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение остальных обязательных полей
    page.fill_name("Иван")
    page.fill_surname("Иванов")
    page.select_region()
    page.fill_email("example@mail.ru")  # Корректный email
    page.fill_password("")  # Пустое поле "Пароль"
    page.fill_confirm_password("Password123")  # Подтверждение пароля
    page.click_submit_button()

    # Проверка сообщения об ошибке для пустого пароля
    assert page.get_password_error_message() == "Длина пароля должна быть не менее 8 символов", \
        "Ошибка: неверное сообщение об ошибке для пустого пароля"

# Тест для регистрации с пустым полем "Подтверждение пароля"
def test_registration_with_empty_confirm_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение остальных полей
    page.fill_name("Иван")  # Корректное значение на кириллице
    page.fill_surname("Иванов")  # Корректное значение на кириллице
    page.select_region()  # Выбор региона
    page.fill_email("example@mail.ru")  # Корректный email
    page.fill_password("Password123")  # Валидный пароль
    page.fill_confirm_password("")  # Пустое поле "Подтверждение пароля"
    page.click_submit_button()

    # Проверка сообщения об ошибке для несовпадения паролей
    assert page.get_password_error_message() == "Пароли не совпадают", \
        "Ошибка: неверное сообщение об ошибке для пустого подтверждения пароля"

# Тест для регистрации с паролем из 21 символа
def test_registration_with_21_symbol_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_password("Password1234567890!!!")  # Пароль из 21 символа
    page.fill_confirm_password("Password1234567890!!!")  # Подтверждение пароля
    page.fill_name("")  # Перенос фокуса
    assert page.get_password_error_message() == "Длина пароля должна быть не более 20 символов", \
        "Ошибка: неверное сообщение об ошибке для пароля из 21 символа"

# Тест для регистрации с паролем без заглавных букв
def test_registration_with_no_uppercase_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_password("password123")  # Пароль без заглавных букв
    page.fill_confirm_password("password123")  # Подтверждение пароля
    page.fill_name("")  # Перенос фокуса
    assert page.get_password_error_message() == "Пароль должен содержать хотя бы одну заглавную букву", \
        "Ошибка: неверное сообщение об ошибке для пароля без заглавных букв"

# Тест для регистрации с паролем на кириллице
def test_registration_with_cyrillic_password(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_password("Пароль123")  # Пароль на кириллице
    page.fill_confirm_password("Пароль123")  # Подтверждение пароля
    page.fill_name("")  # Перенос фокуса
    assert page.get_password_error_message() == "Пароль должен содержать только латинские буквы", \
        "Ошибка: неверное сообщение об ошибке для пароля на кириллице"

# Тест для регистрации с несовпадающими паролями
def test_registration_with_mismatched_passwords(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")  # Поле "Имя"
    page.fill_surname("Иванов")  # Поле "Фамилия"
    page.select_region()  # Выбор региона
    page.fill_email("example@example.com")  # Поле "Email"
    page.fill_password("Password123")  # Поле "Пароль"
    page.fill_confirm_password("Password321")  # Поле "Подтверждение пароля"

    # Перенос фокуса через нажатие кнопки "Зарегистрироваться"
    page.click_submit_button()

    # Проверка сообщения об ошибке
    assert page.get_mismatched_password_error_message() == "Пароли не совпадают", \
        "Ошибка: неверное сообщение об ошибке для несовпадающих паролей"


### ТЕСТЫ ДЛЯ ПОЛЯ "E-mail или мобильный телефон"
## Позитивные тесты
# Регистрация с корректным номером телефона
def test_valid_email_or_phone_field(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение только поля "E-mail или мобильный телефон"
    page.fill_email("+79123456789")  # Корректный номер телефона

    # Проверка отсутствия сообщения об ошибке для поля
    assert not page.browser.find_elements(*page.email_phone_error_message), \
        "Ошибка: сообщение об ошибке появилось при корректном вводе номера телефона"

# Регистрация с пустым полем "E-mail или мобильный телефон"
def test_registration_with_empty_email_or_phone(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех полей, кроме "E-mail или мобильный телефон"
    page.fill_name("Иван")
    page.fill_surname("Иванов")
    page.select_region()
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.fill_name("")  # Перенос фокуса, например, снова на поле "Имя"
    page.click_submit_button()

    # Проверка сообщения об ошибке
    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для пустого поля 'E-mail или мобильный телефон'"

# Регистрация с некорректным форматом номера телефона
def test_registration_with_invalid_phone_format(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")
    page.fill_surname("Иванов")
    page.select_region()
    page.fill_email("99999999999")  # Некорректный номер телефона
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()

    # Проверка сообщения об ошибке для поля "E-mail или мобильный телефон"
    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для некорректного формата номера телефона"

# Регистрация с номером телефона, содержащим буквы
def test_registration_with_phone_containing_letters(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")  # Корректное значение на кириллице
    page.fill_surname("Иванов")  # Корректное значение на кириллице
    page.select_region()  # Выбор региона
    page.fill_email("+7 912 а45-67-89")  # Номер телефона с буквами
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()

    # Проверка сообщения об ошибке
    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для номера телефона, содержащего буквы"

# Регистрация с некорректным email (без домена)
def test_registration_with_invalid_email_without_domain(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")  # Корректное значение на кириллице
    page.fill_surname("Иванов")  # Корректное значение на кириллице
    page.select_region()  # Выбор региона
    page.fill_email("ivan@example")  # Некорректный email (без домена)
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()

    # Проверка сообщения об ошибке
    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для email без домена"

# Регистрация с email без символа "@"
def test_registration_with_email_without_at_symbol(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")  # Корректное значение на кириллице
    page.fill_surname("Иванов")  # Корректное значение на кириллице
    page.select_region()  # Выбор региона
    page.fill_email("ivanexample")  # Email без символа "@"
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()

    # Проверка сообщения об ошибке
    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для email без символа '@'"

# Регистрация с уже существующим email
def test_registration_with_existing_email(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")  # Корректное значение на кириллице
    page.fill_surname("Иванов")  # Корректное значение на кириллице
    page.select_region()  # Выбор региона
    page.fill_email("test_qap@bk.ru")  # Уже существующий email
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()

    # Проверка сообщения об уже существующей учётной записи
    assert page.get_existing_account_message() == "Учётная запись уже существует", \
        "Ошибка: неверное сообщение об ошибке для уже существующего email"

# Регистрация с email, содержащим пробелы
def test_registration_with_email_containing_spaces(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()

    # Заполнение всех обязательных полей
    page.fill_name("Иван")  # Корректное значение на кириллице
    page.fill_surname("Иванов")  # Корректное значение на кириллице
    page.select_region()  # Выбор региона
    page.fill_email("ivan @example.com")  # Email с пробелами
    page.fill_password("Passwo11")
    page.fill_confirm_password("Passwo11")
    page.click_submit_button()

    # Проверка сообщения об ошибке
    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для email с пробелами"











