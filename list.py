import os
import json
from datetime import datetime

def lister_fichiers_png(repertoire_png, repertoire_sortie, fichier_sortie="png.json"):
    # Récupérer la liste des fichiers .png
    fichiers = [
        f for f in os.listdir(repertoire_png)
        if f.lower().endswith('.png') and os.path.isfile(os.path.join(repertoire_png, f))
    ]

    # Générer le JSON
    data = {
        "lastUpdate": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files": sorted(fichiers)
    }

    # Écrire le fichier JSON dans le répertoire de sortie
    chemin_sortie = os.path.join(repertoire_sortie, fichier_sortie)
    with open(chemin_sortie, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Fichier JSON généré : {chemin_sortie}")

# Utilisation avec tes chemins
lister_fichiers_png(
    r"C:\Users\bigde\GitCsharp\AndroJazzPianoFiles\png",
    r"C:\Users\bigde\GitCsharp\AndroJazzPianoFiles"
)
