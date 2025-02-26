client_name = input("Your name ? -: ")
client_mem = int(input("How many people are in dinner groups? -: "))
if client_mem > 8:
    print(f"Mr.{client_name.upper()}, Please Wait !, tables are busy.")
else:
    print(f"Welcome Mr.{client_name.upper()} , Have a seat.")