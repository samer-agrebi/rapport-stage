from pymongo import MongoClient
import spacy
client=MongoClient(host='127.0.0.1',port=27017)
db=client["wevioo"]
collection=db["cv"]
data=collection.find()
print(list(data))

from unidecode import unidecode
skills=set()
for job in collection.find():
    for y in job["skills"]:
        skills.add(unidecode(y["name"].strip()))


#keywords_section:
À_propos=["À-propos","about"]
job_description=["job-description","tes_Mission","Missions_pricipales","Missions_secondaires","outcomes","descriptif du post","ton_role"]
profil_recherché=["profil recherché","preffered experience","competencies","compétences","ce qu'on recherche"]
ce_qu_on_te_propose=["ce qu on te propose","what we offer","ce que nous offrons","salary","pourquoi nous rejoindre"]
Déroulement_des_entretiens=["Déroulement des entretiens","entretien téléphonique","test technique"]
Découvrir_équipe=["Découvrir équipe","rencontrer l'équipe","Meet the team"]

#scraping
dict_1={"about":"Redspher is Europe’s leading providers of Premium Freight services. Redspher delivers the highest possible service through our highly skilled customer service agents."}




dict_2={"job_description":"Redspher is currently looking for a Junior Legal Counsel to join its legal team in Paris for a period of six months",
        "tes_missions":"""Tu assureras le maintien et l’amélioration des dashboards opérationnels sur notre outil de visualisation Metabase "
                       "Tu participeras à l’intégration des données des nouveaux CRM (Hubspot, Salesforce) ,
                       Tu amélioreras la qualité et la cohérence des données en bdd grâce à des scripts d’uniformisation et proposeras des manières
d’optimiser l’accès aux données
Tu réaliseras des analyses selon les différents besoin des équipes (notamment en lien avec les équipes Sales et Network Development) en python et SQL
Tu pourras être amené à réaliser des scrappers en python pour enrichir la connaissance de SpaceFill sur la logistique""",
 "outcomes":"""You will understand and know perfectly our customers by end 2021with the product and sales teamyou will define clear offers and offer perimeters, rework pricing and bundling by end 2021 With the product and sales team
 "you will define the marketing strategy to first be able to measure conversion rate
 "from Invited users to paying customers and improve this conversion rate
 You will generate leads and conversion by selecting appropriate channels
You will build all marketing supports to help salespeople focus on selling """,
"Missions_principales" : """Identifier avec les Account Executives, les comptes à fort potentiel de développement et 
  imaginer les offres de collaboration adaptées aux comptes""" ,
"Missions_secondaires":"""Améliorer nos standards sales et les métriques associés (accélération de la vélocité, taux transfo / cycle)
Contribuer à la structuration de notre stratégie commerciale avec les 2 autres Team Leaders""",
"ton role":"""Directement rattaché au Head of Sales, ta mission est d’assurer que la team Sales soit la plus opérationnelle possible.
En relation directe avec les clients, l’équipe Sales est la voix et le visage de l’entreprise.
Orienté chiffre et résultat, l’objectif du pôle est d’alimenter et fidéliser la base de clients SpaceFill.
En tant que bras droit, tu occuperas une position transverse avec un aperçu complet du cycle de vente d’une start-up tech depuis
les réflexions marketing.
jusqu’au stratégie de persuasion des clients au téléphone en passant par la gestion de notre CRM SalesForce.
Ton rôle est d’offrir de la hauteur de vue aux Sales pour que ceux-ci se dédient entièrement au cycle de vente. Tu fais le lien entre
les Sales et le Marketing ainsi que les autres équipes de SpaceFill."""}



