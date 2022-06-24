text = "Tell me a number and I'll print it, if it is even"
text += "\nOtherwise I'll not print it! type 'Exit' to quit! \n~> "

while True:
    entry = input(text)
    if entry.lower() == 'exit':
        break
    try:
        if int(entry) % 2 == 0:
            print("It's even!")
    except ValueError:
        print("Only 'numbers' or 'Exit' accepted")
print("Program ended!")
