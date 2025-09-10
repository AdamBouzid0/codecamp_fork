#!/usr/bin/env python3
"""
TaskManager - Gestionnaire de tâches en ligne de commande.

Programme principal du gestionnaire de tâches développé dans le cadre du codecamp.
Ce script coordonne l'analyse des arguments, la lecture des fichiers et l'exécution
des commandes de gestion de tâches.

Usage:
    python3 task.py <fichier> add <description>
    python3 task.py <fichier> modify <id> <nouvelle_description>
    python3 task.py <fichier> rm <id>
    python3 task.py <fichier> show

Exemples:
    python3 task.py lestaches.txt add "Faire les courses"
    python3 task.py lestaches.txt modify 1 "Faire les courses au supermarché"
    python3 task.py lestaches.txt rm 1
    python3 task.py lestaches.txt show

Auteurs: Groupe 4 - Codecamp
Date: Septembre 2025
"""

import commands
from options import create_parser

# === ANALYSE DES ARGUMENTS ===
# Création et utilisation du parseur de ligne de commande
options = create_parser().parse_args()

try:
    # === LECTURE DU FICHIER DE TÂCHES ===
    # Tente de lire le fichier existant
    with open(options.file, 'r') as f:
        tasks = f.readlines()
    
    # === EXÉCUTION DE LA COMMANDE ===
    # Dispatch vers la fonction appropriée selon la commande
    if options.command == 'add':
        # Ajoute une nouvelle tâche
        commands.add(' '.join(options.details), options.file, tasks)
        
    elif options.command == 'modify':
        # Modifie une tâche existante
        commands.modify(options.id, ' '.join(options.details), options.file, tasks)
        
    elif options.command == 'rm':
        # Supprime une tâche
        commands.rm(options.id, options.file, tasks)
        
    elif options.command == 'show':
        # Affiche toutes les tâches
        commands.show(tasks)
        
except FileNotFoundError:
    # === GESTION DES FICHIERS INEXISTANTS ===
    # Gère le cas où le fichier de tâches n'existe pas encore
    if options.command == 'add':
        # Permet d'ajouter la première tâche dans un nouveau fichier
        commands.add(' '.join(options.details), options.file, [])
    elif options.command == 'modify':
        # Impossible de modifier dans un fichier inexistant
        print(f"Error: The file {options.file} was not found")
    elif options.command == 'rm':
        # Impossible de supprimer dans un fichier inexistant
        print(f"Error: The file {options.file} was not found")
    elif options.command == 'show':
        # Affiche un message approprié pour un fichier vide
        print("No tasks found.")
