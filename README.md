## Projet OpenClassrooms
## Projet 4 Développez un programme logiciel en Python

###Description du projet :
L'application propose une gestion de tournois d'Echecs. Elle permet :

- D'inscrire des joueurs
- De générer des tournois composés de 4 tours
- De saisir les scores pour chaque tour
- D'afficher le classement des joueurs

### Récupérer le projet :

```
git clone https://github.com/ydjabela/Projet_4_Openclassrooms
```

### Création de l'environnement virtuel

Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_4
```

### Activation de l'environnement virtuel du projet

Windows :

```
Projet_4\Scripts\activate.bat
```

MacOS/Linux :
```
source Projet_4/bin/activate
```

### Installation des packages necessaire pour ce projet
```
pip install -r requirements.txt
```

### Exécuter le scripts:

#### pour exécuter le scraper complet

Pour lancer le projet : ``` python main.py  ``` et laissez-vous guider !

###Utilisation
####Le menu principal est divisé en 4 options.
1) Gestion des joueurs:
Cette option vous permet de gérer les joueurs
- Ajouter un joueur.
- Modifier un joueur (modifier le nom, prénom, age, sex ou classement).
- Afficher les joueurs.
- Afficher les joueurs par classement ou bien par ordre alphabétique.
- Supprimer un joueur.
- Supprimer tous les joueurs.
- Revenir au menu principal.
- Quitter le script.

2) Gestion des tournois :
Cette option vous permet de gérer les tournois.
- Ajouter un tournoi.
- Modifier un tournoi (modifier le nom, lieu, date, joueurs, nombre de tours ou description ou classement).
- Afficher les Tournois.
- Supprimer un tournoi.
- Supprimer tous les tournois.
- Revenir au menu principal.
- Quitter le script.

3) Lancer une partie :
- Le programme vous permet de gérer des tournois d'échecs. Lors de la première utilisation,
- Si aucun joueur n'est présent dans la base de données, vous serez invité à en créer. (8)
- si y en moins de 8 joueurs il vous demandera d'ajouter jusqu'a avoir 8 joueurs.
- S'il existe plus de 8 joueurs, il vous permettra de sélectionner 8 joueurs.
- Si aucun tournoi n'est présent dans la base de donnée, vous serez invité à en créer.
- S'il existe plusieurs tournois, il vous permettra de sélectionner 1 tournoi.
- Lors d'un tournoi, vous serez invité à rentrer les résultats après chaque match. A la fin d'un tournoi, un classement sera généré.
5) Quittez le programme.

### Mise en forme du code :
Le code est mis en forme selon de modèle MVC.

#### Controller:
controller.py

#### Model (one per class) :
- model_tournament.py
- model_player.py
- model_match.py
- database.py

#### View:
- view_tournament.py
- view_player.py
- principal_view.py
#### settings
#### base de donnée json

#### Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
```
pip install -r requirements.txt
```
###Vérifier la qualité du code :
Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela 
- Stephane Didier

