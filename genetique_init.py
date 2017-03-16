import matplotlib.pyplot as plt
import numpy as np
import random

import math


import genetique_fonctions
from genetique_fonctions import calculPorteAndTNT

import genetique_individu
from genetique_individu import generateGene

import genetique_limites
from genetique_limites import limites

#CONSTANTES
G_TERRE   =  9.81
G_LUNE    =  1.62
G_JUPITER = 24.80

g = G_TERRE

TAILLE_POPULATION = 150
NOMBRE_GENERATION = 200

NOMBRE_GENE = 11

HAUTEUR_COUPE = 5
HAUTEUR_RANDOM_TAUX = 75
MUTATION_RANDOM_TAUX = 0

OFFSET = 500
PORTEE = 300

global lstIndividu
lstIndividu = []

#Génération de la population
def generate_population():
	for i in range(0, TAILLE_POPULATION):
		individu = []
		for g in range(0, NOMBRE_GENE):
			individu.append(generateGene(g))

		lstIndividu.append(individu)

lstMoyenneScore = []
lstVarianceScore = []

lstMaxPortee= []
lstMaxTnt   = []
lstMaxScore = []
lstMinScore = []

def evaluate():
	lstPortee = []
	lstTNT = []
	lstScore  = []
	lstScoreMoyenne = []
	totalScore = 0

	for individu in lstIndividu:
		portee, tnt = calculPorteAndTNT(individu[0], individu[1], individu[2], individu[3], individu[4], individu[5], individu[6], individu[7], individu[8], individu[9], individu[10])

		lstPortee.append(portee)
		lstTNT.append(tnt)

	MAX_TNT = max(lstTNT)
	for i in range(0, len(lstPortee)):
		eval_porte = int(lstPortee[i]*100/PORTEE)
		eval_tnt   = int(lstTNT[i]*100/MAX_TNT)
		
		score = (eval_porte + eval_tnt)
		if(limites(individu) == True):
			score = 0.01

		lstScoreMoyenne.append(int(score))
		totalScore += score
		lstScore.append(int(totalScore))



	lstMaxPortee.append(max(lstPortee))
	lstMaxTnt.append(max(lstTNT))
	lstMaxScore.append(max(lstScoreMoyenne))
	lstMinScore.append(min(lstScoreMoyenne))
	moyenne = np.mean(lstScoreMoyenne)
	lstMoyenneScore.append(moyenne)

	variance = np.var(lstScoreMoyenne)
	lstVarianceScore.append(variance)

	return lstScore

def generate_couple(lstScore):
	scoreMax = lstScore[len(lstScore)-1]
	lstCouple = []
	offset = random.randint(0, 100)%scoreMax
	tmp = 0
	i = 0

	while(len(lstCouple) != TAILLE_POPULATION/2):
		couple = []
		while(len(couple) != 2):
			#print(str(tmp) + " < " + str(offset) + " < " + str(lstScore[i]))
			if(tmp <= offset and offset <= lstScore[i]):
				if(len(couple) == 0 or couple[0] != lstIndividu[i]):
					couple.append(lstIndividu[i])


			tmp = lstScore[i]
			i += 1
			if(i == len(lstScore) - 1):
				tmp = 0
				i   = 0
				offset = (offset+OFFSET)%scoreMax			
		lstCouple.append(couple)

	return lstCouple


def create_enfant(lstCouple):

	newLstIndividu = []
	for couple in lstCouple:
		randomHauteur = random.randint(0, 100)
		if(randomHauteur <= HAUTEUR_RANDOM_TAUX):
			hauteurFirst = random.randint(1, NOMBRE_GENE-1)
			hauteurSecond = NOMBRE_GENE - hauteurFirst
		else:			
			hauteurFirst = HAUTEUR_COUPE
			hauteurSecond = NOMBRE_GENE - HAUTEUR_COUPE

		#On définit nos deux enfants par rapport à la coupe de base
		enfant1 = couple[0][:hauteurFirst] + couple[1][-hauteurSecond:]
		enfant2 = couple[1][:hauteurSecond] + couple[0][-hauteurFirst:]

		#On ajoute les enfants, après la mutation
		newLstIndividu.append(mutation(enfant1))
		newLstIndividu.append(mutation(enfant2))

	return newLstIndividu

def mutation(enfant):
	randomMutation = random.randint(0, 100)
	if(randomMutation <= MUTATION_RANDOM_TAUX):
		randomGene = random.randint(0, NOMBRE_GENE-1)
		enfant[randomGene] = generateGene(randomGene)
	return enfant




if __name__ == "__main__":
	generate_population()

	for generation in range(1, NOMBRE_GENERATION+1):

		print("#------------GENERATION "+ str(generation) +" ------------#")

		lstScore = evaluate()
		lstCouple = generate_couple(lstScore)
		lstIndividu = create_enfant(lstCouple)

	#Création des différents graphiques:
	plt.figure(1)

	#Moyenne
	plt.subplot(221)
	t = np.arange(0, NOMBRE_GENERATION, 1)
	plt.plot(t, lstMoyenneScore)
	plt.axis([0, NOMBRE_GENERATION, 0, 200])
	plt.title('Moyenne des scores')
	plt.grid(True)

	#Variance
	if(len(lstVarianceScore) != NOMBRE_GENERATION):
		print("Taille variance: " + str(len(lstVarianceScore)) + " - Erreur")
	else:
		plt.subplot(222)
		u = np.arange(0, NOMBRE_GENERATION, 1)
		plt.plot(u, lstVarianceScore)
		plt.axis([0, NOMBRE_GENERATION, 0, 1000])
		plt.title('Variance des scores')
		plt.grid(True)

	#Score maximum
	plt.subplot(223)
	plt.plot(t, lstMaxScore, t, lstMinScore)
	plt.axis([0, NOMBRE_GENERATION, 0, 200])
	plt.title('Le score max/min par génération')
	plt.grid(True)

	#Affichage de la portee
	plt.subplot(224)
	plt.plot(t, lstMaxPortee)
	plt.axis([0, NOMBRE_GENERATION, 0, PORTEE*2])
	plt.title('Meilleur portée par génération')
	plt.grid(True)


	plt.show()








