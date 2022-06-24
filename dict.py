alien_0 = {
    'color': 'green',
    'point': 5
    }
print(alien_0['color'])
alien_0['color'] = 'red'
print(alien_0['color'])
print(alien_0)
del alien_0['point']
print(alien_0.get('point', 'None value'))

user = {
    'username': 'phenrique',
    'first': 'pedro',
    'last': 'henrique',
    }
for k, v in user.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
for name in sorted(favorite_languages.keys()):
    print(f"thank you {name.title()} for taking the poll")

