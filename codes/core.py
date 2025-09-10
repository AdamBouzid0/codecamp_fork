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
        list: Liste de tuples (id: int, description: str, labels: list) représentant les tâches
        
    Note:
        - Ignore les lignes vides
        - Ignore les lignes mal formatées (sans ';' ou avec ID non numérique)
        - Format attendu: "ID;Description" ou "ID;Description;label1,label2,..."
        - Rétrocompatible avec l'ancien format (sans labels)
        
    Example:
        >>> parse_tasks(["1;Faire les courses;urgent,personnel", "2;Réviser"])
        [(1, 'Faire les courses', ['urgent', 'personnel']), (2, 'Réviser', [])]
    """
    parsed_tasks = []
    for line in tasks:
        line = line.strip()
        if line:  # Ignore empty lines
            parts = line.split(";")
            if len(parts) >= 2:
                try:
                    tid = int(parts[0])
                    description = parts[1]
                    # Gestion des labels (nouveau format)
                    if len(parts) >= 3 and parts[2].strip():
                        labels = [label.strip() for label in parts[2].split(",") if label.strip()]
                    else:
                        labels = []
                    parsed_tasks.append((tid, description, labels))
                except ValueError:
                    # Ignore les lignes avec un ID non numérique
                    continue
    return parsed_tasks


def add(tasks, details, labels=None):
    """
    Ajoute une nouvelle tâche avec un ID auto-incrémenté et des labels optionnels.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        details (str): Description de la nouvelle tâche
        labels (list, optional): Liste des labels à associer à la tâche
        
    Returns:
        tuple: (new_id: int, description: str, labels: list, task_line: str)
            - new_id: L'ID assigné à la nouvelle tâche
            - description: La description de la tâche
            - labels: Liste des labels associés
            - task_line: La ligne formatée à écrire dans le fichier
            
    Note:
        - L'ID est calculé comme max(IDs existants) + 1
        - Si aucune tâche n'existe, l'ID commence à 1
        - La ligne retournée inclut le saut de ligne final
        - Si labels est None, une liste vide est utilisée
        
    Example:
        >>> add(["1;Tâche existante"], "Nouvelle tâche", ["urgent", "personnel"])
        (2, 'Nouvelle tâche', ['urgent', 'personnel'], '2;Nouvelle tâche;urgent,personnel\\n')
    """
    if labels is None:
        labels = []
    
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
    labels_str = ",".join(labels) if labels else ""
    new_task_line = f"{new_id};{details};{labels_str}\n"
    return (new_id, details, labels, new_task_line)


def modify(tasks, task_id, new_details, new_labels=None):
    """
    Modifie la description et/ou les labels d'une tâche existante par son ID.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        task_id (str|int): ID de la tâche à modifier
        new_details (str): Nouvelle description pour la tâche
        new_labels (list, optional): Nouveaux labels pour la tâche (None = pas de changement)
        
    Returns:
        tuple: (found: bool, updated_tasks: list)
            - found: True si la tâche a été trouvée et modifiée, False sinon
            - updated_tasks: Liste des tâches avec la modification appliquée
            
    Note:
        - L'ID peut être fourni comme string ou int, il sera converti
        - Si l'ID n'est pas numérique, retourne (False, [])
        - Si new_labels est None, les labels existants sont conservés
        - La liste retournée contient toutes les tâches, modifiée incluse
        
    Example:
        >>> modify(["1;Ancienne tâche;old"], "1", "Nouvelle description", ["new", "label"])
        (True, [(1, 'Nouvelle description', ['new', 'label'])])
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
    for i, (tid, desc, labels) in enumerate(parsed_tasks):
        if tid == task_id:
            # Utilise les nouveaux labels si fournis, sinon garde les existants
            updated_labels = new_labels if new_labels is not None else labels
            parsed_tasks[i] = (tid, new_details, updated_labels)
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
        >>> rm(["1;Tâche 1;label1", "2;Tâche 2;label2"], "1")
        (True, [(2, 'Tâche 2', ['label2'])])
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
    filtered_tasks = [(tid, desc, labels) for tid, desc, labels in parsed_tasks if tid != task_id]
    
    # Détermine si une tâche a été supprimée
    found = len(filtered_tasks) < original_length
    return found, filtered_tasks
            

