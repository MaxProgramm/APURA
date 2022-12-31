
# removes leading zero
def leading_zero_remover(number: str):
    number = list((number))
    while number[0] == "0":
        number.pop(0)
    return int("".join(number))

