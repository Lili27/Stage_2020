# 1ère PARTIE:
#RECUPERATION DES DONNEES AVEC LES RS CORRESPONDANT A NOS SNP COMMUNS ENTRE LES 2 FICHIERS

# création de 2 fonctions lectures_fichier:
# lecture du 1er fichier et une liste de créer avec les données du fichier1
def lecture_fichier1(nom1):
	liste1 = []
	with open(nom1,"r") as filin1:
		for ligne1 in filin1:
			if not ligne1.startswith("CHR"):
				ligne1 = ligne1.strip() # nettoye les bords
				ligne1 = ligne1.split() # découpe la chaine de caractères en plusieurs champs !
				liste1.append(ligne1) # ajoute la ligne à la liste1
	return liste1

# lecture du 2e fichier et la liste contenant ces données
def lecture_fichier2(nom2):
	liste2= []
	with open(nom2,"r") as filin2:
		for ligne2 in filin2:
			ligne2 = ligne2.strip() # nettoye les bords
			ligne2 = ligne2.split() # découpe la chaine de caractères en plusieurs champs !
			liste2.append(ligne2) # ajoute la ligne à la liste2
	return liste2


# comparaison des 2 listes ainsi créent et donc recherche des SNPs présents dans le fichier data0_90.txt
# et voir si on les retrouve dans le fichier all_chr_SNPs_only_prop.txt 
# si c'est le cas, on notera les informations correponsdantes dans le nouveau fichier data0_90_RS.txt /// 
def comparaison_data(lecture1,lecture2):
	with open("data0_90_RS.txt","w") as filout:
		filout.write("CHR"+"\t"+"RS"+"\t"+"NMISS"+"\t"+ "OR"+"\t"+ "P"+"\t"+ "LOG"+"\n")
		for i in range(len(lecture1)):
			for j in range(len(lecture2)):
				if str(lecture1[i][1]) == str(lecture2[j][0]): 
					filout.write(lecture1[i][0]+"\t"+lecture2[j][1]+"\t"+ lecture1[i][5] +"\t"+ lecture1[i][6] +"\t"+ lecture1[i][8] + "\t" + lecture1[i][9]+"\n")
	return "data0_90_RS.txt"


# programme principal
fichier1 = "data0_90.txt"
fichier2 = "all_chr_SNPs_only_prop.txt"
lecture1 = lecture_fichier1(fichier1)
print(lecture1)
lecture2 = lecture_fichier2(fichier2)
print(lecture2[0])
print("deuxieme fonciton faite!")
comparaison = comparaison_data(lecture1, lecture2)
print(comparaison)
