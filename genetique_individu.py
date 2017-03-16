import random

#Angle entre 0° et 90°
def generateAngle():
	return random.randint(0, 90)

#Longueur du bras entre 1m et 5m
def generateLongueurBras():
	return random.randint(1000, 5000)/100

#Base du bras entre 0.5m et 3m
def generateBase():
	return random.randint(50, 3000)/100

def generateHauteur():
	return random.randint(50, 3000)/100

def generateBaseFleche():
	return random.randint(20, 1000)/100

def generateHauteurFleche():
	return random.randint(20, 1000)/100

#Longueur de la flèche entre 0.1m et 3m
def generateLongueurFleche():
	return random.randint(100, 3000)/100

#Longueur de la corde entre 0.1m et 3m
def generateLongueurCorde():
	return random.randint(100, 3000)/100

def generateMasseVolumique():
	return random.randint(1, 25000) #La masse volumique de la flèche, plus elles grande, plus le matériau est solide
		
def generateYoung():
	return random.randint(1, 1500)  #Le module de Young du matériau

def generateCoeffPoisson():
	return random.randrange(1, 50)/100

def generateGene(g):
	if(g == 0):
		return generateAngle()
	elif(g == 1):
		return generateLongueurBras()
	elif(g == 2):
		return generateBase()
	elif(g == 3):
		return generateHauteur()
	elif(g == 4):
		return generateBaseFleche()
	elif(g == 5):
		return generateHauteurFleche()
	elif(g == 6):
		return generateLongueurFleche()
	elif(g == 7):
		return generateLongueurCorde()
	elif(g == 8):
		return generateMasseVolumique()
	elif(g == 9):
		return generateYoung()
	elif(g == 10):
		return generateCoeffPoisson()
	else:
		print("Erreur - Le gène numéro " + str(g) + " est inexistant")
		return None

def getGene(individu, g):
	return individu[g]
