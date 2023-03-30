
# Simple variables

i = 1 # Integer

i = i + 1

message = "Hello world!" # String

## Complex Variables

# Lists

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# for planet in planets:
#     print("Item is a string and its value is:", planet)

# Dictionaries

starships = {'1701': {
                'Captain': 'James T Kirk',
                'XO': 'Spock',
                'Chief Engineer': 'Scotty'},
             '74656': {
                'Captain': 'Kathryn Janeway',
                'XO': 'Chakotay',
                'Chief Engineer': 'B\'lana Torres'
             },
             '1864': 'Reliant'}

print(starships['74656']['Captain'])

