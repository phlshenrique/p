one_to_million = [x for x in range(1,1000001)]
# for number in one_to_million:
    # print(number)

print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))

cubes = [cube**3 for cube in range(1,11)]
for cube in cubes:
    print(cube)

even = [number for number in range(1,11) if number % 2 == 0]
print("Even: ", even)