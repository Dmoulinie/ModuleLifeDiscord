# Utilisez l'image Python 3.8 alpine comme base
FROM python:3.8-alpine

# Install required packages
RUN apk add --no-cache \
        ghostscript \
        poppler-utils \
        imagemagick \
        imagemagick-dev \
        build-base \
        libffi-dev \
        cairo-dev 

# Définir le répertoire de travail dans l'image
WORKDIR /app

# Copier le code de l'application dans le répertoire de travail de l'image
COPY . .

# Installer les dépendances requises pour l'application
RUN pip install -r requirements.txt




# Définir la commande pour lancer l'application
CMD ["python", "src/bot.py"]
