name1 = input("Entrez le nom du 1er joueur : ").capitalize()
pv1 = int(input("Et son nombre de PV : "))
name2 = input("Entrez le nom du 2ème joueur : ").capitalize()
pv2 = int(input("Et son nombre de PV : "))
# noinspection PyInterpreter
message = name1 + " ( " + str(pv1) + " PV ) affronte " + name2 + " ( " + str(pv2) + " PV )"
print()
print("+" * (len(message)+4))
print("+", message, '+')
print("+" * (len(message)+4))
print()
quest1 = name1 + " combien, de dégats infligez-vous à " + name2 + " ? : "
answer1 = int(input(quest1))
message1 = name1 + " attaque " + name2 + " qui pert " + str(answer1) + " PV"
new_pv2 = abs(pv2 - answer1)
mess_new_pv2 = name2 + " a maintenant " + str(new_pv2) + " PV"
max_size1 = max(len(message1), len(mess_new_pv2))
print()
print("+" * (max_size1 + 4))
print("+ " + message1 + " " * abs(int(str(max_size1 - len(message1)))) + " +")
print("+ " + mess_new_pv2 + " " * abs(int(str(max_size1 - len(mess_new_pv2)))) + " +")
print("+" * (max_size1 + 4))
print()
quest2 = name2 + " combien, de dégats infligez-vous à " + name1 + " ? : "
answer2 = int(input(quest2))
message2 = name2 + " attaque " + name1 + " qui pert " + str(answer2) + " PV"
new_pv1 = + abs(pv1 - answer2)
mess_new_pv1 = name1 + " a maintenant " + str(new_pv1) + " PV"
max_size2 = max(len(message2), len(mess_new_pv1))
print()
print("+" * (max_size2 + 4))
print("+ " + message2 + " " * int(str(max_size2 - len(message2))) + " +")
print("+ " + mess_new_pv1 + " " * int(str(max_size2 - len(mess_new_pv1))) + " +")
print("+" * (max_size2 + 4))
print()
result = "Résultat du combat pour les deux joueurs : "
result_name1 = name1 + " a " + str(new_pv1) + " PV"
result_name2 = name2 + " a " + str(new_pv2) + " PV"
max_size3 = max(len(result), len(result_name1), len(result_name2))
print("+" * (max_size3 + 4))
print("+ " + result + " " * int(str(max_size3 - len(result))) + " +")
print("+ " + result_name1 + " " * int(str(max_size3 - len(result_name1))) + " +")
print("+ " + result_name2 + " " * int(str(max_size3 - len(result_name2))) + " +")
print("+" * (max_size3 + 4))


