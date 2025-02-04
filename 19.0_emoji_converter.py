emojis = {':)': '😊', ':(':'😡' }

message = input('>  ')

words = message.split()

output = ''
for word in words:
    translate = emojis.get(word, word)
    output = output+ ' ' + translate
print(output)