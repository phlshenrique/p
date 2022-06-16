from statistics import mean

numbers = list(range(1,11))

print(min(numbers))
print(max(numbers))
print(mean(numbers))

squares = [value**2 for value in range(1,10)]
print(squares)

if(9 in squares):
    print(True)

magicians = ['Alice', 'edward', 'silvio']
for magician in magicians:
    print(f"{magician.title()}, did a great job")