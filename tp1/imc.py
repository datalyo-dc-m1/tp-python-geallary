taille_saisie= float (input('saisir une taille (en m) '))
poids_saisie= float (input('saisir une poids (en kg) '))

imc = float(poids_saisie/(taille_saisie*taille_saisie))
print ("%.2f" % imc)

imcDescription = bool

if imc < 18.5:
    imcDescription = "vous êtes en état de maigreur"
elif imc > 18.5:
    imcDescription = "vous êtes normal"
elif imc > 24.9:
    imcDescription = "vous êtes en état de surpoids"
elif imc > 29.9:
    imcDescription = "vous êtes en état d obésité"
elif imc > 40:
    imcDescription = "vous êtes en état d obésité massive"

    print (imcDescription)