dict_3={"preffered experience":"""Fully qualified French or European lawyer (Master 2 law degree preferably in international business,
contract or corporate law)
Minimum 1 year of professional experience gained with an international law firm or as In-House Counsel
Fluency in French and English is required, German is a plus
Excellent drafting, analytic and negotiation skills with a strong commercial sense and flexible hands-on approach to business,
with the ability to be creative
Detail oriented with excellent organizational skills and the ability to manage multiple transactions and c
ompeting priorities in a dynamic environment""",
"competencies":"""Proactivity You act without being told what to do. Bring new ideas to the company
Strategic thinking / visioning : You’re able to see and communicate big picture in an inspiring way. You determine
opportunities and threats through comprehensive analysis of current and future trends.
Intelligence : You learn quickly. Demonstrate ability to quickly and proficiently understand and absorb new information
Efficiency : You’re able to produce a significant output with minimal wasted effort
Persuasion : You’re able to convince others to pursue a course of actions
Curiosity : You work with peers and clients to understand problems in-depth to get a real market understanding and expertise
Analytical : You’re able to structure and process qualitative and quantitative data draw insightful conclusion from it.
    You exhibit a probing mind and achieve penetrating insights.
Languages : Bilingual French/English""",

"compétences":"""1-2 ans d’expérience en Sales B2B
Tu comprends les enjeux opérationnels et business de tes signatures (impact sur la marge, le service client, le mix produit)
Très bon communiquant, tu sais exprimer une idée de manière efficace à l’oral comme à l’écrit : court, clair & impactant
Tu es rigoureux et méthodique
Tu as un niveau parfait en français écrit et oral
Plus mais non rédhibitoire - Tu parles anglais et/ou une autre langue (allemand, espagnol, italien..)"
"ce qu'on recherche":"On recherche des gens exceptionnels, c’est à dire avant tout bienveillants, vifs, désir

On recherche quelqun qui est :

Drivé par les résultats
Orienté résultat et passionné(e) par le contact humain
Aime travailler dans un environnement qui va à 2000 à l’heure
Concentré sur la résolution de problèmes
Efficace et prêt à soulever des montagnes
On recherche principalement des talents ayant au moins 1 à 2 ans d’expérience dans la logistique (plus mais non rédhibitoire)"""}

dict_4={"ce qu on te propose":"""Un projet ambitieux avec une ouverture à l’international.
Un moment charnière du développement de l’entreprise.
L’excitation de travailler dans un environnement de travail intense & challengeant.
La possibilité de travailler sur des sujets variés et de progresser vite.
Une culture 1) No bullshit 2) No ego 3) Performance > Temps de travail.
Une équipe où règnent bonne ambiance & bienveillance.
Des bureaux situés en plein coeur de Paris dans le quartier vivant des Grands Boulevards.
Perks : Tickets Restaurants + 50% Navigo + Ligne pro (Aircall)""",
"what we offer":"""A real opportunity to use your creativity with a strong business oriented approach
A startup environment, fast growing, lean and efficient, with the benefits of an important group in an international environment
Strong autonomy in your day to day, goal and success oriented. You can also count on us for coaching and support
A very rewarding job""",
"salary":"""Attractive salary based on your experience
Typical startup perks (Swile, Insurance…)""",

"purquoi nous rejoindre":"""Un poste stratégique dans une start-up en pleine croissance et des échanges quotidiens avec les fondateurs
L’opportunité de rejoindre l’une des start-up B2B les plus prometteuses en Europe à un moment charnière de son développement
(ouverture de l’Allemagne)
Un environnement à 200 à l’heure dans un marché de 300 milliards d’euros en Europe
L’occasion d’enrichir ses connaissances sur le fonctionnement d’une start-up grâce à des missions transverses impliquant l’ensemble des équipes
La possibilité de travailler sur des sujets variés et de progresser rapidement
Une équipe où règne bonne ambiance et bienveillance
Un cadre de travail exceptionnel en plein coeur des Grands Boulevards"
"ce que nous offrons":"L’opportunité de rejoindre l’une des marketplaces B2B les plus prometteuses en France et en Europe
Un environnement à 200 à l’heure dans un des plus grands marchés en Europe
Un salaire compétitif et de l’equity
Mutuelle et prévoyance santé Alan
Tickets restaurants et transports
Cadre de travail exceptionnel en plein coeur des Grands Boulevards"""}



