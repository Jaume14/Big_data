import json
import glob  # permet agafar tots els fitxers
import pandas as pd
from tqdm import tqdm

# creem les variables necessaries per emmagatzemar les dades
files = glob.glob('twitter_api_responses/api_responses/*.json')
llista_dfs = []

# fem els processos
for file in tqdm(files):  # iterem per a cada fitxer
    with open(file, 'r', encoding="utf-8") as jsonfile:
        dades = json.load(jsonfile)
        tweets = dades["data"]  # creem una llista amb tots els tweets del fitxer
        # print(len(tweets)) #imprimim el nombre de tweets a la llista

        for tweet in tweets:  # per a cada tweet treiem el id del usuari (el nom no el tenim a data)
            author_id = tweet["author_id"]
            users = dades["includes"]["users"]  # el username el tenim aquí i per agafar-lo cal iterar
            keywords = []
            mencions = []
            hashtags = []

            #treiem el nombre de mencions de cada candidat
            candidats = ['Basha Changue','Ernest Maragall','Ada Colau','Jaume Collboni','Xavier Trias','Anna Grau','Eva Parera','Daniel Sirera']
            basha_changue = 0
            ernest_maragall=0
            ada_colau=0
            jaume_collboni=0
            xavier_trias=0
            anna_grau=0
            eva_parera=0
            daniel_sirera=0

            if tweet["text"].find('Basha Changue')  >=0:
                basha_changue += 1
            if tweet["text"].find('Ernest Maragall') >=0:
                ernest_maragall += 1
            if tweet["text"].find('Ada Colau') >=0:
                ada_colau += 1
            if tweet["text"].find('Jaume Collboni') >=0:
                jaume_collboni += 1
            if tweet["text"].find('Xavier Trias') >=0:
                xavier_trias += 1
            if tweet["text"].find('Anna Grau') >=0:
                anna_grau += 1
            if tweet["text"].find('Eva Parera') >=0:
                eva_parera += 1
            if tweet["text"].find('Daniel Sirera') >=0:
                daniel_sirera += 1


            try:
                for keyword in tweet["entities"]["annotations"]:
                    keywords.append(keyword["normalized_text"])  # agefim les keywords trobades
            except:
                pass

            try:
                for hashtag in tweet["entities"]["hashtags"]:
                    hashtags.append(hashtag["tag"])  # afegim els hashtags trobats
            except:
                pass

            try:
                for mention in tweet["entities"]["mentions"]:
                    mencions.append(mention["username"])  # afegim els usuaris mencionats
            except:
                pass

            for user in users:  # iterem i igualem per extreure el nom d'usuari
                if user["id"] == author_id:  # agafem el nom d'usuari a partir del id anterior
                    username = user["username"]
                    # print(user["id"], user["username"])
                    followers_count = user["public_metrics"][
                        "followers_count"]  # extraiem el nombre de seguidors de l'usuari
                else:
                    pass
            text = tweet["text"]
            # creem el df amb les dades que decidim agafar
            df = pd.DataFrame({
                "user_id": author_id,
                "username": username,
                "followers_count": followers_count,
                "text": text,
                "mentions": ','.join(mencions),
                "change":basha_changue,
                "maragall":ernest_maragall,
                "colau":ada_colau,
                "collboni":jaume_collboni,
                "trias":xavier_trias,
                "grau":anna_grau,
                "parera":eva_parera,
                "sirera":daniel_sirera,
                "retweet_count": tweet["public_metrics"]["retweet_count"],
                "reply_count": tweet["public_metrics"]["reply_count"],
                "like_count": tweet["public_metrics"]["like_count"],
                "quote_count": tweet["public_metrics"]["quote_count"],
                "impression_count": tweet["public_metrics"]["impression_count"],
                "created_at": tweet["created_at"],
                "keywords": ','.join(keywords),
                "hashtags": ','.join(hashtags)
            }, index=[0])
            # print(df)
            llista_dfs.append(df)
            # print(llista_dfs)

# concatenem totes les llistes dins de la llista anterior
df_final = pd.concat(llista_dfs)
print(df_final)

# exportem a csv
df_final.to_csv("A(4).csv", index=False)
