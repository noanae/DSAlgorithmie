from pathlib import Path
import string

# reprise du code dans le cour pour lire le contenu d'un fichier
# Je charge le contenu du fichier grâce au path
file_path = Path("Users\tancr\OneDrive\Bureau\DSalgo\DSAlgorithmie.txt")

# Lecture du fichier
if file_path.exists():
    with file_path.open(mode='r', encoding='utf-8') as file:
        for line in file:
            print(line.strip()) 


ancienMessage = """Strawberry quince olive fig bliss peach ximenia victoria grape kiwi cherry
feijoa cloud fig nectarine guava blackberry papaya kumquat eggplant watermelon
blackberry strawberry rhubarb lime feijoa eggplant ice apricot nutmeg tamarillo
ugni victoria victoria huckleberry yellow zest elderflower zucchini nebula
apricot ugly jackfruit ugli raspberry zinfandel feijoa vanilla ivory ugli
quandary ximenia blackberry tamarind quince kale avocado oasis eggplant jujube
elderberry mulberry raspberry elderberry feijoa nut abbey kiwi jackfruit ugli
yuzu blackberry mulberry orange waxberry quince vine marvel jackfruit
strawberry kale guava mandarin ugli mulberry nutmeg serene zest dragonfruit
jujube victoria zest kumquat hawthorn waxberry ocean xerophyte lime fig
cantaloupe nutmeg feijoa apple tamarillo lychee hawthorn vine tamarillo palm
kumquat elderflower kale ugni nut kiwi wildberry fennel garden gooseberry
mandarin hawthorn kiwi date xerophyte elderflower raspberry elderberry pearl
onion kale ugni strawberry zucchini banana hawthorn mulberry feast tangerine
jackfruit vanilla indian ugni olive satsuma ugly papaya guava eagle nectarine
wildberry wildberry lemon dragonfruit saffron haven blackberry strawberry grape
jujube tamarind watermelon quandong hawthorn persimmon lemon harmony kale
elderflower vine date persimmon quandong dragonfruit quartz mulberry quince
zinfandel kale cranberry lychee jade tamarillo papaya gooseberry ugly eggplant
elderberry jackfruit cranberry elderberry cactus honeydew vine kale tangerine
persimmon rasp zest dragonfruit jujube blackberry ximenia daisy cantaloupe
papaya hawthorn nut nectarine apricot durian hawthorn mango meadow orange
indian zinfandel lychee tamarillo ugni zest fennel satsuma ugli jackfruit
elderberry jazz durian jujube grape mulberry xerophyte yam kumquat apple
cranberry quest watermelon dragonfruit apricot jujube papaya orange mandarin
rhubarb watermelon banana falcon apple yuzu kumquat elderberry nectarine apple
yuzu satsuma dragonfruit elderflower xerophyte cantaloupe hawthorn luna jujube
elderflower jackfruit zest yam dragonfruit banana rasp date rain kale tamarillo
tamarillo lime ximenia raspberry strawberry fennel ximenia lime lagoon satsuma
grape strawberry zest ugly nut indian cherry kale zinfandel huckleberry
tamarillo zinfandel dawn quandong blueberry blueberry raspberry banana papaya
satsuma ximenia watermelon glow dragonfruit zucchini durian guava olive yam
papaya nest eggplant strawberry cranberry indian strawberry rasp watermelon
koala nut cantaloupe feijoa xerophyte quince apricot river tamarillo orange
ugly zest jujube lychee kiwi mandarin mandarin breeze avocado wildberry
zucchini jackfruit gooseberry durian waxberry wildberry echo nut cherry
quandong lychee blackberry huckleberry amber mandarin xigua quandong banana
mango"""

motsDeRemplissage =  {'rhubarb', 'quince', 'watermelon', 'ximenia', 'nut', 'zucchini',
'blackberry', 'vine', 'cranberry',
 'durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry',
'tangerine', 'satsuma',
 'kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado',
'xigua', 'ugly',
 'waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel',
'raspberry', 'guava',
 'indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry',
'hawthorn', 'apple',
 'nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry',
'quandong', 'zest',
 'wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg',
'persimmon', 'mandarin', 'olive',
 'lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit',
'gooseberry', 'vanilla',
 'mulberry', 'kumquat', 'peach', 'feijoa'}

# Je reprend ma chaine de caractère "ancien_message" en les mettant en minuscule pour être sur qu'il n'y ai pas de majuscules.
# J'utilise la méthode .split pour bien séparer les mots entre eux et faire en sorte que les retours à la lignes ne posent pas problèmes.
ancienMessageRanger = ancienMessage.lower().split()

# Ici on supprimes les mots de remplissages dans notre anciens messages pour que l'on puisse retrouvé les clés 
# la fonction .sorted() va me permettre de trier dans l'ordre alphabétique
# comme je ne pouvais pas soustraire une liste et un ensemble j'ai du utiliser une compréhension de liste : https://www.delftstack.com/fr/howto/python/python-list-subtraction/
clés = sorted([mot for mot in ancienMessageRanger if mot not in motsDeRemplissage])

print("Mots-clés extraits et triés :", clés)


x = ['abbey', 'amber', 'bliss', 'breeze', 'cactus', 'cloud', 'daisy', 'dawn', 'eagle', 'echo', 'falcon', 'feast', 'garden', 'glow', 'harmony', 'haven', 'ice', 'ivory', 'jade', 'jazz', 'koala', 'lagoon', 'luna', 'marvel', 'meadow', 'nebula', 'nest', 'oasis', 'ocean', 'palm', 'pearl', 'quartz', 'quest', 'rain', 'river', 'serene']

# Fonction trouver sur ce site : https://stackoverflow.com/questions/63875471/enumerate-with-letters-instead-of-numbers
# En reprenant cette ceci j'ai donc ajouter une condition qui dit qu'une fois dépasser 26 donc la lettre Z on switch de 
# string.ascii_uppercase[i] (les lettres) à la méthode énumerate (pour les chiffres)
for i, mots in enumerate(x):
    if i < 26:
        print((string.ascii_uppercase[i], mots))
    else:  
        print((i - 25, mots))  


