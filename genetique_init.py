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
NOMBRE_GENERATION = 300

NOMBRE_GENE = 11

HAUTEUR_COUPE = 5
HAUTEUR_RANDOM_TAUX = 80
MUTATION_RANDOM_TAUX = 1

PORTEE = 500

global lstIndividu
lstIndividu = []



lstMoyenneScore = []
lstVarianceScore = []

lstMaxPortee = []
lstMaxScore  = []
lstMinScore  = []
lstScore     = []

lstTNT    = []
lstPortee = []

#Génération de la population
def generate_population():
	for i in range(0, TAILLE_POPULATION):
		individu = []
		for g in range(0, NOMBRE_GENE):
			individu.append(generateGene(g))
		
		portee, tnt = calculPorteAndTNT(individu[0], individu[1], individu[2], individu[3], individu[4], individu[5], individu[6], individu[7], individu[8], individu[9], individu[10])
		
		lstPortee.append(portee)
		lstTNT.append(tnt)		
		lstIndividu.append(individu)

		lstScore.append(evaluate(portee, tnt))

def evaluate(portee, tnt):
	lstScore  = []
	lstScoreMoyenne = []
	totalScore = 0
		individu = lstIndividu[i]

		lstPortee.append(portee)

		eval_porte = portee*100/PORTEE
		
		score = eval_porte

		#print("Portee: " + str(portee))
		#print("Score: " + str(score))
		if(limites(individu) == True or score < 0 or score > 200):
			score = 1
		elif(score > 100 and  score < 200):
			score = 100 - abs(100-score)
		else: 
			score = 1

		lstScoreMoyenne.append(int(score))
		totalScore += score
		lstScore.append(int(score))



	lstMaxPortee.append(np.mean(lstPortee))
	lstMaxScore.append(max(lstScoreMoyenne))
	lstMinScore.append(min(lstScoreMoyenne))
	moyenne = np.mean(lstScoreMoyenne)
	lstMoyenneScore.append(moyenne)

	variance = np.var(lstScoreMoyenne)
	lstVarianceScore.append(variance)

	return lstScore


'''
Tournament !
'''
def generate_couple(lstScore):	

	lstCouple = []
	couple = []
	while(len(lstCouple) != TAILLE_POPULATION/2):
		
		combattants    = []
		meilleur_score = -1
		meilleur_individu = -1

		while(len(combattants) != int(PORTEE/10)):
			
			individu_random = random.randint(0, len(lstIndividu)-1)
			
			if(individu_random not in combattants):
				combattants.append(individu_random)
				score_individu = lstScore[individu_random]
				if(score_individu > meilleur_score):
					meilleur_score = score_individu
					meilleur_individu = individu_random 

		if(len(couple) == 0 or couple[0] != lstIndividu[meilleur_individu]):
			couple.append(lstIndividu[meilleur_individu])

		if(len(couple) == 2):	
			lstCouple.append(couple)
			couple = []

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
		enfant1 = mutation(couple[0][:hauteurFirst] + couple[1][-hauteurSecond:])
		enfant2 = mutation(couple[1][:hauteurSecond] + couple[0][-hauteurFirst:])

		#Calcul de la TNT et de la Portee de l'individu
		portee1, tnt2 = calculPorteAndTNT(enfant1[0], enfant1[1], enfant1[2], enfant1[3], enfant1[4], enfant1[5], enfant1[6], enfant1[7], enfant1[8], enfant1[9], enfant1[10])
		portee2, tnt2 = calculPorteAndTNT(enfant2[0], enfant2[1], enfant2[2], enfant2[3], enfant2[4], enfant2[5], enfant2[6], enfant2[7], enfant2[8], enfant2[9], enfant2[10])

		lstPortee.append(portee1)
		lstPortee.append(portee2)

		lstTNT.append(tnt1)
		lstTNT.append(tnt2)

		#On ajoute les enfants, après la mutation
		newLstIndividu.append(enfant1)
		newLstIndividu.append(enfant2)

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
	plt.axis([0, NOMBRE_GENERATION, 0, 100])
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
	plt.title('Moyenne des portées par génération')
	plt.grid(True)


	plt.show()