dict_5={"déroulement des entretiens":"""Un entretien téléphonique avec un membre de l’équipe technique pour bien comprendre ton background
et répondre à tes questions.
Un test technique à distance pour évaluer tes compétences techniques et ta façon de réfléchir
Un entretien technique pour débrifer l’exercice et te présenter plus en détail le poste
Un entretien avec Benoit, notre CEO
Une rencontre de l’équipe en visio pour t’aider à te projeter"""}
dict_6={"decouvrir l'equipe":"Meet the team"}

#extraction des mots_clés de la section profil_recherché:

#la_méthode_spacy:
KW_profil_recherché_1=["solides connaissances","expérience","formation supérieur","écrire du beau code te tient a coeur",
                     "participer au développement de l'entreprise","méthodique","ambitieux","bonne maitrise de l'anglais",
                     "un niveau parfait en francais","fort esprit d'équipe","esprit entrepreunarial","efficace",
                     "tu as envie de progresser","expliquer clairement les décisiosn","autonome",
                     "dynamique et trés impliqué"]
#la_méthode_YAKE :
KW_profil_recherché_2=["dynamique , entousiasthe et pro-actif","organisé et rigoureux","persévérant et résilient","un vrai compétiteur",
                       "force de proposition et l'autonomie","sympathique et empathique","you get things done",
                       "excellente qualité rédactionnelle","résolution des problémes","une ou plusieurs expérience",
                       "tu parles parfaitement français","passioné par le contact humain","écouter et convaincre les gens",
                       "bonne ambiance et bienveillance","une ouverture à l'internationale","curieux et treés impliqué",
                       "grande rigueur","excellentes capacités d'analyse","trés bon communiquant","partir en déplacement professionnelle"]
#la_méthode_rake_nltk :
KW_profil_recherhé_3=["formation supérieur et expérience dans un poste similaire","efficace et prét à soulever les montagnes",
                      "une excellenet aisance orale","à l'aise avec le fait de prendre des décisions avec ou sans consensus",
                      "tu es humble et tu sais mettre ton égo à coté","tu as beaucoup d'énergie","anglais courant exigé",
                      "tu prends le leads sur les sujets qui te font confiés","atteindre des objectifs de croissance ambitieux",
                      "tu sais exprimer une idée de maniére efficace à l'oral commme à l'écrit","écrire de beau code te tient à coeur"]
#la_méthode_gensim.summarization :
KW_profil_recherché_4=["experience","business","google","project","SpaceFill","React","Back-end","SQL","strategic thinking",
                       "analytical","efficiency","intelligence","proactivity","persuasion","curiosity" "French","English"]

