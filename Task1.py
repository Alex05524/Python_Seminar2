def Input(inText):
    is_OK = False
    while not is_OK:
        numb = float(input(f"{inText}"))
        is_OK = True
        return numb

def Summ(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum

number = Input("Введите число: ")
print(f"Результат суммы цифр = {Summ(number)}")