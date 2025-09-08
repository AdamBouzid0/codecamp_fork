import commands
from options import create_parser

# Création du parseur de ligne de commande
options = create_parser().parse_args()
try:
    # Lecture du fichier de commandes, s’il existe
    with open(options.file, 'r') as f:
        tasks = f.readlines()
    # Exécution de la commande
    if options.command == 'add':
        commands.add(' '.join(options.details), options.file, tasks)
    elif options.command == 'modify':
        commands.modify(options.id, ' '.join(options.details), options.file,
    tasks)
    elif options.command == 'rm':
        commands.rm(options.id, options.file, tasks)
    elif options.command == 'show':
        commands.show(tasks)

except FileNotFoundError:
    print(f"The file {options.file} was not found")