#text
nlp=spacy.load("en_core_sci_lg")
text="""SpaceFill est une plateforme en ligne de stockage en entrepôts dans toute la France, qui aide les entreprises à trouver la meilleure solution de stockage, " \
     à piloter leurs marchandises et à optimiser l’intégralité de leurs schémas logistiques.
Fondée en juin 2018 par Maxime Huzar, Quentin Drillon et Gustave Roche, 
SpaceFill a pour ambition de créer le cloud européen des entrepôts de marchandises. L’entreprise a dès sa création connue une croissance très forte,
 matérialisée par deux levées de fonds, une d’1M€ quatre mois après sa création et une seconde de 7M€ en septembre 2020.
 L’équipe tech et la stack technique

L’équipe technique chez Dashdoc est actuellement composée de 9 personnes, dont une partie à Nantes et l’autre à Paris.

Le produit se décompose en 3 parties : l’API, l’application mobile et l’application web. L’API est développée en Python / Django avec Django Rest Framework, utilise PostgreSQL et est hébergée sur Google Cloud. Les applications sont développées en React / React Native.

Notre fonctionnement se base sur la méthodologie Shape Up : Nous travaillons sur des cycles de 6 semaines, durant lesquels des équipes éphémères de 1 à 3 personnes travaillent chacune sur 1 à 3 sujets ayant un impact fort sur le produit. Les développeurs sont force de décision sur les décisions produit, et sont épaulée par notre Product Manager et notre Designer.
Au bout des 6 semaines, une phase de transition de 2 semaines démarre. Les développeurs est dédiée aux travaux de refactoring, et d’amélioration de la robustesse de notre produit. Elle a pour but de combler la dette technique.

Nous fonctionnons en déploiement continu (Github/CircleCI) et nous sortons de nouvelles améliorations du produit chaque jour.
2-3 ans d’expérience en Supply Acquisition ou Sales B2B (échanges avec des interlocuteurs de type Dirigeants, Directeurs Commerciaux, Directeurs Logistiques est un plus)
Tu as déjà réalisé des rendez-vous terrain et partir en déplacement professionnel ne te fais pas peur (Permis B obligatoire)
Pas d’expérience en logistique au préalable nécessaire mais une capacité et une volonté d’adaptation forte.
Tu comprends les enjeux opérationnels et stratégiques de tes signatures (impact sur la qualité de service, la performance commerciale, l’image de SpaceFill chez nos partenaires)
Très bon communiquant, tu sais exprimer une idée de manière efficace à l’oral comme à l’écrit : court, clair et impactant
Tu es rigoureux et méthodique
Tu as un niveau parfait en français écrit et oral
Plus mais non rédhibitoire - Tu parles anglais et/ou une autre langue (allemand, espagnol)
L’opportunité de rejoindre l’une des marketplaces B2B les plus prometteuses en France et en Europe
Un environnement à 200 à l’heure dans un des plus grands marchés en Europe
Un salaire compétitif et de l’equity
Mutuelle et prévoyance santé Alan
Tickets restaurants et transports
Cadre de travail exceptionnel en plein coeur des Grands Boulevards
Un entretien téléphonique avec un membre de l’équipe technique pour bien comprendre ton background et répondre à tes questions
Un test technique à distance pour évaluer tes compétences techniques et ta façon de réfléchir
Un entretien technique pour débrifer l’exercice et te présenter plus en détail le poste
Un entretien avec Benoit, notre CEO
Une rencontre de l’équipe en visio pour t’aider à te projeter chez Dashdoc
Rémunération attractive et possibilité d’avoir des parts de la société"""
doc=nlp(text)
print(doc.ents)




#résultat
#méthode_spacy:
KW_1=["solution logistique","leaders du marché","start-up","économiser","TPE","PME","temps précieux","responsable marketing",
      "spacefill","meilleure solution de stockage","marchandises","gérer les stocks","shémas logistiques","maxime huzar","quentin drillon","gustave roche",
      "cloud européen","logiciel SAAS","croissance exponentielle","prix Gallion Booster","beacoup d'humour,bienveillance et exigence",
      "responsable marketing","growth hacking","bras droit du ceo et du coo","des choses à construire à optimiser et à automatiser",
      "account manager senior","potentiel commerciale","upsell","cross selling","segment small","mid cap","CRM","Sales Development Representative",
      "python","django","django rest framework","React / React Native","PostgreSQL","shape up","refactoring","Github/CircleCI","solides connaissances",
      "écrire du beau code te tient a coeur","expérience","formation supérieur","poste similaire",
      "participer au développement de l'entreprise","méthodique","ambitieux","bonne maitrise de l'anglais",
      "un niveau parfait en francais","fort esprit d'équipe","esprit entrepreunarial","efficace",
      "tu as envie de progresser","expliquer clairement les décisiosn","autonome","dynamique et trés impliqué","Cadre de travail exceptionnel",
      "Tickets restaurants et transports","environnement de travail intense & challengeant","Un salaire compétitif et de l’equity",
      "entretien téléphonique","entretien technique","decouvrir l'équipe"]

#sauvegarder_scraping:
mydb=client["mydb"]
mycol=mydb["scraping"]
data=list.append(dict_1,dict_2,dict_3,dict_4,dict_5,dict_6)
mycol.insert_one(data)











