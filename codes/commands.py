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


def add(details, filename, tasks, labels=None):
    """
    Commande CLI pour ajouter une nouvelle tâche.
    
    Args:
        details (str): Description de la nouvelle tâche
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        labels (list, optional): Liste des labels à associer à la tâche
        
    Side Effects:
        - Ajoute une ligne au fichier spécifié
        - Affiche un message de confirmation avec l'ID assigné
        
    Example:
        >>> add("Faire les courses", "tasks.txt", [], ["urgent", "personnel"])
        Successfully added task 1 (Faire les courses) with labels: urgent,personnel
    """
    # Utilise la logique métier pour créer la nouvelle tâche
    task_id, description, task_labels, task_line = core.add(tasks, details, labels)
    
    # Ajoute la tâche au fichier (mode append)
    with open(filename, 'a') as f:
        f.write(task_line)
    
    # Confirmation à l'utilisateur
    if task_labels:
        labels_str = ",".join(task_labels)
        print(f"Successfully added task {task_id} ({description}) with labels: {labels_str}")
    else:
        print(f"Successfully added task {task_id} ({description})")

def modify(task_id, new_details, filename, tasks, new_labels=None):
    """
    Commande CLI pour modifier une tâche existante.
    
    Args:
        task_id (str): ID de la tâche à modifier
        new_details (str): Nouvelle description pour la tâche
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        new_labels (list, optional): Nouveaux labels pour la tâche (None = pas de changement)
        
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
    found, updated_tasks = core.modify(tasks, task_id, new_details, new_labels)
    
    if found:
        # Réécrit tout le fichier avec les tâches mises à jour
        with open(filename, 'w') as f:
            for tid, desc, labels in updated_tasks:
                labels_str = ",".join(labels) if labels else ""
                f.write(f"{tid};{desc};{labels_str}\n")
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
            for tid, desc, labels in remaining_tasks:
                labels_str = ",".join(labels) if labels else ""
                f.write(f"{tid};{desc};{labels_str}\n")
        print(f"Task {task_id} removed.")
    else:
        # Message d'erreur si la tâche n'existe pas
        print(f"Error: task id {task_id} not found.")
    
    if found:
        # Réécrit le fichier avec les tâches restantes
        with open(filename, 'w') as f:
            for tid, desc, labels in remaining_tasks:
                labels_str = ",".join(labels) if labels else ""
                f.write(f"{tid};{desc};{labels_str}\n")
        print(f"Task {task_id} removed.")
    else:
        # Message d'erreur si la tâche n'existe pas
        print(f"Error: task id {task_id} not found.")

def show(tasks, label_filter=None):
    """
    Commande CLI pour afficher toutes les tâches.
    
    Args:
        tasks (list): Liste des lignes du fichier de tâches
        label_filter (str, optional): Filtre pour n'afficher que les tâches avec ce label
        
    Side Effects:
        - Affiche un tableau formaté des tâches sur stdout
        - Affiche "No tasks found." si aucune tâche n'existe
        
    Note:
        Délègue l'affichage au module core qui gère le formatage du tableau.
        
    Example:
        >>> show(["1;Première tâche;urgent", "2;Seconde tâche;personnel"])
        +-----+---------------+----------+
        | id  | description   | labels   |
        +-----+---------------+----------+
        | 1   | Première tâche| urgent   |
        | 2   | Seconde tâche | personnel|
        +-----+---------------+----------+
    """
    # Délègue l'affichage au module core
    core.show(tasks, label_filter)


def add_label(task_id, label, filename, tasks):
    """
    Commande CLI pour ajouter un label à une tâche.
    
    Args:
        task_id (str): ID de la tâche à modifier
        label (str): Label à ajouter
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        
    Side Effects:
        - Réécrit le fichier avec le label ajouté
        - Affiche un message de succès ou d'erreur
    """
    found, updated_tasks = core.add_label(tasks, task_id, label)
    
    if found:
        # Réécrit tout le fichier avec les tâches mises à jour
        with open(filename, 'w') as f:
            for tid, desc, labels in updated_tasks:
                labels_str = ",".join(labels) if labels else ""
                f.write(f"{tid};{desc};{labels_str}\n")
        print(f"Label '{label}' added to task {task_id}.")
    else:
        print(f"Error: task id {task_id} not found.")


def rm_label(task_id, label, filename, tasks):
    """
    Commande CLI pour supprimer un label d'une tâche.
    
    Args:
        task_id (str): ID de la tâche à modifier
        label (str): Label à supprimer
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        
    Side Effects:
        - Réécrit le fichier avec le label supprimé
        - Affiche un message de succès ou d'erreur
    """
    found, label_found, updated_tasks = core.rm_label(tasks, task_id, label)
    
    if found:
        if label_found:
            # Réécrit tout le fichier avec les tâches mises à jour
            with open(filename, 'w') as f:
                for tid, desc, labels in updated_tasks:
                    labels_str = ",".join(labels) if labels else ""
                    f.write(f"{tid};{desc};{labels_str}\n")
            print(f"Label '{label}' removed from task {task_id}.")
        else:
            print(f"Error: label '{label}' not found in task {task_id}.")
    else:
        print(f"Error: task id {task_id} not found.")


def set_labels(task_id, labels_str, filename, tasks):
    """
    Commande CLI pour remplacer les labels d'une tâche.
    
    Args:
        task_id (str): ID de la tâche à modifier
        labels_str (str): Nouveaux labels séparés par des virgules
        filename (str): Chemin vers le fichier de tâches
        tasks (list): Liste des lignes existantes du fichier
        
    Side Effects:
        - Réécrit le fichier avec les nouveaux labels
        - Affiche un message de succès ou d'erreur
    """
    # Parse les labels depuis la chaîne
    new_labels = [label.strip() for label in labels_str.split(",") if label.strip()] if labels_str else []
    
    found, updated_tasks = core.set_labels(tasks, task_id, new_labels)
    
    if found:
        # Réécrit tout le fichier avec les tâches mises à jour
        with open(filename, 'w') as f:
            for tid, desc, labels in updated_tasks:
                labels_str = ",".join(labels) if labels else ""
                f.write(f"{tid};{desc};{labels_str}\n")
        if new_labels:
            print(f"Labels for task {task_id} set to: {','.join(new_labels)}")
        else:
            print(f"All labels removed from task {task_id}.")
    else:
        print(f"Error: task id {task_id} not found.")