"""
Options module for command-line argument parsing.

Ce module configure l'analyseur de ligne de commande en utilisant argparse.
Il définit la structure des commandes disponibles et leurs arguments.

Structure CLI:
    python task.py <fichier> <commande> [arguments]

Commandes disponibles:
    - add <description>        : Ajoute une nouvelle tâche
    - modify <id> <description>: Modifie une tâche existante
    - rm <id>                 : Supprime une tâche
    - show                    : Affiche toutes les tâches
    - add-label <id> <label>  : Ajoute un label à une tâche
    - rm-label <id> <label>   : Supprime un label d'une tâche
    - set-labels <id> <labels>: Remplace les labels d'une tâche

Auteurs: Groupe 4 - Codecamp
"""

import argparse


def create_parser():
    """
    Crée et configure l'analyseur de ligne de commande.
    
    Returns:
        argparse.ArgumentParser: Parseur configuré avec toutes les commandes
        
    Note:
        Utilise des sous-parseurs pour gérer les différentes commandes.
        Chaque commande a ses propres arguments spécifiques.
        
    Example:
        >>> parser = create_parser()
        >>> args = parser.parse_args(['tasks.txt', 'add', 'Nouvelle', 'tâche'])
        >>> print(args.command, args.details)
        add ['Nouvelle', 'tâche']
    """
    # Création du parseur principal
    parser = argparse.ArgumentParser(
        description='Simple task manager - Gestionnaire de tâches en ligne de commande',
        epilog='Exemple: python task.py lestaches.txt add "Faire les courses"'
    )
    
    # Argument positionnel obligatoire : le fichier de tâches
    parser.add_argument(
        'file', 
        help='Chemin vers le fichier contenant les tâches'
    )
    
    # Sous-parseurs pour les différentes commandes
    subparsers = parser.add_subparsers(
        help='Commandes disponibles pour gérer les tâches', 
        dest='command', 
        required=True,
        metavar='COMMANDE'
    )
    
    # === Commande ADD ===
    parser_add = subparsers.add_parser(
        'add', 
        help='Ajouter une nouvelle tâche',
        description='Ajoute une nouvelle tâche avec la description fournie'
    )
    parser_add.add_argument(
        'details', 
        nargs='*', 
        default=["no details"], 
        help="Description de la tâche (plusieurs mots acceptés)"
    )
    parser_add.add_argument(
        '--labels', 
        help="Labels à associer à la tâche (séparés par des virgules, ex: urgent,personnel)"
    )
    
    # === Commande MODIFY ===
    parser_modify = subparsers.add_parser(
        'modify', 
        help='Modifier une tâche existante',
        description='Modifie la description d\'une tâche en utilisant son ID'
    )
    parser_modify.add_argument(
        'id', 
        help="ID numérique de la tâche à modifier"
    )
    parser_modify.add_argument(
        'details', 
        nargs='*', 
        default=["no details"], 
        help="Nouvelle description de la tâche"
    )
    
    # === Commande RM (Remove) ===
    parser_rm = subparsers.add_parser(
        'rm', 
        help='Supprimer une tâche',
        description='Supprime définitivement une tâche en utilisant son ID'
    )
    parser_rm.add_argument(
        'id', 
        help="ID numérique de la tâche à supprimer"
    )
    
    # === Commande SHOW ===
    parser_show = subparsers.add_parser(
        'show', 
        help='Afficher toutes les tâches',
        description='Affiche la liste de toutes les tâches dans un tableau formaté'
    )
    parser_show.add_argument(
        '--filter', 
        help="Filtre pour n'afficher que les tâches ayant ce label"
    )
    
    # === Commande ADD-LABEL ===
    parser_add_label = subparsers.add_parser(
        'add-label', 
        help='Ajouter un label à une tâche',
        description='Ajoute un label à une tâche existante'
    )
    parser_add_label.add_argument(
        'id', 
        help="ID numérique de la tâche"
    )
    parser_add_label.add_argument(
        'label', 
        help="Label à ajouter à la tâche"
    )
    
    # === Commande RM-LABEL ===
    parser_rm_label = subparsers.add_parser(
        'rm-label', 
        help='Supprimer un label d\'une tâche',
        description='Supprime un label spécifique d\'une tâche existante'
    )
    parser_rm_label.add_argument(
        'id', 
        help="ID numérique de la tâche"
    )
    parser_rm_label.add_argument(
        'label', 
        help="Label à supprimer de la tâche"
    )
    
    # === Commande SET-LABELS ===
    parser_set_labels = subparsers.add_parser(
        'set-labels', 
        help='Remplacer les labels d\'une tâche',
        description='Remplace tous les labels d\'une tâche par une nouvelle liste'
    )
    parser_set_labels.add_argument(
        'id', 
        help="ID numérique de la tâche"
    )
    parser_set_labels.add_argument(
        'labels', 
        help="Nouveaux labels (séparés par des virgules, ex: urgent,personnel)"
    )
    
    return parser
