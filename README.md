# MyProject

## Description

Mon projet est un site web construit avec Django pour gérer un blog avec des articles et des événements, et inclut un formulaire de contact. 
Le backend utilise JWT pour l'authentification des API et l'authentification par session pour le site web. 
La documentation de l'API est générée avec `drf_yasg`.

## Prérequis

- Python 3.x
- Django 3.x
- pip (Python package installer)

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/anisay12/blog_project.git
   cd myproject

2.Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate   # Sur Windows, utilisez `venv\Scripts\activate`

3. Installer les dépendances :
4. ```bash
pip install -r requirements.txt

5. Configurer les variables d'environnement :
   Créez un fichier .env à la racine du projet et ajoutez-y les variables nécessaires :

    SECRET_KEY=your-secret-key
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3

5.Appliquer les migrations de la base de données :
```bash
python manage.py migrate

6.Créer un superutilisateur :
```bash
python manage.py createsuperuser

7. Démarrer le serveur de développement :
```bash
python manage.py runserver

## Utilisation
Accédez à l'interface d'administration à http://127.0.0.1:8000/admin/ pour gérer les articles, les événements et les contacts.
Accédez aux différentes sections du site :
Articles : http://127.0.0.1:8000/articles/
Événements : http://127.0.0.1:8000/events/
Formulaire de contact : http://127.0.0.1:8000/contact/

## Tester les endpoints
Obtenir un token :
Envoyez une requête POST à /api/token/ avec les informations d'identification de l'utilisateur (nom d'utilisateur et mot de passe) pour obtenir un token JWT.


## Documentation de l'API
Pour la documentation Swagger UI : http://127.0.0.1:8000/swagger/
Pour la documentation ReDoc : http://127.0.0.1:8000/redoc/
Pour le schéma JSON : http://127.0.0.1:8000/swagger.json
Pour le schéma YAML : http://127.0.0.1:8000/swagger.yaml




   


