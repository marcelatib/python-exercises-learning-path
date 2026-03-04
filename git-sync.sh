#!/bin/bash

# Script para sincronizar com GitHub

echo "=== Verificando status do Git ==="
git status

echo -e "\n=== Verificando commits ==="
git log --oneline || echo "Nenhum commit encontrado"

echo -e "\n=== Adicionando todos os arquivos ==="
git add .

echo -e "\n=== Fazendo commit inicial ==="
git commit -m "Initial commit: Python exercises learning path" || echo "Nenhuma alteração para commitar ou commit já existe"

echo -e "\n=== Verificando branch ==="
git branch -a

echo -e "\n=== Renomeando para main (se necessário) ==="
git branch -M main || echo "Branch main já existe"

echo -e "\n=== Fazendo push para GitHub ==="
git push -u origin main

echo -e "\n=== Sincronização concluída! ==="
git log --oneline -5

