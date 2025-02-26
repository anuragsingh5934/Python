# moving items from one list to another

unconfirmed_user = ['sumit','kundan', 'adarsh', 'prince']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print(f"Verifying user : {current_user}")
    confirmed_user.append(current_user)
print("\nThe following users have been confirmed")
for confirmed_use in confirmed_user:
    print(confirmed_use)