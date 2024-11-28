from datetime import time


def activation_time_dark_theme(user_time):
    return time(hour=6) > user_time or user_time >= time(hour=22)


def get_user_by_name(user_list, name):
    for user in user_list:
        if user["name"] == name:
            return user


def get_lowest_age(user_list, age):
    new_users_list = []
    for user in user_list:
        if user["age"] < age:
            new_users_list.append(user)
    return new_users_list


def enable_dark_theme(dark_theme_enabled_by_user, current_time):
    if dark_theme_enabled_by_user is None:
        return activation_time_dark_theme(current_time)
    elif dark_theme_enabled_by_user:
        return True
    else:
        return False


def print_function_info(func, *args):
    name = func.__name__
    function_info = f"{name.title().replace("_", " ")} [{", ".join(args)}]"
    print(function_info)
    return function_info


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    is_dark_theme = activation_time_dark_theme(current_time)
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=23)
    dark_theme_enabled_by_user = False

    is_dark_theme = enable_dark_theme(dark_theme_enabled_by_user, current_time)
    assert is_dark_theme is False


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = get_user_by_name(users, "Olga")
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = get_lowest_age(users, 20)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_function_info(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_info(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_info(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
