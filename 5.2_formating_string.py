# formatting string # dynamic variable
first_name = 'John'
last_name = 'Smith'
message = first_name + ' [' + last_name + '] is a coder' # not ideal
print(message)

msg = f'{first_name} [{last_name}] is a coder' # String Concatination
print(msg)