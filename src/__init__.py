carte_chance = {
    0:["Amende pour excès de vitesse", -15],
    1:["La banque vous verse un dividende de € 50",50],
    2:["Vous êtes imposé pour les réparations de voirie a raison de : € 40 par house et € 115 par hotel",""],
    3:["Avancez jusqu'à la case Départ",0],
    4:["Payez les frais de scolarité : € 150",-150],
    5:["Rendez-vous Rue de la Paix",0],
    6:["Rendez-vous à l'Avenue Henri-Martin. Si vous passez par Départ recevez € 200",0],
    7:["Faites des réparations dans toutes vos houses : € 25 et € 100 par hôtel",""],
    8:["Avancez au Bd de la Villette. Si vous passez par Départ recevez € 200",0],
    9:["Allez à la gare de Lyon. Si vous passez par Départ recevez € 200",0],
    10:["Votre immeuble et votre prêt rapportent. Vous devez toucher € 150",150],
    11:["Allez en prison. Ne franchissez pas la case Départ. Ne touchez pas € 200",0],
    12:["Reculez de 3 squares",0],
    13:["Amende pour ivresse : € 20",-20],
    14:["Vous avez gagné le price de mots croisés. Recevez € 100",100],
    15:["Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.",0]
}



carte_caisse_communaute = {

    0:["C'est votre jour anniversaire chaque joueur doit vous donner € 10",""],
    1:["Payer l'hôpital € 100",-100],
    2:["Vous avez gagné le 2nd price de beauté. Recevez € 10",10],
    3:["Erreur de la banque en votre faveur recevez € 200",200],
    4:["Recevez votre intérêt sur l'emprunt à 7% , € 25",25],
    5:["Payez un amende de € 10 ou bien tirez un carte 'CHANCE'",""],
    6:["Retournez a Belleville",0],
    7:["Recevez votre revenu annuel € 100",100],
    8:["Allez en prison .Avancez tout droit en prison .Ne passez pas par la case départ . Ne recevez pas € 200",0],
    9:["Placez-vous sur la case Départ",0],
    10:["Payez la note du médecin € 50",-50],
    11:["Payez votre police d'assurance s'élevant à € 50",-50],
    12:["Les contributions vous remboursent la somme de € 20",20],
    13:["Vous héritez de € 100",100],
    14:["La vente de votre stock vous rapporte € 50",50],
    15:["Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.",0]
}

squares = {
    0:"Case Départ",            # 0
    1:"Belleville",             # 1
    2:"Caisse de Communauté",   # 2
    3:"Lecourbe",               # 3
    4:"Impôts",                 # 4
    5:"Gare Montparnasse",      # 5
    6:"Vaugirard",              # 6
    7:"Carte Chance",           # 7
    8:"Courcelles",             # 8
    9:"Républiques",            # 9
    10:"Simple Visite",          # 10
    11:"La Villette",            # 11
    12:"Cie électricité",        # 12
    13:"Neuilly",                # 13
    14:"Paradis",                # 14
    15:"Gare de Lyon",           # 15
    16:"Mozart",                 # 16
    17:"Caisse de Communauté",   # 17 
    18:"Saint-Michel",           # 18
    19:"Pigalle",                # 19
    20:"Parc Gratuit",           # 20
    21:"Matignon",               # 21
    22:"Carte Chance",           # 22
    23:"Malesherbes",            # 23
    24:"Henri-Martin",           # 24
    25:"Gare du Nord",           # 25
    26:"Saint-Honoré",           # 26
    27:"La Bourse",              # 27
    28:"Cie des Eaux",           # 28
    29:"La Fayette",             # 29
    30:"Allez en Prison",        # 30
    31:"Breteuil",               # 31
    32:"Foch",                   # 32
    33:"Caisse de Communauté",   # 33
    34:"Capucines",              # 34
    35:"Gare Saint-Lazare",      # 35
    36:"Carte Chance",           # 36
    37:"Champs-élysées",         # 37
    38:"Taxe de Luxe",           # 38
    39:"La Paix",                # 39
    40:"Prison",                 # 40
    41:"Les stations",              # 5 + 15 + 25 + 35 (41)
    42:"Les Cies",               # 12 + 28 (42)
    43:"Brun",                   # 1 + 3 (43)
    44:"Bleu clair",             # 6 + 8 + 9 (44)
    45:"Violet",                 # 11 + 13 + 14 (45)
    46:"Orange",                 # 16 + 18 + 19 (46)
    47:"Rouge",                  # 21 + 23 + 24 (47)
    48:"Jaune",                  # 26 + 27 + 29 (48)
    49:"Vert",                   # 31 + 32 + 34 (49)
    50:"Bleu foncé"              # 37 + 39 (50)
}
companies = {
    12 : {
        "name": "Compagnie de distribution d'électricité",
        "price": 150,
        "mortgage":75,
        "color": 42,
        "owner": ""
    },
    
    28: {
        "name": "Compagnie de distribution des eaux",
        "price": 150,
        "mortgage":75,
        "color": 42,
        "owner": ""
    }
}


