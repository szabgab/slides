def check_money():
    return money > 1000000

def check_salary():
    salary += 1
    return salary >= 1000

while True:
    if check_money() or check_salary():
        print("I can live well")
