# Projet : recherche exacte et approchée d'un mot
# LIN Gérald / SINNAPPAN Alain - TD e / Groupe 10


def menu():
	print("\nSaisie d'un nouveau texte                -> (0)\nRecherche exacte d'un mot                -> (1)\nRecherche approchée d'un mot             -> (2)")
	print("Recherche d'une classe de mots           -> (3)\nRecherche approchée d'une classe de mots -> (4)\nQuitter                                  -> (5)\n")

def choice():
	choix=int(input("Entrez votre choix (0-5) : "))
	while choix<0 or choix>5:
		choix=int(input("Entrez votre choix (0-5) : "))
	return choix


#supprimer la ponctuation dans un mot, ex : "manger," devient "manger"
def supp_ponctuation(mot):
	lst=[",",".","!","?",";",":"]
	i=0
	new_mot=""
	for i in mot:         #parcourir les caractères dans le mot
		if i not in lst:  #si le caractère n'est pas une ponctuation, je le met dans une nouvelle chaîne, qui sera renvoyée à la fin
			new_mot+=i
	return new_mot


def mot_exact(mot,texte):
	pos=1              #position
	lst=texte.split()  #liste des mots du texte
	lst_pos=[]        #liste des positions du mot
	if mot=="":       #sécurité si l'user n'entre rien
		return lst_pos
	for i in lst:
		element=supp_ponctuation(i)
		if element==mot:
			lst_pos.append(str(pos))  #prendre toutes les positions du mot
		pos+=len(i)+1
	return lst_pos


####################################################
#fonction qui fait une liste avec les lettres du mot

#def transforme_lst(mot):
#	lst=[]
#	for lettre in mot:
#		lst.append(lettre)
#	return lst
####################################################


def mot_approche(mot,k,texte):
	pos=1
	lst=texte.split()
	lst_pos=[[]]
	if mot=="":       #sécurité si l'user n'entre rien
		return lst_pos
	for word in lst:                      #parcourt la liste qui contient le texte
		element=supp_ponctuation(word)    #pour chaque mot, supprime la ponctuation
		if len(element)==len(mot):        #si la longueur du mot dans la liste est de même longueur que le mot qu'on cherche
			compteur_lettre=0             #compteur de lettres différentes
			i=0                      #indice pour les lettres dans le mot
			while i<len(mot):
				if element[i]!=mot[i]:    #si la lettre du mot dans la liste ne correspond pas à la lettre du mot cherché, on incrémente 1 au compteur de lettres différentes
					compteur_lettre+=1
				i+=1
			if compteur_lettre<=k:        #une fois que le mot est parcouru, on regarde le nombre de lettres différentes
				if compteur_lettre==0:           #s'il n'y a aucune lettres différentes, on ajoute juste la position du mot
					lst_pos[0].append(str(pos))
				else:
					lst_pos.append([element,str(pos),compteur_lettre])   #s'il y a différence, on ajoute le mot et sa position en liste
		pos+=len(word)+1    #position des mots
	return lst_pos
	#à la fin, ça donne exemple : [[1 , 5 , 10],[autre, 40],[votre, 50], etc ]



def classe_menu():
	print("Choisissez :")
	print('\n1 : "x" -> un caractère de', "l'alphabet considéré")
	print("\n2 : * -> un caractère quelconque")
	print("\n3 : [caractères] -> une classe de caractères, tels les intervalles => [a,e,i,o,u] ou [A..Z]")
	print("\n4 : #C -> caractère quelconque sauf un caractère C ou d’une classe de caractères C")
	print("\n5 : arrêter")

def classe_choix():
	choix=int(input("\nEntrez votre choix ( (1-5) / (5) pour arrêter) : "))
	while choix<1 or choix>5:
		choix=int(input("Entrez votre choix ( (1-5) / (5) pour arrêter) : "))
	return choix

