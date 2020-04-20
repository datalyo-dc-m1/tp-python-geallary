from random import randint

#help (randint)

number_to_guess = randint(1,10)
print (f"le nombre à deviner : {number_to_guess}")

has_won = False
user_propal = int(input('Rentrez un nombre entre 1 et 10 '))

while has_won == False:
    while user_propal < 0 or user_propal > 10:
        print ('Vous n avez pas saisi un nombre entre 1 et 10')
        user_propal = int(input('Rentrez un nombre entre 1 et 10 '))

        if user_propal != number_to_guess:
            print('c est pas ca')
        else:
            has_won = True
            print('GG')