stations = {
    5: {
        "name": "Gare Montparnasse",
        "price": 200,
        "loyer": [25,50,100,200],
        "mortgage":100,
        "color": 41,
        "owner": ""
    }, 
        
    15: {
        "name": "Gare de Lyon",
        "price": 200,
        "loyer": [25,50,100,200],
        "mortgage":100,
        "color": 41,
        "owner": ""
    },

    25: {
        "name": "Gare du Nord",
        "price": 200,
        "loyer": [25,50,100,200],
        "mortgage":100,
        "color": 41,
        "owner": ""
    },
        
    35: {
        "name": "Gare Saint-Lazare",
        "price": 200,
        "loyer": [25,50,100,200],
        "mortgage":100,
        "color": 41,
        "owner": ""
    }
}


lots = {
    1: {
        "name": "Boulevard de Belleville",
        "price": 60,
        "loyer": [2,10,30,90,160,250],
        "mortgage":30,
        "house":50,
        "color": 43,
        "owner": ""
    },

    3: {
        "name": "Rue Lecourbe",
        "price": 60,
        "loyer": [4,20,60,180,320,450],
        "mortgage":30,
        "house":50,
        "color": 43,
        "owner": ""
    },

    6: {
        "name": "Rue Vaugirard",
        "price": 100,
        "loyer": [6,30,90,270,400,550],
        "mortgage":50,
        "house":50,
        "color": 44,
        "owner": ""
    },

    8: {
        "name": "Rue de Courcelles",
        "price": 100,
        "loyer": [6,30,90,270,400,550],
        "mortgage":50,
        "house":50,
        "color": 44,
        "owner": ""
    },        
    
    9: {
        "name": "Avenue de la République",
        "price": 120,
        "loyer": [8,40,100,300,450,600],
        "mortgage":60,
        "house":50,
        "color": 44,
        "owner": ""
    },
    
    11: {
        "name": "Boulevard de la Villette",
        "price": 140,
        "loyer": [10,50,150,450,625,750],
        "mortgage":70,
        "house":100,
        "color": 45,
        "owner": ""
    },

    13: {
        "name": "Avenue de Neuilly",
        "price": 140,
        "loyer": [10,50,150,450,625,750],
        "mortgage":70,
        "house":100,
        "color": 45,
        "owner": ""
    },
    
    14: {
        "name": "Rue de Paradis",
        "price": 160,
        "loyer": [12,60,180,500,700,900],
        "mortgage":80,
        "house":100,
        "color": 45,
        "owner": ""
    },

    16: {
        "name": "Avenue Mozart",
        "price": 180,
        "loyer": [14,70,200,550,750,950],
        "mortgage":90,
        "house":100,
        "color": 46,
        "owner": ""
    },    
    
    18: {
        "name": "Boulevard St Michel",
        "price": 180,
        "loyer": [14,70,200,550,750,950],
        "mortgage":90,
        "house":100,
        "color": 46,
        "owner": ""
    },    
    
    19: {
        "name": "Place Pigalle",
        "price": 200,
        "loyer": [16,80,220,600,800,1000],
        "mortgage":100,
        "house":100,
        "color": 46,
        "owner": ""
    },    

    21: {
        "name": "Avenue Matignon",
        "price": 220,
        "loyer": [18,90,250,700,875,1050],
        "mortgage":110,
        "house":150,
        "color": 47,
        "owner": ""
    },    
    
    23: {
        "name": "Boulevard Malesherbes",
        "price": 220,
        "loyer": [18,90,250,700,875,1050],
        "mortgage":110,
        "house":150,
        "color": 47,
        "owner": ""
    },    
    
    24: {
        "name": "Avenue Henri Martin",
        "price": 240,
        "loyer": [20,100,300,750,925,1100],
        "mortgage":120,
        "house":150,
        "color": 47,
        "owner": ""
    },       

    26: {
        "name": "Faubourg St Honoré",
        "price": 260,
        "loyer": [22,110,330,800,975,1150],
        "mortgage":130,
        "house":150,
        "color": 48,
        "owner": ""
    },

    27: {
        "name": "Place de la Bourse",
        "price": 260,
        "loyer": [22,110,330,800,975,1150],
        "mortgage":130,
        "house":150,
        "color": 48,
        "owner": ""
    },
          
    29: {
        "name": "Rue de la Fayette",
        "price": 280,
        "loyer": [24,120,360,850,1025,1200],
        "mortgage":140,
        "house":150,
        "color": 48,
        "owner": ""
    },    
    
    31: {
        "name": "Avenue de Breteuil",
        "price": 300,
        "loyer": [26,130,390,900,1100,1275],
        "mortgage":150,
        "house":200,
        "color": 49,
        "owner": ""
    },    
        
    32: {
        "name": "Avenue Foch",
        "price": 300,
        "loyer": [26,130,390,900,1100,1275],
        "mortgage":150,
        "house":200,
        "color": 49,
        "owner": ""
    },    
        
    34: {
        "name": "Boulevard des Capucines",
        "price": 320,
        "loyer": [28,150,450,1000,1200],
        "mortgage":160,
        "house":200,
        "color": 49,
        "owner": ""
    },      

    37: {
        "name": "Avenue des Champs-Elisées",
        "price": 350,
        "loyer": [35,175,500,1100,1300,1500],
        "mortgage":175,
        "house":200,
        "color": 50,
        "owner": ""
    },    
        
    39: {
        "name": "Rue de la Paix",
        "price": 400,
        "loyer": [50,200,600,1400,1700,2000],
        "mortgage":200,
        "house":200,
        "color": 50,
        "owner": ""
    }
}    



