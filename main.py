def check_choice(message: str, choices: tuple) -> str:
    """
    inputの選択肢が正しいかを確認する
    """
    while True:
        choice = input(message)
        if choice in choices:
            return choice
        print("Invalid input. Input correct choice.")

def check_calculation_input(message: str, 
                            ans: float,
                            negative_not_allowed: bool=False, 
                            zero_not_allowed: bool=False) -> float:
    """
    inputが計算の条件に適しているかを確認する
    """
    while True:
        choice = input(message)
        if choice == "ans":
            choice = ans
        
        try:
            choice = float(choice)
            if (negative_not_allowed)and(choice<0):
                print("Negative value is not allowed. Input positive float.")
            elif (negative_not_allowed)and(choice==0):
                print("Zero is not allowed. Input none zero.")
            else:
                return choice
        except:
            print("Invalid data. Input float.")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def main():
    """
    インプットを受け取り、各種関数を呼び出す
    """
    ans = None #初期値はNone
    message = "Input calculation type.\n"
    message += "1: addition, a + b\n"
    message += "2: subtraction, a - b\n"
    message += "3: multiplication, a * b\n"
    message += "4: division, a / b\n"
    message += "5: exponent, a ^ b\n"
    message += "6: square root, √a\n"
    choices = ("1","2","3","4","5","6")
    choice = check_choice(message, choices)

    if choice == "1":
        message = "Input a and b for a + b\n"
        message += "a = "
        a = check_calculation_input(message, ans, False, False)
        message = "b = "
        b = check_calculation_input(message, ans, False, False)
        ans = addition(a, b)
        print(f"{a} + {b} = {ans}")

    if choice == "2":
        message = "Input a and b for a - b\n"
        message += "a = "
        a = check_calculation_input(message, ans, False, False)
        message = "b = "
        b = check_calculation_input(message, ans, False, False)
        ans = subtraction(a, b)
        print(f"{a} - {b} = {ans}")

    if choice == "3":
        message = "Input a and b for a * b\n"
        message += "a = "
        a = check_calculation_input(message, ans, False, False)
        message = "b = "
        b = check_calculation_input(message, ans, False, False)
        ans = multiplication(a, b)
        print(f"{a} * {b} = {ans}")

main()