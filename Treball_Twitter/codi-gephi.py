import json
import glob  # permet agafar tots els fitxers
import pandas as pd
from tqdm import tqdm

#preparem els elements necessaris prèviament a la iteració
files = glob.glob('twitter_api_responses/api_responses/*') #per treure tots els arxius
llista_dfs = []
llista_prov = []

#extraiem la informació dels tweets
for file in tqdm(files):#iterem per a cada fitxer
    print(file)
    with open(file, encoding='utf-8') as fitxer:
        dades =json.load(fitxer)
        tweets = dades['data']
        for tweet in tweets: #iterem cada tweet
            author_id = tweet['author_id']
            created_at = tweet['created_at']
            users = dades['includes']['users']
            for user in users: #treiem el nom d'usuari comparant id i username
                if user['id'] == author_id:
                    user_name = user['username']
                else:
                    pass

            try: #agafem les mencions
                llista_mencions = tweet['entities']['mentions']
                for element in llista_mencions:
                    mencionat = element['username']
                    rel = (user_name, mencionat, created_at)
                    llista_prov.append(rel)
            except KeyError:
                pass

#creem el df i l'exportem a csv
df = pd.DataFrame(llista_prov, columns = ['Source', 'Target', 'Timestamp'])
df.to_csv('mencions2.csv', index=False)