"""
Commands module for task management CLI.

Ce module implémente l'interface entre la ligne de commande et la logique métier.
Il gère les opérations sur les fichiers et l'affichage des messages utilisateur.

Chaque fonction correspond à une commande CLI et gère:
- La lecture/écriture des fichiers de tâches
- L'affichage des messages de succès/erreur
- La coordination avec le module core pour la logique métier

Auteurs: Groupe 4 - Codecamp
"""

import core


def add(details, filename, tasks):
    """
    Commande CLI pour ajouter une nouvelle tâche.
    
    Args:
        details (str): Description de la nouvelle tâche
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        
    Side Effects:
        - Ajoute une ligne au fichier spécifié
        - Affiche un message de confirmation avec l'ID assigné
        
    Example:
        >>> add("Faire les courses", "tasks.txt", [])
        Successfully added task 1 (Faire les courses)
    """
    # Utilise la logique métier pour créer la nouvelle tâche
    task_id, description, task_line = core.add(tasks, details)
    
    # Ajoute la tâche au fichier (mode append)
    with open(filename, 'a') as f:
        f.write(task_line)
    
    # Confirmation à l'utilisateur
    print(f"Successfully added task {task_id} ({description})")

def modify(task_id, new_details, filename, tasks):
    """
    Commande CLI pour modifier une tâche existante.
    
    Args:
        task_id (str): ID de la tâche à modifier
        new_details (str): Nouvelle description pour la tâche
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        
    Side Effects:
        - Réécrit entièrement le fichier avec les modifications
        - Affiche un message de succès ou d'erreur
        
    Note:
        Le fichier est entièrement réécrit pour maintenir la cohérence.
        
    Example:
        >>> modify("1", "Nouvelle description", "tasks.txt", ["1;Ancienne"])
        Task 1 modified.
    """
    # Utilise la logique métier pour modifier la tâche
    found, updated_tasks = core.modify(tasks, task_id, new_details)
    
    if found:
        # Réécrit tout le fichier avec les tâches mises à jour
        with open(filename, 'w') as f:
            for tid, desc in updated_tasks:
                f.write(f"{tid};{desc}\n")
        print(f"Task {task_id} modified.")
    else:
        # Message d'erreur si la tâche n'existe pas
        print(f"Error: task id {task_id} not found.")

def rm(task_id, filename, tasks):
    """
    Commande CLI pour supprimer une tâche.
    
    Args:
        task_id (str): ID de la tâche à supprimer
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        
    Side Effects:
        - Réécrit le fichier sans la tâche supprimée
        - Affiche un message de succès ou d'erreur
        
    Note:
        Les IDs des autres tâches ne sont pas modifiés après suppression.
        
    Example:
        >>> rm("1", "tasks.txt", ["1;Tâche à supprimer", "2;Autre tâche"])
        Task 1 removed.
    """
    # Utilise la logique métier pour supprimer la tâche
    found, remaining_tasks = core.rm(tasks, task_id)
    
    if found:
        # Réécrit le fichier avec les tâches restantes
        with open(filename, 'w') as f:
            for tid, desc in remaining_tasks:
                f.write(f"{tid};{desc}\n")
        print(f"Task {task_id} removed.")
    else:
        # Message d'erreur si la tâche n'existe pas
        print(f"Error: task id {task_id} not found.")

def show(tasks):
    """
    Commande CLI pour afficher toutes les tâches.
    
    Args:
        tasks (list): Liste des lignes du fichier de tâches
        
    Side Effects:
        - Affiche un tableau formaté des tâches sur stdout
        - Affiche "No tasks found." si aucune tâche n'existe
        
    Note:
        Délègue l'affichage au module core qui gère le formatage du tableau.
        
    Example:
        >>> show(["1;Première tâche", "2;Seconde tâche"])
        +-----+---------------+
        | id  | description   |
        +-----+---------------+
        | 1   | Première tâche|
        | 2   | Seconde tâche |
        +-----+---------------+
    """
    # Délègue l'affichage au module core
    core.show(tasks)