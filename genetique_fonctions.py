import math
from math import sqrt
from math import sin
from math import radians

#Minimiser la portée et l'énergie
G_TERRE   =  9.81**-2

'''
Effet du ressort (en N/m)
@params
E  ->
v  ->

@return
K  -> Double -> Le ressort 
'''
def ressort(v, E):
	K = (1/3)*(E/(1-2*v))
	return K

'''
Calcul de la longueur à vide
@params
lb  -> Int -> La longueur du bras (en mètres)
lc  -> Int -> La longueur de la corde (en mètres)

@return
lv  -> Int -> Longueur à vide (en mètres)
'''
def longueur_vide(lb, lc):
	f = lb**2-((1/4)*(lc**2))
	if(f > 0):
		lv = sqrt(f)
	else:
		lv = 0
	return lv/4

'''
Calcul de la longueur du déplacement de la flèche
@params
lf	-> Int -> Longueur de la flèche (en mètres)
lv	-> Int -> Longueur à vide (en mètres)

@return
ld 	-> Int -> Longueur du déplacement
'''
def longueur_deplacement(lf, lv):
	ld = lf - lv
	#print("Longueur déplacement: " + str(ld))
	return ld

'''
La masse du projectile en Kg
@params
p   -> Int -> La masse volumique de la flèche (en kg/m3)
b   -> Int -> Base de la section du bras (en mètres)
h   -> Int -> Hauteur de la section du bras (en mètres)
lf  -> Int -> Longueur de la flèche (en mètres)

@return
mp  ->  Int ->  La masse du projectile

'''
def masse_projectile(p, bf, hf, lf):
	mp = p*bf*hf*lf
	return mp

'''
Calcul de la vélocité de la flèche
@params
K  -> -> Le ressort
ld -> -> Longueur du déplacement
mp -> -> La masse du projectile

@return
V -> -> La vélocité
'''
def velocite(K, ld, mp):
	V = sqrt((K*(ld**2))/mp)
	return V

'''
Calcul la portée du projectile
@params
V -> -> La vélocité
g -> -> gravité
a -> -> l'angle de tir

@return 
d -> La distance parcourue
'''
def portee(V, g, a):
	d = ((V**2)/g)*sin(radians(2*a))
	return d

'''
Calcul de l'énergie d'impact
@params
mp -> -> Masse du projectile
V  -> -> Vélocité

@return
ec -> -> energie d'impact
'''
def energie_impact(mp, V):
	ec = (1/2)*mp*V**2
	return ec

'''
EquivalenceJoule et gramme de TNT
@params
ec  -> -> l'énergie d'impact

@return
tnt -> -> l'équivalence de l'énergie d'impact en gramme de TNT
'''
def energie_tnt(ec):
	tnt = ec/4184
	return tnt

def calculPorteAndTNT(a, lb, b, h, bf, hf, lf, lc, p, E, v):
	g   = G_TERRE
	K   = ressort(v, E)
	lv  = longueur_vide(lb, lc)
	ld  = longueur_deplacement(lf, lv)
	mp  = masse_projectile(p, bf, hf, lf)
	V   = velocite(K, ld, mp)
	P   = portee(V, g, a)
	ec  = energie_impact(mp, V)
	tnt = energie_tnt(ec)

	return P, tnt


