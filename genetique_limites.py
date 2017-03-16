import genetique_individu
from genetique_individu import getGene

import genetique_fonctions
from genetique_fonctions import ressort
from genetique_fonctions import longueur_vide
from genetique_fonctions import longueur_deplacement


def moment_quadratique(b, h):
	I = (b*(h**3))/12
	return I


def force_traction(K, ld):
	F = K*ld
	return F


def fleche_max(b, h, K, ld, lb, E):
	I = moment_quadratique(b, h)
	F = force_traction(K, ld)
	f = (F*(lb**3))/(48*E*I)
	return f

def limites(individu):
	lb = getGene(individu, 1) 
	b  = getGene(individu, 2)
	h  = getGene(individu, 3)
	lf = getGene(individu, 6)
	lc = getGene(individu, 7)
	E  = getGene(individu, 9)
	v  = getGene(individu, 10)

	K  = ressort(v, E)
	lv = longueur_vide(lb, lc)
	ld = longueur_deplacement(lf, lv)

	f  = fleche_max(b, h, K, ld, lb, E)

	if(ld > f):
		return False
	elif(lv > lf):
		return True
	elif(lc > lb):
		return True
	else:
		return False

