import json
survey = []


while True: 
    info = {}
    user = 0

    if user.lower() == 'stop':
        # int qui manque pour que le fonctionne
        break
    
    info["nom"] = input ("Entrer votre nom : ")
    info["prenom"] = input ("Entrer votre prenom : ")
    info["date"] = input ("Entrer votre date de naissance (jj/mm/aaaa) : ")
    info["couleur"] = input ("Quelle est votre couleur préférée : ")

    survey.append(info)

    # json
    with open("survey.json", "w") as file:
        json.dump(survey, file, indent=4)


    with open("survey.json", "r") as file:
        survey = json.load(file)

    # ajout pour list
    # info += ["nom"] = input ("Entrer votre nom : ")
    # info += ["prenom"] = input ("Entrer votre prenom : ")
    # info += ["animaux"] = input ("Combien d’animaux domestiques possède-vous ? ")