class CorrectUser:
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    FIRSTNAME = 'TestUserName'
    LASTNAME = 'TestLastName'
    ZIPCODE = '1234'


class InCorrectUser:
    USERNAME = '1111'
    PASSWORD = '1111'


class ErrorMessage:
    INCORRECT_LOGIN = 'Epic sadface: Username and password do not match any user in this service'