# Une compagnie: 4 fois le montant des dés
# Deux compangnies: 10 fois le montant des dés 


# name des différentes squares 
# @case = ("Case Départ",            # 0
#          "Belleville",             # 1
#          "Caisse de Communauté",   # 2
#          "Lecourbe",               # 3
#          \"Impôts",                 # 4
#          "Gare Montparnasse",      # 5
#          "Vaugirard",              # 6
#          "Carte Chance",           # 7
#          "Courcelles",             # 8
#          "Républiques",            # 9
#          "Simple Visite",          # 10
#          "La Villette",            # 11
#          "Cie électricité",        # 12
#          "Neuilly",                # 13
#          "Paradis",                # 14
#          "Gare de Lyon",           # 15
#          "Mozart",                 # 16
#          "Caisse de Communauté",   # 17 
#          "Saint-Michel",           # 18
#          "Pigalle",                # 19
#          "Parc Gratuit",           # 20
#          "Matignon",               # 21
#          "Carte Chance",           # 22
#          "Malesherbes",            # 23
#          "Henri-Martin",           # 24
#          "Gare du Nord",           # 25
#          "Saint-Honoré",           # 26
#          "La Bourse",              # 27
#          "Cie des Eaux",           # 28
#          "La Fayette",             # 29
#          \"Allez en Prison",        # 30
#          "Breteuil",               # 31
#          "Foch",                   # 32
#          "Caisse de Communauté",   # 33
#          "Capucines",              # 34
#          "Gare Saint-Lazare",      # 35
#          "Carte Chance",           # 36
#          "Champs-élysées",         # 37
#          "Taxe de Luxe",           # 38
#          "La Paix",                # 39
#          "Prison",                 # 40
#          "Les stations",              # 5 + 15 + 25 + 35 (41)
#          "Les Cies",               # 12 + 28 (42)
#          "Brun",                   # 1 + 3 (43)
#          "Bleu clair",             # 6 + 8 + 9 (44)
#          "Violet",                 # 11 + 13 + 14 (45)
#          \"Orange",                 # 16 + 18 + 19 (46)
#          "Rouge",                  # 21 + 23 + 24 (47)
#          "Jaune",                  # 26 + 27 + 29 (48)
#          "Vert",                   # 31 + 32 + 34 (49)
#          "Bleu foncé"              # 37 + 39 (50)
#          );