#fonction qui créé la "classe" du mot
def classe_mot():
	classe_menu()
	lst_car=[]          #liste de la classe du mot
	choix_car=0
	p=""                #pour le repérage
	while choix_car!=5:
		choix_car=classe_choix()
			
		if choix_car==1:
			lettre=input("Choisissez une lettre : ")
			while len(lettre)>1:               #sécurité pour qu'une lettre/caractère
				lettre=input("Choisissez une lettre : ")
			lst_car.append(lettre)
			#repérage: ###
			p+=lettre+" "
			print("Actuellement :",p)
		
		
		if choix_car==2:
			lst_car.append("*")
			#repérage: ###
			p+="* "
			print("Actuellement :",p)
		
		
		if choix_car==3:
			cl=int(input("Tapez 1 : [a,e,i,o,u] \nTapez 2 : [A..Z] \nVotre choix : "))          #variable pour choisir entre 1 ou 2
			while cl<1 or cl>2:           #sécurité
				cl=int(input("Tapez 1 : [a,e,i,o,u] \nTapez 2 : [A..Z] \nVotre choix : "))
			
			#ex : [a,e,i,o,u]
			if cl==1:
				caractere=input('Entrez vos caractères une à une ("stop" pour arrêter) : ')
				intervalle=[]                #liste de l'intervalle des lettres qui sera ajoutée à la liste de la classe de mot
				
				while caractere!="stop":
					if caractere in intervalle:             #sécurité pour empêcher une lettre en double
						print("Ce caractère est déjà enregistré !\n")
					elif (len(caractere)!=1) or (caractere in [""," "]) or not str.isalpha(caractere):          #sécurité pour n'avoir qu'une lettre et non autre caractère
						print("Réessayez.")
					else:
						intervalle.append(caractere)
					caractere=input('Entrez vos caractères une à une ("stop" pour arrêter) : ')
				if len(intervalle)>0:              #sécurité pour ne pas avoir de sous-liste vide dans la liste de classe de mot
					lst_car.append(intervalle)
					#repérage: ###
					p_tempo=",".join(intervalle)
					p+="["+p_tempo+"] "
					print("Actuellement :",p)
			
			#ex : [A..Z]
			if cl==2:
				intervalle=[]
				premier=input("Première lettre de l'intervalle : ")              #lettre du début de l'intervalle
				while not str.isalpha(premier) or len(premier)!=1:               #sécurité n°1 pour n'avoir qu'une lettre
					premier=input("Première lettre de l'intervalle : ")
				deuxieme=input("Deuxième lettre de l'intervalle : ")             #lettre de fin de l'intervalle
				while not str.isalpha(deuxieme) or len(deuxieme)!=1:             #sécurité n°2 pour n'avoir qu'une lettre aussi
					deuxieme=input("Deuxième lettre de l'intervalle : ")
				
				while ord(deuxieme)<ord(premier):                                #sécurité pour ne pas avoir un ordre inverse des lettres
					premier=input("Première lettre de l'intervalle : ")
					while not str.isalpha(premier) or len(premier)!=1:
						premier=input("Première lettre de l'intervalle : ")
					deuxieme=input("Deuxième lettre de l'intervalle : ")
					while not str.isalpha(deuxieme) or len(deuxieme)!=1:
						deuxieme=input("Deuxième lettre de l'intervalle : ")
				
				for numero in range(ord(premier),ord(deuxieme)+1):          #je regarde le "code" ASCII de la lettre de début et de fin, pour avoir l'intervalle en nombre
					intervalle.append(chr(numero))                          #j'ajoute chaque lettre grâce à son "code" ASCII à la liste intervalle
				lst_car.append(intervalle)
				#repérage: ###
				p+="["+premier+".."+deuxieme+"] "
				print("Actuellement :",p)
		
		if choix_car==4:
			cl=int(input("Tapez 1 : #C (une lettre en particulier) \nTapez 2 : #[a,e,i,o,u] \nTapez 3 : #[A..Z] \nVotre choix : "))
			while cl<1 or cl>3:   #sécurité
				cl=int(input("Tapez 1 : #C (une lettre en particulier) \nTapez 2 : #[a,e,i,o,u] \nTapez 3 : #[A..Z] \nVotre choix : "))
				
			# complément lettre (une lettre en particulier)
			if cl==1:
				lettre=input("Choisissez une lettre : ")
				while len(lettre)>1:                    #même principe, sécurité pour n'avoir qu'une lettre/caractère
					lettre=input("Choisissez une lettre : ")
				lettre_tempo="#"+lettre                 #variable temporaire (pas nécessaire) pour avoir "#" avec le caractère
				lst_car.append(lettre_tempo)
				#repérage: ###
				p+=lettre_tempo+" "
				print("Actuellement :",p)
			
			# complément, ex : #[a,e,i,o,u]
			if cl==2:
				caractere=input('Entrez vos caractères une à une ("stop" pour arrêter) : ')
				intervalle=["#"]           #le "#" permet de différencier les listes intervalles
				intervalle_tempo=[]        #liste d'intervalle temporaire pour l'esthétique à la fin
				
				while caractere!="stop":
					if caractere in intervalle:          #même principe, sécurité pour éviter les doublons
						print("Ce caractère est déjà enregistré !\n")
					elif (len(caractere)!=1) or (caractere in [""," "]) or not str.isalpha(caractere):      #sécurité pour n'avoir qu'une lettre et non autre caractère
						print("Réessayez.")
					else:
						intervalle.append(caractere)
						intervalle_tempo.append(caractere)
					caractere=input('Entrez vos caractères une à une ("stop" pour arrêter) : ')
				if len(intervalle)>1:                #sécurité pour ne pas avoir de sous-liste vide dans la liste de classe de mot
					lst_car.append(intervalle)
					#repérage: ###
					p_tempo=",".join(intervalle_tempo)
					p+="#["+p_tempo+"] "
					print("Actuellement :",p)
			
			if cl==3:
				#cf lignes précédentes (choix 3), même principe
				intervalle=["#"]
				premier=input("Première lettre de l'intervalle : ")
				while not str.isalpha(premier):
					premier=input("Première lettre de l'intervalle : ")
				deuxieme=input("Deuxième lettre de l'intervalle : ")
				while not str.isalpha(deuxieme):
					deuxieme=input("Deuxième lettre de l'intervalle : ")
					
				while ord(deuxieme)<ord(premier):
					premier=input("Première lettre de l'intervalle : ")
					while not str.isalpha(premier) or len(premier)!=1:
						premier=input("Première lettre de l'intervalle : ")
					deuxieme=input("Deuxième lettre de l'intervalle : ")
					while not str.isalpha(deuxieme) or len(deuxieme)!=1:
						deuxieme=input("Deuxième lettre de l'intervalle : ")
				
				for numero in range(ord(premier),ord(deuxieme)+1):
					intervalle.append(chr(numero))
				lst_car.append(intervalle)
				#repérage: ###
				p+="#["+premier+".."+deuxieme+"] "
				print("Actuellement :",p)
	lst_car.append(p)       #en ajoutant "p" à la liste classe de mot, on se retrouve avec ex : de base [element1, element2, etc] // avec p : [element1, element2, etc, p]
	return lst_car

