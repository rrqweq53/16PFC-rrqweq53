import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Hawaii', 'HI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'Los Angeles')
hashmap.set(cities, 'HI', 'Honolulu')
hashmap.set(cities, 'FL', 'Orlando')

hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print('-'*10)
print('NY State has: %s' % hashmap.get(cities,'NY'))
print('HI State has: %s' % hashmap.get(cities,'HI'))

print('-'*10)
print("Hawaii's abbreviation is: %s" % hashmap.get(states, 'Hawaii'))
print("Florida's abbreviation is: %s" % hashmap.get(states, 'Florida'))

print('-'*10)
print('Hawaii has: %s' % hashmap.get(cities, hashmap.get(states, 'Hawaii')))
print('Florida has: %s' % hashmap.get(cities, hashmap.get(states, 'Florida')))

print('-'*10)
hashmap.list(states)

print('-'*10)
hashmap.list(cities)

print('-'*10)
state = hashmap.get(states, 'Texas')

if not state:
    print("Sorry, no Texas")

city = hashmap.get(cities, 'TX', 'Not Entered Yet')
print("The city for the state 'TX' is: %s"% city)
