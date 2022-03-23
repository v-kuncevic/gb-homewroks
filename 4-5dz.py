import utils

utils.parsing_courses

utils.recalculating_course

if __name__ == "__main__":
    import sys

    source_currency = sys.argv[1]
    destination_currency = 'BYN'  # Я из Беларуси, поэтому пусть будут бел.рубли
    amount = float('1')
    time_current_course, exchange_rate = utils.recalculating_course(source_currency, destination_currency, amount)
    print("Актуальный курс на:", time_current_course)
    print(f"{source_currency} = {exchange_rate} {destination_currency}")
