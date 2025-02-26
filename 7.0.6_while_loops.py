# introducing while 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# user choose when to quit
prompt = "\nTell me something, and i will repeat back to you."
prompt += "\nEnter 'quit' to end program."
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

