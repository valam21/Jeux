print("Salut ce jeu consiste à deviner le nombre gagnant compris de 0 à 100")
answer = input("Voulez-vous continuez ? ")
if answer.lower() == "oui":
    import random
    nb_choisir = random.randint(1, 100)
    print("C'est parti pour 10 chance ")
    nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
    nb_chance = 9
    while nb_choisir != int(nb_devine) and nb_chance >= 1:
        if nb_choisir > int(nb_devine):
            print("Le nombre que vous cherchez est supérieur à " + nb_devine)
            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
        else:
            print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
        nb_chance = nb_chance - 1
    if nb_chance <= 1:
        print("Vous avez perdu !")
    if nb_choisir == int(nb_devine):
        print("Vous avez gagné !")
        print("C'est bien, vous vous débroullez correctement ")
        choix = input("voulez-vous passer à l'étape suivante ? : ")
        if choix.lower() == "oui":
            import random
            nb_choisir = random.randint(1, 100)
            print("C'est parti pour 8 chance ")
            nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
            nb_chance = 7
            while nb_choisir != int(nb_devine) and nb_chance >= 1:
                if nb_choisir > int(nb_devine):
                    print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                else:
                    print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                nb_chance = nb_chance - 1
            if nb_chance <= 1:
                print("Vous avez perdu !")
            if nb_choisir == int(nb_devine):
                print("Super, vous avez gagné !")
                choix = input("voulez-vous passer à l'étape suivante ? : ")
                if choix.lower() == "oui":
                    import random
                    nb_choisir = random.randint(1, 100)
                    print("C'est parti pour 7 chance ")
                    nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                    nb_chance = 6
                    while nb_choisir != int(nb_devine) and nb_chance >= 1:
                        if nb_choisir > int(nb_devine):
                            print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                        else:
                            print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                        nb_chance = nb_chance - 1
                    if nb_chance <= 1:
                        print("Vous avez perdu !")
                    if nb_choisir == int(nb_devine):
                        print("Super, vous avez gagné !")
                        choix = input("voulez-vous passer à l'étape suivante ? : ")
                        if choix.lower() == "oui":
                            import random
                            nb_choisir = random.randint(1, 100)
                            print("C'est parti pour 6 chance ")
                            nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                            nb_chance = 5
                            while nb_choisir != int(nb_devine) and nb_chance >= 1:
                                if nb_choisir > int(nb_devine):
                                    print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                                else:
                                    print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                                nb_chance = nb_chance - 1
                            if nb_chance <= 1:
                                print("Vous avez perdu !")
                            if nb_choisir == int(nb_devine):
                                print("Félicitation, vous avez gagné !")
                                choix = input("voulez-vous passer à l'étape suivante ? : ")
                                if choix.lower() == "oui":
                                    import random
                                    nb_choisir = random.randint(1, 100)
                                    print("C'est parti pour 5 chance ")
                                    nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                                    nb_chance = 4
                                    while nb_choisir != int(nb_devine) and nb_chance >= 1:
                                        if nb_choisir > int(nb_devine):
                                            print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                                        else:
                                            print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                                        nb_chance = nb_chance - 1
                                    if nb_chance <= 1:
                                        print("Vous avez perdu !")
                                    if nb_choisir == int(nb_devine):
                                        print("Super, vous avez gagné !")
                                        choix = input("voulez-vous passer à l'étape suivante ? : ")
                                        if choix.lower() == "oui":
                                            import random
                                            nb_choisir = random.randint(1, 100)
                                            print ("C'est parti pour 4 chance ")
                                            nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                                            nb_chance = 3
                                            while nb_choisir != int(nb_devine) and nb_chance >= 1:
                                                if nb_choisir > int(nb_devine):
                                                    print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                                                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                                                else:
                                                    print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                                                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                                                nb_chance = nb_chance - 1
                                            if nb_chance <= 1:
                                                print("Vous avez perdu !")
                                            if nb_choisir == int(nb_devine):
                                                print("Géniale, vous avez gagné !")
                                                choix = input("voulez-vous passer à l'étape suivante ? : ")
                                                if choix.lower() == "oui":
                                                    import random
                                                    nb_choisir = random.randint(1, 100)
                                                    print("C'est parti pour 3 chance ")
                                                    nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                                                    nb_chance = 2
                                                    while nb_choisir != int(nb_devine) and nb_chance >= 1:
                                                        if nb_choisir > int(nb_devine):
                                                            print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                                                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                                                        else:
                                                            print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                                                            nb_devine =input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                                                        nb_chance = nb_chance - 1
                                                    if nb_chance <= 1:
                                                        print("Vous avez perdu !")
                                                    if nb_choisir == int(nb_devine):
                                                        print("Super, vous avez gagné !")
                                                        choix = input("voulez-vous passer à l'étape suivante ? : ")
                                                        if choix.lower() == "oui":
                                                            import random
                                                            nb_choisir = random.randint(1, 100)
                                                            print("C'est parti pour 2 chance ")
                                                            nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                                                            nb_chance = 1
                                                            while nb_choisir != int(nb_devine) and nb_chance >= 1:
                                                                if nb_choisir > int(nb_devine):
                                                                    print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                                                                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                                                                else:
                                                                    print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                                                                    nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                                                                nb_chance = nb_chance - 1
                                                            if nb_chance <= 1:
                                                                print("Vous avez perdu !")
                                                            if nb_choisir == int(nb_devine):
                                                                print("Super, vous avez gagné !")
                                                                choix = input("voulez-vous passer à l'étape suivante ? : ")
                                                                if choix.lower() == "oui":
                                                                    import random
                                                                    nb_choisir = random.randint(1, 100)
                                                                    print("C'est parti pour 1 chance ")
                                                                    nb_devine = input("D'evinez le nombre gagnant compris de 0 à 100 : ")
                                                                    nb_chance = 0
                                                                    while nb_choisir != int(nb_devine) and nb_chance >= 1:
                                                                        if nb_choisir > int(nb_devine):
                                                                            print("Le nombre que vous cherchez est supérieur à " + nb_devine)
                                                                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix : ")
                                                                        else:
                                                                            print("Le nombre que vous cherchez est inférieur à " + str(nb_devine))
                                                                            nb_devine = input("IL vous reste " + str(nb_chance) + " chance. Faite encore votre choix :")
                                                                        nb_chance = nb_chance - 1
                                                                    if nb_chance <= 1:
                                                                        print("Vous avez perdu !")
                                                                    if nb_choisir == int(nb_devine):
                                                                        print("Vous etes un expert !")