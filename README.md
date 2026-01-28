# Projet-Big_Data

## Idée

Faire un shazam maison. Le but du projet est de créer un shazam, où a partir d'un fichier audio, on doit retrouver la musique la plus proche grace à une base de donnée vectorielle de musiques.

## À faire

1. trois articles de recherche à trouver et à lire par personne.
2. Faire le projet.
3. Faire un rapport.

## Articles de recherche

### Thomas

1. [An Industrial-Strength Audio Search Algorithm](research_paper/thomas/Wang03-shazam.pdf)

    Cet article présente un algorithme de reconnaissance audio, développé par Avery Li-Chun Wang (Shazam).

    L’objectif est d’identifier un morceau de musique à partir d’un court extrait sonore (quelques secondes), même lorsque celui-ci est fortement dégradé : bruit ambiant, voix superposées, distorsions, compression GSM ou coupures réseau.

    L’article propose une méthode de fingerprinting audio basée sur l’extraction de pics fréquentiels, appelés *constellations*. Ces points caractéristiques sont ensuite combinés par paires pour former des hashs temporels discriminants. L’algorithme identifie les morceaux en détectant des alignements temporels cohérents entre l’extrait audio et les pistes de la base de données.

2. [Cross modal audio search and retrieval with joint embeddings based on text and audio](research_paper/thomas/Audio%20search%20and%20retrieval%20-%20Microsoft.pdf)

    Cet article traite de la recherche et de la récupération audio multimodales, en combinant texte et audio.

    Les chercheurs s’attaquent ici à une des limites des moteurs de recherche audio : soit les moteurs comparent texte-texte (via des métadonnées), soit audio-audio (par similarité acoustique), sans interaction entre les deux.

    Les auteurs proposent un embedding conjoint audio-texte à l’aide d’un réseau de neurones siamois (Siamese Neural Network). Ce réseau projette des caractéristiques audio et textuelles dans un même espace, où la similarité sémantique et acoustique peut être mesurée directement.

3. [A fast audio similarity retrieval method for millions of music tracks](research_paper/thomas/A%20fast%20audio%20similarity%20retrieval%20method.pdf)

    Cet article parle du problème de la recherche rapide de similarité audio dans des bases de données musicales de très grande taille (plusieurs millions de morceaux).

    Le problème est que les méthodes de similarité audio les plus performantes reposent sur des modèles complexes (par exemple les modèles de timbre gaussiens), qui sont très coûteux à calculer et donc difficiles à appliquer sur de gros datasets.

    Les auteurs proposent une méthode filter-and-refine qui porte sur une adaptation de l’algorithme FastMap. L’idée est de projeter les morceaux de musique dans un espace vectoriel de plus faible dimension, afin d’effectuer une pré-sélection rapide des candidats les plus proches grâce à une distance euclidienne, puis d'améliorer les résultats avec la mesure exacte (divergence de Kullback–Leibler symétrisée).

## Premiers pas

### Comment démarrer le projet

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

### Ajout d'une librairie

1. On utilise pip pour installer la librairie qu'on souhaite (Il faut bien vérifier qu'on se situe dans le venv).
2. Puis on fait la commande :

    ```bash
        pip freeze > requirements.txt
        # Cette commande permet de mettre à jour les librairies nécessaires pour éxecuter le code du projet.
    ```

## Structure du projet

```bash
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
