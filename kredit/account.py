def credit_account(money, rate, period):

    money_per_month = money * (rate / 100 + 1) ** period \
                      * (rate / 100) / ((rate / 100 + 1) ** period - 1)
    # Итоговая сумма выплаты по кредиту
    result = round(money_per_month * period)
    return result




if __name__ == "__main__":
    main()
