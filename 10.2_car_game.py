command = ''
while True:
    command = input('>' ).lower()
    if command == 'start':
         print("Your car has been started successfully")
    elif command == 'stop':
         print("car stopped")
    elif command == 'help':
         print("""
start 
stop
quit""")
    elif command == 'quit':
         break
    else:
         print("I do not understand")