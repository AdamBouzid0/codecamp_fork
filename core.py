import sys

def parse_tasks(tasks):
    """Transforme les lignes du fichier en une liste de (id:int, description:str)."""
    parsedTasks = []
    with open(tasks, 'r') as f:
        lines = f.readLines()
        f.close()
    for line in lines:
        parts = line.strip().split(";", 1)
        if len(parts) == 2:
            try:
                tid = int(parts[0])
                parsedTasks.append((tid, parts[1]))
            except ValueError:
                continue
    return parsedTasks


def add(details):
    """
    task lestaches.txt add <la description sur le,  reste de la ligne> : 
    ajoute au fichier lestaches.txt la ligne de la tâche, retourne son identifiant;
    """
    filename = sys.argv[1]
    newId = 0
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    if lines: 
        lastId = lines[-1].split(';')[0]
        newId = int(lastId) + 1
    
    newTask = f"{newId};{details}\n"

    with open(filename, "a") as f:
        f.writelines(newTask)
        f.close()
    
    return newId


def modify(id, details):
    """
    task lestaches.txt modify id <la nouvelle description sur le reste de la ligne> :
    remplace la description de la tâche d’identifiant id dans lestaches.txt, renvoie un message
    d’erreur si la tâche n’est pas trouvée
    """
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_lines = []
    found = False

    for line in lines:
        parts = line.strip().split(";", 1)
        if int(parts[0])!=id:
            new_lines.append(line)
        else:
            found = True
            new_lines.append(parts[0] + ";" + details + "\n")
            
    with open(filename, 'w') as f:
        f.writelines(new_lines)
        
    if not found:
        print("La tâche n'a pas été trouvée")
    

def rm(id):
    """
    task lestaches.txt rm id : retire la ligne du fichier lestaches.txt contenant la tâche
    d’identifiant id, renvoie un message d’erreur si la tâche n’est pas trouvée ;
    """
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_lines = []
    found = False

    for line in lines:
        parts = line.strip().split(";", 1)
        if int(parts[0])!=id:
            new_lines.append(line)
        else:
            found = True
            
    with open(filename, 'w') as f:
        f.writelines(new_lines)
        
    if not found:
        print("La tâche n'a pas été trouvée")
            

def show1(id):
    """
    task lestaches.txt show : affiche la liste des tâches du fichier sous la forme ci-dessous en
    les triant par leurs identifiants.
    """
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readLines()
    
    for line in lines.splitlines():
        idLine = int(line.split(';')[0])
        if idLine == id:
            description = line.split(';')[1]

    return description

def show(tasks):
    """
    Print tasks in a simple table.
    """

    maxDesc = 14
    for tid, desc in tasks:
        if len(desc) > maxDesc:
            maxDesc = len(desc)

    parsed = sorted(parse_tasks(tasks), key=lambda x: x[0])
    print("+-----+" + "-"*maxDesc + "+")
    print("| id  | description    |")
    print("+-----+" + "-"*maxDesc + "+")
    for tid, desc in parsed:
        print(f"| {tid:<3} | {desc:<int(maxDesc)} |")
        print("+-----+" + "-"*maxDesc + "+")