cars = ['bmw', 'audi', 'subaru', 'toyota']

for car in cars:
    if(len(car) <= 3):
        print(car.upper())
    else:
        print(car.title())