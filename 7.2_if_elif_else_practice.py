good_credit = False
price_of_house = 10_00_000
credit_10_amount = int(price_of_house) * 0.1
credit_20_amount = int(price_of_house) * 0.2
if good_credit:
    print(f"Your credit is good , so you have to pay {credit_10_amount}")
else:
    print(f"Your credit score is very low , so you have to put down money {credit_20_amount}")
print("Thank you!")