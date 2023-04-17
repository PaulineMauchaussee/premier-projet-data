import pandas as p
import datetime



file_path ="clients.csv"
data = p.read_csv(file_path)
print(data.head())


#Afficher les informations générales du DataFrame(le tableau)
data.info()

#Afficher le nombre de personnes par profession
profession = data["profession"].value_counts()
print(profession)

# Afficher le nombre de personnes par pays
pays = data ["country"].value_counts()
print(pays)

# Afficher les 10 premières personnes dont le nom de famille commence par la lettre 'D
personne_d = data[data["lastname"].str.startswith("D")].head(10)
print(personne_d)

# Créer un nouveau DataFrame contenant uniquement les colonnes firstname, lastname et email
# premier crochet = accès à une partie du tableau et second crochet un filtre 
new_data = data[["firstname" , "lastname" , "email"]]
print(new_data.head())

# Trier le DataFrame par ordre alphabétique croissant des noms de famille
sorted_data = data.sort_values(by=["lastname"])
print(sorted_data)


# Sauvegarder les données triées dans un nouveau fichier CSV
# 
sorted_data.to_csv("sorted_data.csv" , index=False)

#Trouver la ville la plus fréquente dans le fichier
most_common_city = data["city"].mode().iloc[0]

# Filtrer les personnes travaillant dans une profession spécifique, par exemple "DataScientist"
data_scientists = data[data["profession"]=="firefighter"]
print(data_scientists)

# Calculer l'age moyen par profession
data['birthdate'] = p.to_datetime(data['birthdate'], format="%m-%d-%Y")

def calcule_age(birthdate):
    #importer datetime en haut du code 
    today = datetime.datetime.now()
    # on soustrait l'année de naissance à l'année actuelle et on soustrait un an si la date  d'anniversaire est passée
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

data['age'] = data['birthdate'].apply(calcule_age)
print(data['age'])
age_par_profession = data.groupby('profession')['age'].mean()
print(age_par_profession)

#Calculer le salaire moyen par profession
#groupby = je regroupe par 
salaire_moyen_profession = data.groupby("profession")["salary"].mean()
print(salaire_moyen_profession)

#Afficher les personnes ayant un salaire supérieur à un montant donné, par exemple 5000
salaire_sup = data[data["salary"]> 5000]
print(salaire_moyen_profession)

#Afficher le pourcentage de personnes par pays
#le nombre de personne dans un pays/par nombre total de personnes dans la table 
pourcentage_pays =  data["country"].value_counts(normalize=True) * 100
print(pourcentage_pays)

#: Trouver le salaire le plus élevé et le plus bas par pays
salaire_max = data.groupby("country")["salary"].max()
salaire_min = data.groupby("country")["salary"].min()
print(salaire_max)
print(salaire_min)