#          Cartes Chances
# Amende pour excès de vitesse : F 1.500
# La banque vous verse un dividende de F 5.000
# Vous êtes imposé pour les réparations de voirie a raison de : F 4.000 par house et F 11.500 par hotel
# Avancez jusqu'à la case "Départ"
# Payez les frais de scolarité : F 15.000
# Rendez-vous Rue de la Paix (nu = F 5.000 Hôtel = F 200.000)
# Rendez-vous à l'Avenue Henri-Martin (nu = F 2.000 Hôtel = F 110.000). Si vous passez par "Départ" recevez F 20.000
# Faites des réparations dans toutes vos houses : F 2.500 et F 10.000 par hôtel
# Avancez au Bd de la Villette (nu = F 1.000 Hôtel = F 75.000). Si vous passez par "Départ" recevez F 20.000
# Allez à la gare de Lyon (1 gare = F 2.500;4 stations = F 20.000). Si vous passez par "Départ" recevez F 20.000
# Votre immeuble et votre prêt rapportent. Vous devez toucher F 15.000
# Allez en prison. Ne franchissez pas la case "Départ". Ne touchez pas F 20.000
# Reculez de 3 squares
# Amende pour ivresse : F 2.000
# Vous avez gagné le price de mots croisés. Recevez F 10.000
# Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.
 
# Cartes Caisses de Communauté
 
# C'est votre jour anniversaire chaque joueur doit vous donner F 1.000
# Payer l'hôpital F 10.000
# Vous avez gagné le 2nd price de beauté. Recevez F 1.000
# Erreur de la banque en votre faveur recevez F 20.000
# Recevez votre intérêt sur l'emprunt à 7% , F 2.500
# Payez un amende de F 1.000 ou bien tirez un carte "CHANCE"
# Retournez a Belleville(nu = F 200 Hôtel = F 25.000)
# Recevez votre revenu annuel F 10.000
# Allez en prison .Avancez tout droit en prison .Ne passez pas par la case départ . Ne recevez pas F 20.000
# Placez-vous sur la case " Départ"
# Payez la note du médecin F 5.000
# Payez votre police d'assurance s'élevant à F 5.000
# Les contributions vous remboursent la somme de F 2.000
# Vous héritez de F 10.000
# La vente de votre stock vous rapporte F 5.000
# Vous êtes libéré de prison .Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.
# Boulevard de Belleville
# Terrain nu : 2€
# 1 houses : 10€
# 2 houses : 30€
# 3 houses : 90€
# 4 houses : 160€
# hotel : 250€

# Rue Lecourbe
# Terrain nu : 4€
# 1 houses : 20€
# 2 houses : 60€
# 3 houses : 180€
# 4 houses : 320€
# hotel : 450€

# Rue Vaugirard
# Terrain nu : 6€
# 1 houses : 30€
# 2 houses : 90€
# 3 houses : 270€
# 4 houses : 400€
# hotel : 550€

