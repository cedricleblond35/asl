FROM ubuntu:22.04

# Mettre à jour les paquets et installer tzdata pour une gestion robuste des fuseaux horaires
RUN apt-get update && apt-get install -y tzdata

# Définir explicitement le fuseau horaire (par exemple, Europe/Paris)
RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
    echo "Europe/Paris" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# Mettre à jour les paquets et installer les dépendances nécessaires pour Python et OpenCV
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    libgl1-mesa-glx

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier tout le contenu du répertoire local dans /app du conteneur
COPY . .

# Installer les dépendances Python listées dans requirements.txt, incluant OpenCV
RUN pip install --no-cache-dir -r requirements.txt

# Installer OpenCV via pip (si ce n'est pas déjà dans requirements.txt)
RUN pip install opencv-python

# Exposer le port 5000 (par défaut pour Flask)
EXPOSE 5000

# Lancer l'application Flask
CMD ["python3", "app/app.py"]