from account import credit_account
from exchange import money_exchange

def main():
    s = int(input("Ссумма кредита: "))
    p = int(input("Ставка: "))
    l = int(input("Срок кредита: "))

    result_calculator = credit_account(s, p, l)
    value = "рублей"
    result_exchange = money_exchange(result_calculator, value)

    print("\nПараметры счета: ")
    print("Сумма кредита: ", s, value)
    print("Срок кредита: ", l, "м")
    print("Процентная ставка: ", p, "%")
    print("Сумма выплаты по кредиту: ", result_calculator, value)
    print("Сумма с учетом перевода: ", result_exchange)


if __name__ == "__main__":
    main()