<h2>Scorpion - Algorithme génétique</h2>

<div>
<p>Création d'un algorithme génétique pour apprendre à un Scorpion à tirer à une certaine distance</p>
<p>4 fichiers sont présents dans le dépôt : </p>
  <ul>
	<li><b>génétique_fonctions</b> : correspond à toutes les fonctions de physique qui vont permettre de calculer la portée et la puissance de tir de l'individu</li>
	<li><b>genetique_individu</b> : toutes les caractérisiques, génération et modification des gènes d'un individu.</li>
	<li><b>genetique_limites</b> : vérification des caractéristiques de l'individu pour savoir si il va pouvoir tirer.</li>
	<li><b>genetique_init</b> : le fichier principal qui contient toutes les phases de l'algorithme génétique. C'est dans celui-ci qu'on aura le nombre de génération, la taille de la population, le pourcentage de chance d'avoir une mutation ou encore le pourcentage de chance que la coupe des gènes soit modifié.</li>
    </ul>
</div>
  
Les variables ont initialement les valeurs suivantes : 
<table>
	<tr><td>TAILLE_POPULATION</td><td>150</td></tr>
	<tr><td>NOMBRE_GENERATION</td><td>300</td></tr>
	<tr><td>HAUTEUR_COUPE</td><td>5</td></tr>
	<tr><td>HAUTEUR_RANDOM_TAUX</td><td>80</td></tr>
	<tr><td>MUTATION_RANDOM_TAUX</td><td>1</td></tr>
	<tr><td>PORTEE</td><td>300</td></tr>
</table>

<div>
<p>Pour lancer l'algorithme il suffit de lancer la commande suivante : <b>python genetique_init.py</b>
<div>
