bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(bikes)
#second last from list
print(bikes[-2])
#formatting string 
print(f"I never had a {bikes[-3].title()}!")
#add at the end
bikes.append("caloi")
#add at the beggining
bikes.insert(0, "oggi")
print(bikes)
#remove by index
del bikes[3]
print(bikes)
#remove by value
bikes.remove("cannondale")
print(bikes)
bikes.sort(reverse=True)
print(bikes)