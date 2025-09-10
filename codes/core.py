"""
Core module for task management.

Ce module contient la logique métier principale pour la gestion des tâches.
Il fournit les fonctions de base pour créer, modifier, supprimer et afficher des tâches.

Format des tâches: Chaque tâche est stockée sous forme "ID;Description" dans le fichier.

Auteurs: Groupe 4 - Codecamp
"""


def parse_tasks(tasks):
    """
    Parse les lignes brutes du fichier en une liste structurée de tâches.
    
    Args:
        tasks (list): Liste des lignes lues depuis le fichier de tâches
        
    Returns:
        list: Liste de tuples (id: int, description: str) représentant les tâches
        
    Note:
        - Ignore les lignes vides
        - Ignore les lignes mal formatées (sans ';' ou avec ID non numérique)
        - Le format attendu est "ID;Description"
        
    Example:
        >>> parse_tasks(["1;Faire les courses", "2;Réviser"])
        [(1, 'Faire les courses'), (2, 'Réviser')]
    """
    parsed_tasks = []
    for line in tasks:
        line = line.strip()
        if line:  # Ignore empty lines
            parts = line.split(";", 1)
            if len(parts) == 2:
                try:
                    tid = int(parts[0])
                    parsed_tasks.append((tid, parts[1]))
                except ValueError:
                    # Ignore les lignes avec un ID non numérique
                    continue
    return parsed_tasks


def add(tasks, details):
    """
    Ajoute une nouvelle tâche avec un ID auto-incrémenté.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        details (str): Description de la nouvelle tâche
        
    Returns:
        tuple: (new_id: int, description: str, task_line: str)
            - new_id: L'ID assigné à la nouvelle tâche
            - description: La description de la tâche
            - task_line: La ligne formatée à écrire dans le fichier
            
    Note:
        - L'ID est calculé comme max(IDs existants) + 1
        - Si aucune tâche n'existe, l'ID commence à 1
        - La ligne retournée inclut le saut de ligne final
        
    Example:
        >>> add(["1;Tâche existante"], "Nouvelle tâche")
        (2, 'Nouvelle tâche', '2;Nouvelle tâche\\n')
    """
    # Trouve le prochain ID disponible en analysant les tâches existantes
    parsed_tasks = parse_tasks(tasks)
    if parsed_tasks:
        # Calcule l'ID maximum et ajoute 1
        max_id = max(task[0] for task in parsed_tasks)
        new_id = max_id + 1
    else:
        # Premier ID si aucune tâche n'existe
        new_id = 1
    
    # Formate la ligne pour l'écriture dans le fichier
    new_task_line = f"{new_id};{details}\n"
    return (new_id, details, new_task_line)


def modify(tasks, task_id, new_details):
    """
    Modifie la description d'une tâche existante par son ID.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        task_id (str|int): ID de la tâche à modifier
        new_details (str): Nouvelle description pour la tâche
        
    Returns:
        tuple: (found: bool, updated_tasks: list)
            - found: True si la tâche a été trouvée et modifiée, False sinon
            - updated_tasks: Liste des tâches avec la modification appliquée
            
    Note:
        - L'ID peut être fourni comme string ou int, il sera converti
        - Si l'ID n'est pas numérique, retourne (False, [])
        - La liste retournée contient toutes les tâches, modifiée incluse
        
    Example:
        >>> modify(["1;Ancienne tâche"], "1", "Nouvelle description")
        (True, [(1, 'Nouvelle description')])
    """
    # Validation et conversion de l'ID
    try:
        task_id = int(task_id)
    except ValueError:
        # ID invalide (non numérique)
        return False, []
        
    # Parse les tâches existantes
    parsed_tasks = parse_tasks(tasks)
    found = False
    
    # Recherche et modification de la tâche correspondante
    for i, (tid, desc) in enumerate(parsed_tasks):
        if tid == task_id:
            parsed_tasks[i] = (tid, new_details)
            found = True
            break
    
    return found, parsed_tasks
def rm(tasks, task_id):
    """
    Supprime une tâche par son ID.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        task_id (str|int): ID de la tâche à supprimer
        
    Returns:
        tuple: (found: bool, remaining_tasks: list)
            - found: True si la tâche a été trouvée et supprimée, False sinon
            - remaining_tasks: Liste des tâches restantes après suppression
            
    Note:
        - L'ID peut être fourni comme string ou int, il sera converti
        - Si l'ID n'est pas numérique, retourne (False, tâches_originales)
        - Les IDs des autres tâches ne sont pas réassignés
        
    Example:
        >>> rm(["1;Tâche 1", "2;Tâche 2"], "1")
        (True, [(2, 'Tâche 2')])
    """
    # Validation et conversion de l'ID
    try:
        task_id = int(task_id)
    except ValueError:
        # ID invalide, retourne les tâches non modifiées
        return False, parse_tasks(tasks)
        
    # Parse les tâches existantes
    parsed_tasks = parse_tasks(tasks)
    original_length = len(parsed_tasks)
    
    # Filtre les tâches pour enlever celle avec l'ID spécifié
    filtered_tasks = [(tid, desc) for tid, desc in parsed_tasks if tid != task_id]
    
    # Détermine si une tâche a été supprimée
    found = len(filtered_tasks) < original_length
    return found, filtered_tasks
            

def show(tasks):
    """
    Affiche la liste des tâches dans un tableau formaté, triées par ID.
    
    Args:
        tasks (list): Liste des lignes du fichier de tâches
        
    Returns:
        None: Affiche directement le résultat sur stdout
        
    Note:
        - Affiche "No tasks found." si aucune tâche n'existe
        - Le tableau s'adapte automatiquement à la longueur des descriptions
        - Les tâches sont automatiquement triées par ID croissant
        - Format du tableau: +-----+-------------+
                           | id  | description |
                           +-----+-------------+
                           
    Example:
        >>> show(["2;Seconde tâche", "1;Première tâche"])
        +-----+---------------+
        | id  | description   |
        +-----+---------------+
        | 1   | Première tâche|
        | 2   | Seconde tâche |
        +-----+---------------+
    """
    # Parse et vérifie s'il y a des tâches
    parsed_tasks = parse_tasks(tasks)
    if not parsed_tasks:
        print("No tasks found.")
        return
    
    # Trie les tâches par ID croissant
    sorted_tasks = sorted(parsed_tasks, key=lambda x: x[0])
    
    # Calcule la largeur optimale pour la colonne description
    max_desc_length = max(len(desc) for _, desc in sorted_tasks) if sorted_tasks else 10
    max_desc_length = max(max_desc_length, 11)  # Largeur minimale pour "description"
    
    # Construction et affichage du tableau
    border_line = f"+-----+{'-' * (max_desc_length + 2)}+"
    header_line = f"| {'id':<3} | {'description':<{max_desc_length}} |"
    
    print(border_line)
    print(header_line)
    print(border_line)
    
    # Affichage de chaque tâche
    for task_id, description in sorted_tasks:
        print(f"| {task_id:<3} | {description:<{max_desc_length}} |")
    
    print(border_line)