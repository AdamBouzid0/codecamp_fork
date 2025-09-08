import sys
import os

def read_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    id_, desc = line.strip().split(" ", 1)
                    tasks.append({"id": int(id_), "desc": desc})
    return tasks

def write_tasks(filename, tasks):
    with open(filename, "w", encoding="utf-8") as f:
        for task in sorted(tasks, key=lambda t: t["id"]):
            f.write(f"{task['id']} {task['desc']}\n")

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(filename, description):
    tasks = read_tasks(filename)
    new_id = get_next_id(tasks)
    tasks.append({"id": new_id, "desc": description})
    write_tasks(filename, tasks)
    print(new_id)

def modify_task(filename, id_, new_desc):
    tasks = read_tasks(filename)
    found = False
    for task in tasks:
        if task["id"] == id_:
            task["desc"] = new_desc
            found = True
            break
    if found:
        write_tasks(filename, tasks)
    else:
        print("Erreur : tâche non trouvée.", file=sys.stderr)

def remove_task(filename, id_):
    tasks = read_tasks(filename)
    new_tasks = [task for task in tasks if task["id"] != id_]
    if len(new_tasks) == len(tasks):
        print("Erreur : tâche non trouvée.", file=sys.stderr)
    else:
        write_tasks(filename, new_tasks)

def show_tasks(filename):
    tasks = read_tasks(filename)
    for task in sorted(tasks, key=lambda t: t["id"]):
        print(f"{task['id']}: {task['desc']}")

def main():
    filename = sys.argv[1]
    command = sys.argv[2]

    if command == "add":
        description = " ".join(sys.argv[3:])
        add_task(filename, description)
    elif command == "modify":
        try:
            id_ = int(sys.argv[3])
        except ValueError:
            print("Erreur : id invalide.")
            return
        new_desc = " ".join(sys.argv[4:])
        modify_task(filename, id_, new_desc)
    elif command == "rm":
        if len(sys.argv) < 4:
            print("Usage: task <fichier> rm <id>")
            return
        try:
            id_ = int(sys.argv[3])
        except ValueError:
            print("Erreur : id invalide.", file=sys.stderr)
            return
        remove_task(filename, id_)
    elif command == "show":
        show_tasks(filename)
    else:
        print("Commande inconnue.")

if __name__ == "__main__":
    main()