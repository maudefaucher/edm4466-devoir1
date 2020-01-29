### BONJOUR MAUDE, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

### TOUT D'ABORD, TON SCRIPT DEVAIT SE TERMINER PAR ".py" -> ASSEZ IMPORTANT POUR QUE PYTHON PUISSE L'EXÉCUTER

### TRÈS INTÉRESSANTE EXPLORATION DE TES VARIABLES, CI-DESSOUS! :)

url = "https://montrealcampus.ca?p=30145"
print(url)
moitié1 = "https://montrealcampus.ca?p="
print(moitié1)
moitié2 = "30145"
print(moitié2)
url = moitié1 + moitié2 
print(url)

numéros = list(range(20000, 30150)) ### ATTENTION: PAS D'ACCENTS DANS LES NOMS DE VARIABLE; MÊME SI ÇA FONCTIONNE, ÇA PEUT PLANTER DANS CERTAINS ENVIRONNEMENTS...
print(numéros)
print(len(numéros))
numéros.append(30150)
print(numéros, len(numéros))

# Je ne crois pas que mon utilisation de .append est correcte ici, comme j'ai ajouté 30 150 à la liste "manuellement", mais je ne comprenais pas comment le faire autrement. 
### OUI, C'EST UNE BONNE UTILISATION DE .APPEND
### ELLE N'EST PAS UTILE POUR RÉPONDRE À LA QUESTION,
### MAIS TU TESTES, TU ESSAIES, TU REGARDES CE QUE ÇA VA DONNER, ET C'EST EXCELLENT SUR LE PLAN PÉDAGOGIQUE!
### JE T'ENCOURAGE À CONTINUER! :)

print(type(moitié1))

url2 = []

for numéro in numéros : ### ACCENTS! 🙀
   bonnuméro = str(numéro)
   url2.append(moitié1 + bonnuméro)

print(url2)

print(len(numéros))

### BOOM! EXCELLENT!
### C'EST EXACTEMENT CE QUE JE VOUS DEMANDAIS DE FAIRE! BRAVO!