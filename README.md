# 🕷️ Projet Web Scrapping avec BeautifulSoup

Un projet de web scrapping développé en Python utilisant la bibliothèque BeautifulSoup pour extraire et analyser des données depuis des sites web.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Description

Ce projet permet d'extraire automatiquement des paroles de chansons depuis des sites web en utilisant les techniques de web scrapping. BeautifulSoup facilite l'analyse du code HTML et l'extraction des paroles qui sont ensuite sauvegardées au format JSON.

## ✨ Fonctionnalités

- 🎵 **Extraction de paroles** : Récupération automatique de paroles de chansons depuis le web
- 🔍 **Analyse HTML** : Parsing et navigation dans la structure HTML des pages
- 📊 **Traitement des données** : Nettoyage et organisation des paroles extraites
- 💾 **Sauvegarde JSON** : Export des résultats dans un fichier JSON structuré

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Clonez ce dépôt :**
```bash
git clone https://github.com/EbroVital/webScraping.git
cd webScraping
```

2. **Créez un environnement virtuel (recommandé) :**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Installez les dépendances :**
```bash
pip install beautifulsoup4
pip install requests
```

**OU** utilisez le fichier requirements.txt (si disponible) :
```bash
pip install -r requirements.txt
```

### 📦 Dépendances principales

- **beautifulsoup4** : Bibliothèque pour le parsing HTML/XML
- **requests** : Pour effectuer des requêtes HTTP

## 💻 Utilisation

### Utilisation basique

```python
from bs4 import BeautifulSoup
import requests

# Effectuer une requête HTTP
url = "https://example.com"
response = requests.get(url)

# Parser le contenu HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extraire des données
lyrics = soup.find("div", class_="Lyrics__Container-sc-a49d8432-1 fBKwZw")
```

### Lancer le script principal

```bash
python index.py
```


## 🛠️ Technologies utilisées

- **Python** : Langage de programmation
- **BeautifulSoup4** : Parsing et extraction de données HTML/XML
- **Requests** : Gestion des requêtes HTTP

## 📖 Exemples d'utilisation

### Extraire tous les liens d'une page

```python
from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Trouver tous les liens
liens = soup.find_all('a')
for lien in liens:
    print(lien.get('href'))
```


### Sauvegarder les données dans un fichier JSON

```python
import json

urls = get_all_urls()
    
    words = []
    for url in urls :
        lyrics = extract_lyrics(url=url)
        words.extend(lyrics)
    
    with open("data.json", "w") as f :
        json.dump(words, f, indent=4)
```

## ⚠️ Considérations légales et éthiques

- ✅ Vérifiez toujours le fichier `robots.txt` du site avant de scraper
- ✅ Respectez les conditions d'utilisation des sites web
- ✅ Limitez la fréquence de vos requêtes pour ne pas surcharger les serveurs
- ✅ Identifiez votre bot avec un User-Agent approprié
- ❌ Ne scrapez pas de données personnelles sans autorisation

## 🔧 Résolution des problèmes courants

### Erreur de connexion
```python
# Ajouter un User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, headers=headers)
```
## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📚 Ressources utiles

- [Documentation BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Documentation Requests](https://requests.readthedocs.io/)
- [Guide du Web Scraping éthique](https://www.scrapehero.com/web-scraping-laws/)

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !
