awesome_couples = {
    'Batman': 'Robin',
    'Harley Quinn': 'Poison Ivy',
    'Iron man': 'War machine',
    'Phenix' : 'Cyclope',
    'Bob sponge square': 'Patrick'
    }

a = awesome_couples['Phenix']
bob = 'Bob sponge square'
b = (bob, 'Patrick starfish') in awesome_couples

awesome_couples['Ant man'] = 'the Wasp'

del awesome_couples['Bob sponge square']

c = bob in awesome_couples
d = awesome_couples.get(bob, 'unknown')
e = awesome_couples.get('Ant man', 'toto')

print (a,b,c,d,e)