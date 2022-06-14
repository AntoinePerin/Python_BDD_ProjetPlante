import pymysql.cursors   

serveur="94.247.183.221"
usr='pc'
passwd='pc-bdd1304'
bdd='projetplante'

# I- Connexion BDD

def dbConnection():
    return pymysql.connect(host=serveur,
                    user=usr,
                    password=passwd,
                    db=bdd,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor) 


# II- Enregistrer Mesure DB

    # II-1 Fonction enregistrer mesure DB

def enregistrerMesures(date,humidite,temperature,luminosite,co2,adressMac):
    
    ENREGISTRER_MESURES = "INSERT INTO mesures(Date_mesure,Humidite_mesure,\
        Temperature_mesure,Luminosite_mesure,CO2_mesure,Adresse_Mac_Plante) VALUES(%s,%s,%s,%s,%s,%s)"
    
    connection = dbConnection()
    
    with connection.cursor() as cursor:
        cursor.execute(ENREGISTRER_MESURES,(date,humidite,temperature,luminosite,co2,adressMac))
        
    connection.commit()
    connection.close()

    # II-2 Test enregistrer mesure DB   
    
date = "2022-04-13 19:59:00"
humidite="15"
temperature="15"
luminosite="15"
co2="15"
adressMac="test3"

#enregistrerMesures(date, humidite, temperature, luminosite, co2, adressMac)

# III- Inserer nouvelle plante DB

    # III-1 Fonction inserer plante
    
def insererPlante(adresseMac,nomPlante,dateDePlantation,description,NiveauIrrigation,SeuilHumidite):
    INSERER_PLANTE="INSERT INTO plante(Adresse_Mac_Plante, Libelle_plante, \
        Date_plantation_plante, Description_plante,Niveau_irrigation_plante,Seuil_humidite_plante) VALUES (%s,%s,%s,%s,%s,%s);"
    connection = dbConnection()
    
    with connection.cursor() as cursor:
        cursor.execute(INSERER_PLANTE,(adresseMac,nomPlante,dateDePlantation,description,NiveauIrrigation,SeuilHumidite))
        
    connection.commit()
    connection.close()
    
    # III-2 Test Fonction inserer plante
    
adresseMac="test54"
nomPlante="JonquilleTest3"
dateDePlantation="2022-05-18 19:59:00"
description="Ceci est la plus belle des jonquilles test"
NiveauIrrigation="4"
SeuilHumidite="50"

#insererPlante(adresseMac,nomPlante,dateDePlantation,description,NiveauIrrigation,SeuilHumidite)

# IV- Inserer irrigation
    
    # IV-1 Fonction inserer irrigation
    
def insererIrrigation(dateIrrigation,automatiqueIrrigation,adresseMac):
    INSERER_IRRIGATION="INSERT INTO irrigation(Date_irrigation,automatique_irrigation,Adresse_Mac_plante) VALUES(%s,%s,%s);"
    connection = dbConnection()
        
    with connection.cursor() as cursor:
        cursor.execute(INSERER_IRRIGATION,(dateIrrigation,automatiqueIrrigation,adresseMac))
            
    connection.commit()
    connection.close()
    
    # IV-2 test Fonction inserer irrigation

automatiqueIrrigation="0" #irrigation automatique = 1 et irrigation manuelle = 0
dateIrrigation="2022-05-18 19:59:00"
adresseMac="test3"

#insererIrrigation(dateIrrigation,automatiqueIrrigation,adresseMac)

# V- Recuperer seuil d'humidité d'une plante

    # V-1 Fonction recuperer seuil d'humidité

def recupererSeuilHumidite(adresseMac):
    RECUPERER_SEUIL="SELECT Seuil_humidite_plante FROM plante WHERE Adresse_Mac_Plante =%s"
    connection = dbConnection()
        
    with connection.cursor() as cursor:
        cursor.execute(RECUPERER_SEUIL,(adresseMac))
        
    result = cursor.fetchone() 
    print(result) #tu recuperes un objet json, il faut le deserialiser pour avoir le seuil seul
            
    connection.commit()
    connection.close()
    
    # V-2 test Fonction recuperer seuil d'humidité
    
adresseMac="test3"
#recupererSeuilHumidite(adresseMac)

# VI- Recuperer le niveau d'arrossage pour une plante

    # VI-1 Fonction recuperer niveau arrosage
def recupererNiveauArrossage(adresseMac):
    RECUPERER_NIVEAU="SELECT Niveau_irrigation_plante FROM plante WHERE Adresse_Mac_Plante =%s"
    connection = dbConnection()
        
    with connection.cursor() as cursor:
        cursor.execute(RECUPERER_NIVEAU,(adresseMac))
        
    result = cursor.fetchone()
    print(result) #tu recuperes un objet json, il faut le deserialiser pour avoir le seuil seul
            
    connection.commit()
    connection.close()
    
    # VI-2 test Fonction recuperer niveau arrosage
    
adresseMac="test54"
#recupererNiveauArrossage(adresseMac)

