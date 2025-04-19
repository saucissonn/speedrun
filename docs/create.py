import os

# Fonction pour extraire les fonctions après chaque balise # EXERCICE n
def extract_functions_for_exercises(code):
    functions = []
    current_function = []
    inside_exercise = False
    for line in code.splitlines():
        if line.strip().startswith('# EXERCICE '):  # Identifier un nouveau bloc d'exercice
            if current_function:
                functions.append("\n".join(current_function))  # Ajouter la fonction précédente
            current_function = []
            inside_exercise = True
        elif inside_exercise and line.strip().startswith('def '):
            current_function.append(line)  # Ajouter une fonction
        elif inside_exercise and line.strip().startswith('assert '):
            continue  # Ignorer les assert dans ce cas
    if current_function:  # Ajouter la dernière fonction
        functions.append("\n".join(current_function))
    return functions

# Fonction pour remplacer le code entre les balises dans les fichiers
def replace_code_in_file(filename, function_code, start_marker, end_marker):
    with open("C:/Users/BonSaucisson/OneDrive/travail_term/NSI/SITE/docs/exercices_python/" + filename, 'r+', encoding='utf-8') as file:
        content = file.read()
        
        # Trouver les indices des bornes définies par les balises
        start_index = content.find(start_marker) + len(start_marker)
        end_index = content.find(end_marker)
        
        # Remplacer le code entre les bornes par la fonction extraite
        content = content[:start_index] + '\n' + function_code + '\n' + content[end_index:]
        
        # Réécrire le fichier avec les modifications
        file.seek(0)
        file.write(content)
        file.truncate()

# Lis le fichier all.py pour extraire les fonctions
with open("C:/Users/BonSaucisson/OneDrive/travail_term/NSI/epreuve pratique/all.py", 'r', encoding='utf-8') as f:
    all_code = f.read()

functions = extract_functions_for_exercises(all_code)

# Liste des exercices à traiter
exercises = 48

# Pour chaque exercice (de 1 à 48), insère les fonctions appropriées
for i in range(1, exercises + 1):
    # La fonction pour le sujet1 dans cet exercice
    function_code = functions[i - 1]  # La fonction pour le sujet1 (de l'exercice i)
    
    # Définir les balises de début et de fin
    start_marker = "# --- PYODIDE:code --- #"
    end_marker = "# --- PYODIDE:ignore --- #"
    
    # Calculer le fichier correspondant au sujet1
    sujet1_filename = f'sujet1-{i}.py'

    # Remplacer le code dans le fichier sujet1
    replace_code_in_file(sujet1_filename, function_code, start_marker, end_marker)

print("Les fichiers ont été mis à jour avec succès.")
