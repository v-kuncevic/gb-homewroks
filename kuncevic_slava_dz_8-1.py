import re


def email_parse(email_address):
    pattern = re.compile(r'^(\w+)@(\w+\.\w+)$')
    result = pattern.match(email_address)
    if not result:
        raise ValueError(f'wrong email: {email_address}')
    return result.groupdict()


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
