class Date:
    str_date_format = ''

    def __init__(self, string_date):
        Date.str_date_format = string_date

    @classmethod
    def parse(cls):
        return list(map(int, cls.str_date_format.split('-')))

    @staticmethod
    def validate(string_date):
        validators = [lambda x: True if 1 <= x <= 31 else False, lambda x: True if 1 <= x <= 12 else False,
                      lambda x: True if x >= 1900 else False]
        for pos, el in enumerate(Date.parse()):
            if not validators[pos](el):
                raise ValueError(f"У вас неверное значение в позиции {pos + 1}")
        return True


int_date_format = Date('01-02-2021')
Date.validate(Date.str_date_format)
