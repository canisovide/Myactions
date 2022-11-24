import sys
def sub_string(mot="eneam", cle="eneam"):
    while mot.__len__() == 1:
        mot = str(input("Entrez une chaîne de caractères :"))
    mot = list(mot.upper())
    mot_crypte = []
    if len(cle) == 1:
        cle = cle.upper()
        cle = ord(cle) - 65
        for letter in mot:
            if letter in [" ", "  ", "/t", "'", ",", '"']:
                mot_crypte.append(letter)
            else:
                letter = ord(letter) + cle

                if letter > 90:
                    letter = letter - 26
                mot_crypte.append(chr(letter))
    else:
        cle = list(cle.upper())
        j = 0
        for i, letter in enumerate(mot):
            # print(j)
            if letter in [" ", "  ", "\t", "'", ",", '"', ".", ";", ":", "...","(", ")", "[", "]"]:
                mot_crypte.append(letter)
            else:
                code = ord(cle[j]) - 65
                letter = ord(letter) + code
                if letter > 90:
                    letter = letter - 26
                mot_crypte.append(chr(letter))
                if j == len(cle) - 1:
                    j = 0
                else:
                    j += 1

    return "".join([letter for letter in mot_crypte])


def sub_fichier(fichier, cle):
    with open(fichier, "r") as file, open("resultats.txt", "w") as filout:
        for mot in file:
            mot = mot.strip()
            mot = sub_string(mot,cle)
            filout.write("* " + mot + "\n")


sub_fichier(sys.argv[1], sys.argv[2])

print("{}".format('Le message à été bien chiffré'))
