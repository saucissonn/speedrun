import re

with open("every.md", "r", encoding="utf-8") as f:
    contenu = f.read()

# Remplace chaque chemin sujetX-Y.py par sujetX-Y-Copie.py
nouveau_contenu = re.sub(
    r"\{\{ IDE\('exercices_python/(sujet\d+-\d+)\.py'\) \}\}",
    r"{{ IDE('exercices_python/\1-Copie.py') }}",
    contenu
)

with open("every.md", "w", encoding="utf-8") as f:
    f.write(nouveau_contenu)

print("✅ Tous les chemins ont été mis à jour dans every.md.")