# Avenue de la République
# Terrain nu : 8€
# 1 houses : 40€
# 2 houses : 100€
# 3 houses : 300€
# 4 houses : 450€
# hotel : 600€

# Rue de Courcelles
# Terrain nu : 6€
# 1 houses : 30€
# 2 houses : 90€
# 3 houses : 270€
# 4 houses : 400€
# hotel : 550€

# Avenue de Neuilly
# Terrain nu : 10€
# 1 houses : 50€
# 2 houses : 150€
# 3 houses : 450€
# 4 houses : 625€
# hotel : 750€

# Rue de Paradis
# Terrain nu : 12€
# 1 houses : 60€
# 2 houses : 180€
# 3 houses : 500€
# 4 houses : 700€
# hotel : 900€

# Boulevard de la Villette
# Terrain nu : 10€
# 1 houses : 50€
# 2 houses : 150€
# 3 houses : 450€
# 4 houses : 625€
# hotel : 750€

# Avenue Mozart
# Terrain nu : 14€
# 1 houses : 70€
# 2 houses : 200€
# 3 houses : 550€
# 4 houses : 760€
# hotel : 950€

# Place Pigalle
# Terrain nu : 16€
# 1 houses : 80€
# 2 houses : 220€
# 3 houses : 600€
# 4 houses : 800€
# hotel : 1000€

# Boulevard St Michel
# Terrain nu : 14€
# 1 houses : 70€
# 2 houses : 200€
# 3 houses : 550€
# 4 houses : 750€
# hotel : 950€

# Boulevard Malesherbes
# Terrain nu : 18€
# 1 houses : 90€
# 2 houses : 2500€
# 3 houses : 700€
# 4 houses : 875€
# hotel : 1050€

# Avenue Henri Martin
# Terrain nu : 20€
# 1 houses : 100€
# 2 houses : 300€
# 3 houses : 750€
# 4 houses : 925€
# hotel : 1100€

# Avenue Matignon
# Terrain nu : 18€
# 1 houses : 90€
# 2 houses : 250€
# 3 houses : 700€
# 4 houses : 875€
# hotel : 1050€

# Place de la Bourse
# Terrain nu : 22€
# 1 houses : 110€
# 2 houses : 330€
# 3 houses : 800€
# 4 houses : 975€
# hotel : 1150€

# Faubourg St Honoré
# Terrain nu : 22€
# 1 houses : 110€
# 2 houses : 330€
# 3 houses : 800€
# 4 houses : 975€
# hotel : 1150€

# Rue de la Fayette
# Terrain nu : 24€
# 1 houses : 120€
# 2 houses : 360€
# 3 houses : 850€
# 4 houses : 1025€
# hotel : 1200€

# Avenue Foch
# Terrain nu : 26€
# 1 houses : 130€
# 2 houses : 390€
# 3 houses : 900€
# 4 houses : 1100€
# hotel : 250€ 

# Avenue de Breteuil
# Terrain nu : 26€
# 1 houses : 130€
# 2 houses : 390€
# 3 houses : 900€
# 4 houses : 1100€
# hotel : 1275€

# Boulevard des Capucines
# Terrain nu : 28€
# 1 houses : 150€
# 2 houses : 450€
# 3 houses : 1000€
# 4 houses : 1200€
# hotel : 1400€

# Avenue des Champs-Elisées
# Terrain nu : 35€
# 1 houses : 175€
# 2 houses : 500€
# 3 houses : 1100€
# 4 houses : 1300€
# hotel : 1500€

# Rue de la Paix
# Terrain nu : 50€
# 1 houses : 200€
# 2 houses : 600€
# 3 houses : 1400€
# 4 houses : 1700€
# hotel : 2000€

# stations
# 1 gare : 25€
# 2 gare : 50€
# 3 gare : 100€
# 4 gare : 200€

# companies distribution des eaux et d'électricité
# Une compagnie: 4 fois le montant des dés
# Deux compangnies: 10 fois le montant des dés 