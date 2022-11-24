# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# base = list(alphabet)
# cryte = []
# cle = 'L'
# mot = "Bonjour"
# mot = mot.upper()
# liste = []
# for i, letter in enumerate(range(ord(cle), 116)):
#     if letter > 90:
#         letter = letter - 26
#     letter = chr(letter)
#     liste.append(letter)
#
#     if i == 25:
#         break
#
# for letter in mot:
#     for j in range(len(base)):
#         if letter == base[j]:
#             cryte.append(liste[j])
#
# print(cryte)
#
# mot_crypte = "".join(cryte)
# print(mot_crypte)
# def sub_cryt(mot="Bonjour", cle="A"):
#     cle, mot = cle.upper(), mot.upper()
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     base = list(alphabet)
#     liste = []
#     crypte = []
#     for i, letter in enumerate(range(ord(cle), 116)):
#         if letter > 90:
#             letter = letter - 26
#         letter = chr(letter)
#         liste.append(letter)
#         if i == 25:
#             break
#     for letter in mot:
#         for j in range(len(base)):
#             if letter == base[j]:
#                 crypte.append(liste[j])
#     return "".join([letter for letter in crypte])
#
#
# print(sub_cryt("eneam", "d"))
#
#
# def sub_ascii(mot="eneam", cle="D"):
#     cle = cle.upper()
#     cle = ord(cle) - 65
#     mot = list(mot.upper())
#     mot_crypte = []
#     for letter in mot:
#         letter = ord(letter) + cle
#         if letter > 90:
#             letter = letter - 26
#         mot_crypte.append(chr(letter))
#
#     return "".join([letter for letter in mot_crypte])
#
#
# print(sub_ascii())

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

mot = str(input("Entrez une chaîne de caractères :")).strip()
cle = str(input("Entrez une clé :")).strip()
print(sub_string(mot, cle))
