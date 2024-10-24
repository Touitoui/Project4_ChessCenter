# Chess Tournament Manager

Une application Python en ligne de commande pour la gestion de tournoi d'échecs. Cette application permet aux organisateurs de:
- Créer de nouveaux tournois
- Organiser des tournois avec la gestion du score
- Créer et gerer des joueurs
- Suivit du score et des matches
- Voir l'historique des tournois


## Prérequis

- Python 3.9+
- pip (Python package installer)

## Installation

1. Cloner le repository:
```bash
git clone https://github.com/yourusername/chess-tournament-manager.git
cd chess-tournament-manager
```

2. Créer et activer un environnement virtuel (recommandé):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Installer les dépendances:
```bash
pip install -r requirements.txt
```

## Utilisation

1. Démarrer l'application:
```bash
python main.py
```

2. Options du menu principal:
   - **Nouveau tournoi**: Crée un nouveau tournoi
   - **Charger tournoi**: Charge un tournoi existant (Affichera le résumé si le tournoi est déjà terminé)
   - **Info tournoi**: Détails sur les differents tournois, en cours ou terminé
   - **Afficher les joueurs**: Affiche les informations des differents joueurs
   - **Créer joueur**: Ajoute un nouveau joueur à la base de donnée
   - **Quitter**: Quitte l'application

3. Créer un Tournoi:
   - Entrer les informations du tournoi (Nom, Lieu, Date)
   - Selectionner les participants
   - Définir le nombre de rounds (4 par default)
   - Entrer les résultat des matches au fur et à mesure

4. Gestion des joueurs:
   - Les joueurs sont identifié par leur nom/prénom et leur ID de Club
   - Les IDs de Club sont au format : AB12345 (2 lettres + 5 chiffres)
   - Les informations de joueurs sont enregistré de façon persistante dans des fichiers json

## Stoquage des données

L'application créera au besoin le dossier `data` pour stoquer ses données, ainsi que deux sous-dossiers:
- `data/players/`: Stoque les information des joueurs au format JSON
- `data/tournaments/`: Stoque les information des tournois au format JSON

## Code Quality

Pour générer un rapport Flake8:

1. Installer Flake8:
```bash
pip install flake8
```

2. Lancer Flake8:
```bash
flake8 --output-file=flake8_report.txt --statistics --count
```

3. Voir le rapport dans `flake8_report.txt`

## Structure du Projet

```
chess-tournament-manager/
│
├── app/
│   ├── controller/
│   │   ├── player_controller.py
│   │   └── tournament_controller.py
│   ├── model/
│   │   ├── match.py
│   │   ├── player.py
│   │   ├── tournament.py
│   │   └── turn.py
│   ├── view/
│   │   ├── match_view.py
│   │   ├── menu_view.py
│   │   ├── player_view.py
│   │   └── tournament_view.py
│   └── tools/
│       ├── inquirer_tools.py
│       └── utils.py
│
├── data/
│   ├── players/
│   └── tournaments/
│
├── main.py
├── requirements.txt
└── README.md
```

## Formatage des données
Les données joueur étant sauvegardé dans des fichiers JSON simple, ceux-ci peuvent être exporté/importé, et modifié manuellement au besoin.

### Player JSON Format:
```json
{
    "id": 1,
    "last_name": "Smith",
    "first_name": "John",
    "birthdate": "15/03/1990",
    "club_id": "AB12345"
}
```

