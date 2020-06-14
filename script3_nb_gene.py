# 3ème PARTIE:
# COMPTAGE DU NOMBRE EXACT DE GENES PRESENTS DANS NOS DONNEES
# EN PRENANT EN COMPTE LE DESEQUILIBRE DE LIAISON
# (car un gène peut être répété plusieurs fois)

# creation de la fonction lecture_fichier:
def lecture_fichier1(nom1,nom2):
	liste1 = []
	with open(nom1, "r") as filin1, open(nom2, "w") as filout:
		for ligne1 in filin1:
			if not ligne1.startswith("CHR"):
				ligne1 = ligne1.strip() # nettoye les bords
				ligne1 = ligne1.split() # découpe la chaine de caractères en plusieurs champs !
				if ligne1[2] not in liste1: # si le gène n'est pas présent dans la liste, il est rajouté !
					liste1.append(ligne1[2])
					filout.write(ligne1[2] + "\n")
	return liste1
	


# programme principal
fichier1 =  "data0_90_GENE.txt"
fichier2 = "Nombre_de_genes_imatinib.txt"
lecture1 = lecture_fichier1(fichier1,fichier2)
print("liste1: ", lecture1)
print("Nombre de gènes présents dans notre liste:", len(lecture1))
