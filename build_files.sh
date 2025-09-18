#!/usr/bin/env bash

# Instala as dependências Python a partir do requirements.txt
echo "Instalando dependências..."
pip install -r requirements.txt

# Agora, execute os comandos do Django
echo "Migrando banco de dados..."
python3 ./src/manage.py makemigrations --noinput
python3 ./src/manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python3 ./src/manage.py collectstatic --noinput