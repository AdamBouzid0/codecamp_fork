import core

# Implémentation des différentes commandes, utilisant les fonctions contenues dans le module core
def add(details, filename, tasks):
    id = core.add(details)
    print(f"Task {id} added.")

def modify(task_id, details, filename):
    if core.modify(filename, task_id, ' '.join(details)):
        print(f"Task {task_id} modified.")
    else:
        print(f"Error: task id {task_id} not found.")

def rm(task_id, filename):
    if core.remove_task(filename, task_id):
        print(f"Task {task_id} removed.")
    else:
        print(f"Error: task id {task_id} not found.")

def show(filename):
    tasks = core.get_all_tasks(filename)
    for task_id, description in tasks:
        print(f"{task_id}: {description}")()  (id,filename,tasks)():
    tasklist = core.show(tasks)