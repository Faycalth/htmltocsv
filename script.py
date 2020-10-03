#script qui va transformer le fichier "donneeshtml.html" (tiré du site labonnealternace.com) en fichier csv
import os

#Saisie utilisateur
try: 
    nom_fichier = str(input("Entrez le nom du fichier à parcourir (avec l'extension html) :\n"))
    if os.path.splitext(nom_fichier)[1] != ".html":
        raise NameError("ErreurExtension")
except NameError:
    print("Le fichier n'a pas une extension html")
    raise
else: 
    nom_fichier_src = os.path.splitext(nom_fichier)[0]+".html"
    nom_fichier_csv = os.path.splitext(nom_fichier)[0]+".csv"
    #Ouverture du fichier
    with open(nom_fichier_src, "r") as fichier_src, open(nom_fichier_csv, "w") as fichier_csv:

        fichier_csv.write("Description, Ville, Distance (Lyon), Nom de l'entreprise\n") #métadonnée
        
        #Parcours du fichier
        ligne = fichier_src.read()

        for lignes in ligne.split("{") :
            for data in lignes.split(","):
                
                if '"naf_text"' in data : 
                    data = data.split(":") #séparation de la donnée et de la métadonnée
                    if '"' in data[1]:
                        data[1] = data[1].replace('\"', "") #retirer les doubles quotes
                    fichier_csv.write(data[1]+", ") 
                
                if '"city"' in data :
                    data = data.split(":")
                    if '"' in data[1]:
                        data[1] = data[1].replace('\"', "")
                    fichier_csv.write(data[1]+", ")
            
                if '"distance"' in data :
                    data = data.split(":")
                    if '"' in data[1]:
                        data[1] = data[1].replace('\"', "")
                    fichier_csv.write(data[1]+", ")
                
                if '"name"' in data :
                    data = data.split(":")
                    if '"' in data[1]:
                        data[1] = data[1].replace('\"', "")
                    fichier_csv.write(data[1]+", ")
                    fichier_csv.write("\n")
        

    print("Programme terminé")