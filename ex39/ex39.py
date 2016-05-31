states = {
    'Oregan': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Hawaii': 'HI',
}

cities = {
    'CA': 'Los Angeles',
    'HI': 'Honolulu',
    'FL': 'Jacksonville',
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

print('-'*10)
print("Hawaii's abbreviation is: %s" % states['Hawaii'])
print("Florida's abbreviation is: %s" % states['Florida'])

print('-'*10)
print("states = %s" % states)
print("states.items() = %s" % str(states.items()))
print('-'*10)
for state, abbrev in states.items():
    print ("%s is abbreviated %s" % (state, abbrev))

print('-'*10)
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city))

print('-'*10)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-'*10)
state=states.get('Texas')

if not state:
    print("Sorry,no Texas")

city=cities.get('TX', 'Not Entered Yet')
print("The city for the state'TX' is: %s" %city)