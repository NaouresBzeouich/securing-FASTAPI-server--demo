# --------------------------
# Étape 1 : Build
# --------------------------
FROM python:3.10-alpine AS builder

# Installer les dépendances nécessaires à la compilation
RUN apk add --no-cache build-base libffi-dev musl-dev

WORKDIR /app

# Copier uniquement les dépendances pour profiter du cache
COPY /FastAPISecurityTest/requirements.txt .

# Installer les dépendances dans un dossier spécifique
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

# Copier le code source
COPY . .

# --------------------------
# Étape 2 : Runtime minimal
# --------------------------
FROM python:3.10-alpine

# Créer un utilisateur non-root
RUN adduser -D fastapiuser

# Créer le dossier de l'application et définir le propriétaire
WORKDIR /app
COPY --from=builder /install /usr/local
COPY --from=builder /app /app

# Changer le propriétaire
RUN chown -R fastapiuser:fastapiuser /app

# Passer à l'utilisateur non-root
USER fastapiuser

# Exposer le port FastAPI
EXPOSE 8000

# Commande pour lancer le serveur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
