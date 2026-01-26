# Projet-Big_Data

## Idée

Faire un shazam maison. Le but du projet est de créer un shazam, où a partir d'un fichier audio, on doit retrouver la musique la plus proche grace à une base de donnée vectorielle de musiques.

## À faire

1. trois articles de recherche à trouver et à lire par personne.
2. Faire le projet.
3. Faire un rapport.

## Comment démarrer le projet

1. Importer le projet sur sa machine.
2. Créer un venv :

```bash
    python3 -m venv venv
    # Activation du venv
    source venv/bin/activate
    # Vérification de l'activation du venv
    which python
```

3. Installer les librairies necessaires pour l'éxécution du projet :

```bash
    pip install -r requirements.txt
```

## Ajout d'une librairie

1. On utilise pip pour installer la librairie qu'on souhaite (Il faut bien vérifier qu'on se situe dans le venv).
2. Puis on fait la commande :

```bash
    pip freeze > requirements.txt
    # Cette commande permet de mettre à jour les librairies nécessaires pour éxecuter le code du projet.
```

## Structure du projet

```
shazam-maison/
├── README.md                  # Présentation du projet, comment lancer
├── requirements.txt           # Dépendances Python
├── .gitignore

├── data/                      # Les données du projet
│   ├── raw/                   # Audios bruts (les datasets téléchargés)
│   ├── processed/             # Audios nettoyés / segments
│   ├── features/              # Descripteurs / empreintes / embeddings
│   └── index/                 # Fichiers de la base vectorielle

├── src/
│   ├── __init__.py
│   ├── config.py              # Chemins de fichiers, hyperparamètres simples

│   ├── data_utils/            # Gestion des données
│   │   ├── __init__.py

│   ├── audio/                 # Tout ce qui touche au signal audio
│   │   ├── __init__.py
│   │   ├── loading.py         # Chargement audio, resampling, mono, etc.
│   │   └── preprocessing.py   # Normalisation, découpe en fenêtres, etc.

│   ├── features/              # Représentations numériques de l’audio
│   │   ├── __init__.py

│   ├── index/                 # Base de données vectorielle
│   │   ├── __init__.py
│   │   └── build_index.py     # Script pour construire et mettre à jour l’index

│   ├── retrieval/             # Pipeline pour répondre à une requête
│   │   ├── __init__.py

│   └── api/                   # Interface simple pour tester le Shazam
│       ├── __init__.py
│       └── app.py             # Petitte API pour envoyer un audio et recevoir le résultat

├── scripts/                   # Scripts à lancer depuis le terminal

└── tests/                     # Pour les tests
    ├── __init__.py

```

## Lien intéressant

1. Kaggle: <https://www.kaggle.com>
2. Free Music Archive: <https://freemusicarchive.org>
3. GTZAN Genre Collection: <https://www.kaggle.com/datasets/carlthome/gtzan-genre-collection>
4. MusicGenres Dataset (HuggingFace): <https://huggingface.co/datasets/ccmusic-database/music_genre>
5. MusicCaps / AudioSet: <https://huggingface.co/datasets/google/MusicCaps>
6. Recherche: <https://dblp.org> & <https://dblp.uni-trier.de/search/publ>
7. Apache spark: <https://spark.apache.org>