def show(tasks, label_filter=None):
    """
    Affiche la liste des tâches dans un tableau formaté, triées par ID.
    
    Args:
        tasks (list): Liste des lignes du fichier de tâches
        label_filter (str, optional): Filtre pour n'afficher que les tâches avec ce label
        
    Returns:
        None: Affiche directement le résultat sur stdout
        
    Note:
        - Affiche "No tasks found." si aucune tâche n'existe
        - Le tableau s'adapte automatiquement à la longueur des descriptions et labels
        - Les tâches sont automatiquement triées par ID croissant
        - Format du tableau avec labels: +-----+-------------+----------+
                                       | id  | description | labels   |
                                       +-----+-------------+----------+
                           
    Example:
        >>> show(["2;Seconde tâche;urgent", "1;Première tâche;personnel"])
        +-----+---------------+----------+
        | id  | description   | labels   |
        +-----+---------------+----------+
        | 1   | Première tâche| personnel|
        | 2   | Seconde tâche | urgent   |
        +-----+---------------+----------+
    """
    # Parse et vérifie s'il y a des tâches
    parsed_tasks = parse_tasks(tasks)
    
    # Applique le filtre par label si spécifié
    if label_filter:
        parsed_tasks = [(tid, desc, labels) for tid, desc, labels in parsed_tasks 
                       if label_filter in labels]
    
    if not parsed_tasks:
        if label_filter:
            print(f"No tasks found with label '{label_filter}'.")
        else:
            print("No tasks found.")
        return
    
    # Trie les tâches par ID croissant
    sorted_tasks = sorted(parsed_tasks, key=lambda x: x[0])
    
    # Calcule les largeurs optimales pour les colonnes
    max_desc_length = max(len(desc) for _, desc, _ in sorted_tasks) if sorted_tasks else 10
    max_desc_length = max(max_desc_length, 11)  # Largeur minimale pour "description"
    
    max_labels_length = max(len(",".join(labels)) for _, _, labels in sorted_tasks) if sorted_tasks else 6
    max_labels_length = max(max_labels_length, 6)  # Largeur minimale pour "labels"
    
    # Construction et affichage du tableau
    border_line = f"+-----+{'-' * (max_desc_length + 2)}+{'-' * (max_labels_length + 2)}+"
    header_line = f"| {'id':<3} | {'description':<{max_desc_length}} | {'labels':<{max_labels_length}} |"
    
    print(border_line)
    print(header_line)
    print(border_line)
    
    # Affichage de chaque tâche
    for task_id, description, labels in sorted_tasks:
        labels_str = ",".join(labels) if labels else ""
        print(f"| {task_id:<3} | {description:<{max_desc_length}} | {labels_str:<{max_labels_length}} |")
    
    print(border_line)


def add_label(tasks, task_id, new_label):
    """
    Ajoute un label à une tâche existante.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        task_id (str|int): ID de la tâche à modifier
        new_label (str): Label à ajouter
        
    Returns:
        tuple: (found: bool, updated_tasks: list)
            - found: True si la tâche a été trouvée et le label ajouté, False sinon
            - updated_tasks: Liste des tâches avec la modification appliquée
            
    Note:
        - Ne fait rien si le label existe déjà
        - L'ID peut être fourni comme string ou int
        
    Example:
        >>> add_label(["1;Ma tâche;urgent"], "1", "important")
        (True, [(1, 'Ma tâche', ['urgent', 'important'])])
    """
    try:
        task_id = int(task_id)
    except ValueError:
        return False, []
        
    parsed_tasks = parse_tasks(tasks)
    found = False
    
    for i, (tid, desc, labels) in enumerate(parsed_tasks):
        if tid == task_id:
            if new_label not in labels:
                labels.append(new_label)
            parsed_tasks[i] = (tid, desc, labels)
            found = True
            break
    
    return found, parsed_tasks


def rm_label(tasks, task_id, label_to_remove):
    """
    Supprime un label d'une tâche existante.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        task_id (str|int): ID de la tâche à modifier
        label_to_remove (str): Label à supprimer
        
    Returns:
        tuple: (found: bool, label_found: bool, updated_tasks: list)
            - found: True si la tâche a été trouvée, False sinon
            - label_found: True si le label existait et a été supprimé, False sinon
            - updated_tasks: Liste des tâches avec la modification appliquée
            
    Example:
        >>> rm_label(["1;Ma tâche;urgent,important"], "1", "urgent")
        (True, True, [(1, 'Ma tâche', ['important'])])
    """
    try:
        task_id = int(task_id)
    except ValueError:
        return False, False, []
        
    parsed_tasks = parse_tasks(tasks)
    found = False
    label_found = False
    
    for i, (tid, desc, labels) in enumerate(parsed_tasks):
        if tid == task_id:
            found = True
            if label_to_remove in labels:
                labels.remove(label_to_remove)
                label_found = True
            parsed_tasks[i] = (tid, desc, labels)
            break
    
    return found, label_found, parsed_tasks


def set_labels(tasks, task_id, new_labels):
    """
    Remplace tous les labels d'une tâche existante.
    
    Args:
        tasks (list): Liste des lignes existantes du fichier de tâches
        task_id (str|int): ID de la tâche à modifier
        new_labels (list): Nouveaux labels pour la tâche
        
    Returns:
        tuple: (found: bool, updated_tasks: list)
            - found: True si la tâche a été trouvée et modifiée, False sinon
            - updated_tasks: Liste des tâches avec la modification appliquée
            
    Example:
        >>> set_labels(["1;Ma tâche;ancien"], "1", ["nouveau", "important"])
        (True, [(1, 'Ma tâche', ['nouveau', 'important'])])
    """
    try:
        task_id = int(task_id)
    except ValueError:
        return False, []
        
    parsed_tasks = parse_tasks(tasks)
    found = False
    
    for i, (tid, desc, labels) in enumerate(parsed_tasks):
        if tid == task_id:
            parsed_tasks[i] = (tid, desc, new_labels.copy())
            found = True
            break
    
    return found, parsed_tasks