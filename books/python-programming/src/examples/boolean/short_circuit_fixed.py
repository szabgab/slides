def check_money():
    return money > 1000000

def check_salary():
    salary += 1
    return salary >= 1000

while True:
    has_good_money = check_money()
    has_good_salary = check_salary()

    if has_good_money or has_good_salary:
        print("I can live well")
