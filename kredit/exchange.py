def money_exchange(ThNumOfMoney, value):

    USD = {"code": "us", "rate": 62}
    EURO = {"code": "eu", "rate": 76}
    CNY = {"code": "ch", "rate": 10}

    print("Варианты валюты:")
    print("USD-code:", USD["code"])
    print("EURO-code:", EURO["code"])
    print("CNY-code:", CNY["code"])

    currency = input("Введите код валюты: ")

    if currency == USD["code"]:
        value = "dollars"
        return round(ThNumOfMoney / USD["rate"],2),value
    if currency == EURO["code"]:
        value = "euros"
        return round(ThNumOfMoney / EURO["rate"],2), value
    if currency == CNY["code"]:
        value = "yuan"
        return round(ThNumOfMoney / CNY["rate"],2), value

def main():
    ThNumOfMoney = int(input("Введите сумму денег для обмена (в рублях): "))
    value = "рублей"

    print("Сумма после обмена: ", money_exchange(ThNumOfMoney, value))
    print("Ваша изначальная сумма: ", ThNumOfMoney, value)


if __name__ == "__main__":
    main()