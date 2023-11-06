# Pun Generator

Ce programme est conçu pour vous fournir des blagues amusantes à partir d'une API de blagues. Vous trouverez ci-dessous des informations sur la manière d'installer et de lancer le programme, ainsi que des détails sur ses fonctionnalités.

## Fonctionnalités

Ce programme est capable de :

- Récupérer une blague aléatoire à partir de l'API de blagues.
- Afficher la blague récupérée dans la console.

## Installation

Pour exécuter ce programme, suivez ces étapes :

### 1. Clonez le repository sur votre ordinateur :

```bash
git clone https://github.com/[votre-nom]/pun-generator.git
```

### 2. Installez les dépendances :
```bash
pip install -r requirements.txt
```
## Comment lancer - Terminal

Vous pouvez exécuter le programme en utilisant la ligne de commande comme suit :

```bash
python3 app.py
```
## Comment lancer - Docker

Vous pouvez exécuter le programme en utilisant Docker comme suit :

### Monté l'image docker
```bash
docker build -t pun-generator .
```

### Lancer l'image docker
```bash
docker run pun-generator
```



