class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_log):
        if not isinstance(new_log, str):
            raise TypeError
        if not '@' in new_log:
            raise ValueError
        if not '.' in new_log:
            raise ValueError
        if new_log.index('@') > new_log.index('.'):
            raise ValueError
        self.__login = new_log

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой")
        elif not 5 <= len(new_password) <= 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif not self.is_include_digit(new_password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif not self.is_include_only_latin(new_password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif self.check_password_dictionary(new_password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = new_password
    @staticmethod
    def is_include_digit(password):
        '''
        проверка пароля на наличие цифры
        :param password:
        :return: True or False
        '''
        from string import digits
        for value in password:
            if value in digits:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        '''
        Проверка на наличие верхнего и нижнего регистра
        :param password:
        :return: True or False
        '''
        if any(value.islower() for value in password) and any(value.isupper() for value in password):
            return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        '''
        Проверка на наличие только латинских букв
        :param password:
        :return: True or False
        '''
        from string import ascii_lowercase, digits
        for value in password.lower():
            if value in digits:
                continue
            elif value in ascii_lowercase:
                return True
        return False

    @staticmethod
    def check_password_dictionary(password):
        '''
        проверяет если пароль в файле легких паролей
        :param password:
        :return: True or False
        '''
        with open('easy_passwords.txt') as easy_passwords:
            list_easy_password = [i.replace('\n', '') for i in easy_passwords]
            if password in list_easy_password:
                return True
            return False








