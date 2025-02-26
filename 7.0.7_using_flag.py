# flag
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit to quit game'"
active = True # this is flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)