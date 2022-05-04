class ListVerification(Exception):
    pass


if __name__ == '__main__':
    exception = []
    while True:
        num = input('Введите число или "stop" для выхода: ')
        if num == 'stop':
            break
        try:
            exception.append(float(num))
        except ValueError:
            raise ListVerification(num)
