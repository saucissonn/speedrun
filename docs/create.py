import os

for i in range(1, 49):
    md_filename = f"sj_{i}.md"
    
    if os.path.isfile(md_filename):
        with open(md_filename, "r", encoding="utf-8") as f:
            contenu = f.read()

        nouveau_texte = contenu.replace("Voir le PDF de tous sujets", "Voir le PDF de tous les sujets")

        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(nouveau_texte)

        print(f"✔️ Modifié : {md_filename}")
    else:
        print(f"⚠️ Fichier introuvable : {md_filename}")