def classe_recherche(lst_caractere,texte):
	pos=1
	lst_txt=texte.split()
	lst_pos=[]
	if lst_caractere==['']:      #lorsqu'il n'y a aucune saisie de l'user
		return lst_pos
	for word in lst_txt:
		element=supp_ponctuation(word)
		if len(element)==len(lst_caractere)-1:      # "-1" car il y a la variable "p" (cf lignes précédentes)
			i=0
			compteur_erreur=0
			while i<len(lst_caractere)-1:           #je parcours les caractères séléctionnés par l'user    ++++   j'ajoute "-1" car il y a la variable "p" (cf lignes précédentes)
				if len(lst_caractere[i])==1 and str.isalpha(lst_caractere[i][0]):         #si : "x" -> un caractère de l'alphabet considéré
					if element[i] not in lst_caractere[i]:                     #si le caractère dans le mot regardé ne correspond pas au caractère séléctionné, j'incrémente 1 à un compteur d'erreurs
						compteur_erreur+=1
				elif len(lst_caractere[i])>1 and lst_caractere[i][0]!="#":             #si : [caractères]
					if element[i] not in lst_caractere[i]:
						compteur_erreur+=1
				elif len(lst_caractere[i])>1 and lst_caractere[i][0]=="#":             #si : #C ou #[caractères]
					if element[i] in lst_caractere[i]:
						compteur_erreur+=1
				i+=1
			if compteur_erreur==0:          #si le compteur d'erreurs est différent de 0, c'est que le mot regardé ne correspondait pas aux critères
				lst_pos.append(str(pos))
		pos+=len(word)+1
	return lst_pos


def classe_approche(lst_caractere,k,texte):
	pos=1
	lst_txt=texte.split()
	lst_pos=[[]]
	if lst_caractere==['']:        #lorsqu'il n'y a aucune saisie de l'user
		return lst_pos
	#cf lignes précédentes, même principe
	for word in lst_txt:
		element=supp_ponctuation(word)
		if len(element)==len(lst_caractere)-1:     #rappel : "-1" car il y a la variable "p" (cf lignes précédentes)
			i=0
			compteur_erreur=0
			while i<len(lst_caractere)-1:         #rappel : "-1" car il y a la variable "p" (cf lignes précédentes)
				if len(lst_caractere[i])==1 and str.isalpha(lst_caractere[i]):
					if element[i] not in lst_caractere[i]:
						compteur_erreur+=1
				elif len(lst_caractere[i])>1 and lst_caractere[i][0]!="#":
					if element[i] not in lst_caractere[i]:
						compteur_erreur+=1
				elif len(lst_caractere[i])>1 and lst_caractere[i][0]=="#":
					if element[i] in lst_caractere[i]:
						compteur_erreur+=1
				i+=1
			if compteur_erreur<=k:
				if compteur_erreur==0:
					lst_pos[0].append(str(pos))
				else:
					lst_pos.append([element,str(pos),compteur_erreur])
		pos+=len(word)+1
	return lst_pos


