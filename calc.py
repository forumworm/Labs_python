s = [0, 1]
oper = ["and", "or", "n=", "="]
print("Возможные операции: ", oper)

a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))
sign = input("Введите значение операции: ")

if (a in s) and (b in s) and (sign in oper):
    a = bool(a)
    b = bool(b)
    if sign == oper[0]:
        result = int(a & b)
        print(result)
    if sign == oper[1]:
        result = int(a | b)
        print(result)
    if sign == oper[2]:
        result = int((a != b))
        print(result)
    if sign == oper[3]:
        result = int(a == b)
        print(result)

else:
    print("Значения не верны")