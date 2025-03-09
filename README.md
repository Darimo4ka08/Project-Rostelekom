# Project Rostelekom

## Описание проекта

Проект Rostelekom представляет собой набор автоматизированных тестов, направленных на проверку функциональности регистрационной формы. Он разработан с использованием Python и инструмента тестирования Selenium для обеспечения надежности и точности тестирования.

## Структура проекта
Project-Rostelekom/
├── .idea/ # Настройки IDE (PyCharm)
├── tests/ # Каталог с тестами
│ ├── conftest.py # Файл настроек для pytest
│ ├── registration_page.py # Логика взаимодействия с регистрационной формой
│ └── test_registration.py # Набор тестов для проверки регистрации
├── requirements.txt # Список зависимостей проекта
└── README.md # Описание проекта

Copy

## Установка и настройка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Darimo4ka08/Project-Rostelekom.git
   cd Project-Rostelekom
Создайте виртуальное окружение:

Для Linux/macOS:

bash
Copy
python -m venv .venv
source .venv/bin/activate
Для Windows:

bash
Copy
python -m venv .venv
.venv\Scripts\activate
Установите зависимости:

bash
Copy
pip install -r requirements.txt
Запуск тестов
Для запуска всех тестов выполните команду:

bash
Copy
pytest tests/
Для запуска тестов с генерацией HTML-отчёта:

bash
Copy
pytest --html=report.html --self-contained-html
## Тесты
Проект включает в себя следующие сценарии:

Проверка регистрации с корректным номером телефона.

Проверка ошибок валидации, таких как:

Неправильный формат номера телефона.

Несовпадение пароля и подтверждения.

Пустое или некорректное значение полей.

Пример теста
python
Copy
def test_registration_with_invalid_email(browser):
    page = RegistrationPage(browser)
    page.open()
    page.click_register_button()
    page.fill_email("invalid_email")  # Некорректный email
    page.fill_password("Password123")
    page.fill_confirm_password("Password123")
    page.click_submit_button()

    assert page.get_email_phone_error_message() == "Введите телефон в формате +7ХХХХХХХХХХ или email в формате example@email.ru", \
        "Ошибка: неверное сообщение об ошибке для некорректного email"
## Дополнительные сведения
PyTest используется для написания и выполнения тестов.

Selenium WebDriver — для взаимодействия с веб-интерфейсом.

Поддерживаемые браузеры: Chrome (рекомендуемый), Firefox.

Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

Автор: Darimo4ka08

Дата создания: март 2025