############################
#                          #
#    DEBUT DU PROGRAMME    #
#                          #
############################

boucle=True
saisie="La maison du masson est massiv."

while boucle==True:
	menu()
	choix=choice()
	
	if choix==0:
		#esthétique
		print("\nVotre saisie actuelle :",saisie)
		###
		
		saisie_tempo=input('/!\ Entrez "stop" pour retourner au menu /!\ \nEcrivez votre texte : ')
		if saisie_tempo!="stop":
			saisie=saisie_tempo
	
	
	if choix==1:
		#esthétique
		print("\nVotre saisie actuelle :",saisie)
		###
		
		mot_a_trouver=input("Entrez votre mot : ")
		lst_pos=mot_exact(mot_a_trouver,saisie)
		if len(lst_pos)==0:
			print("\nLe mot",'"' +str(mot_a_trouver) +'"',"n'apparaît pas.")
		else:
			chaine_pos=", ".join(lst_pos)
			print("\nLe mot",'"' +str(mot_a_trouver) +'"',"apparaît",len(lst_pos),"fois, à la position :",chaine_pos)
	
	
	if choix==2:
		#esthétique
		print("\nVotre saisie actuelle :",saisie)
		###
		
		mot_a_trouver=input("Entrez votre mot : ")
		erreur=int(input("Choisissez à combien de lettres d'erreurs près : "))
		lst_pos=mot_approche(mot_a_trouver,erreur,saisie)
		if len(lst_pos[0])==0 and len(lst_pos)==1:
			print("\nLe mot",'"' +str(mot_a_trouver) +'"',"n'apparaît pas.")
		else:
			if len(lst_pos[0])==0:
				print("\nLe mot",'"' +str(mot_a_trouver) +'"',"n'apparaît pas.")
			else:
				chaine_pos=", ".join(lst_pos[0])
				print("\nLe mot",'"' +str(mot_a_trouver) +'"',"apparaît",len(lst_pos[0]),"fois, à la position :",chaine_pos)
			i=1
			while i<len(lst_pos):
				print("Le mot",'"' +lst_pos[i][0] +'"',"apparaît avec",lst_pos[i][2],"erreur(s), à la position :",lst_pos[i][1])
				i+=1
	
	
	if choix==3:
		#esthétique
		print("\nVotre saisie actuelle :",saisie,"\n")
		###
		
		lst_cara=classe_mot()
		lst_pos=classe_recherche(lst_cara,saisie)
		if len(lst_pos)==0:
			print("\nAucun mot de la classe",'"' +lst_cara[-1] +'"',"n'apparaît.")
		else:
			chaine_pos=", ".join(lst_pos)
			print("\nLes mots de la classe",'"' +lst_cara[-1] +'"',"apparaissent",len(lst_pos),"fois, à la position :",chaine_pos)
	
	
	if choix==4:
		#esthétique
		print("\nVotre saisie actuelle :",saisie,"\n")
		###
		
		lst_cara=classe_mot()
		erreur=int(input("Choisissez à combien de lettres d'erreurs près : "))
		lst_pos=classe_approche(lst_cara,erreur,saisie)
		if len(lst_pos[0])==0 and len(lst_pos)==1:
			print("\nAucun mot de la classe",'"' +lst_cara[-1] +'"',"n'apparaît.")
		else:
			if len(lst_pos[0])==0:
				print("\nAucun mot de la classe",'"' +lst_cara[-1] +'"',"n'apparaît.")
			else:
				chaine_pos=", ".join(lst_pos[0])
				print("\nLes mots de cette classe",'"' +lst_cara[-1] +'"',"apparaissent",len(lst_pos[0]),"fois, à la position :",chaine_pos)
			i=1
			while i<len(lst_pos):
				print("Le mot",'"' +lst_pos[i][0] +'"',"apparaît avec",lst_pos[i][2],"erreur(s), à la position :",lst_pos[i][1])
				i+=1
	
	
	if choix==5:
		boucle=False
		print("Vous quittez le programme.\n")


##########################
#                        #
#    FIN DU PROGRAMME    #
#                        #
##########################
