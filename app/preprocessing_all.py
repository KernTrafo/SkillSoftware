from operator import mod
from numpy.lib.function_base import append
import pandas as pd 
import numpy as np
from pandas.core.dtypes.missing import isna 
import sqlalchemy as db1
import string as st
import re
import nltk
from nltk import PorterStemmer, WordNetLemmatizer
import random
import numbers as num 
import operator
from sqlalchemy import create_engine
from app.models import Skills
from app.models import UserSkills
#from app import db
from typing import Counter  
from app import app, db
from itertools import chain



from flask_login import current_user, login_user, logout_user, login_required
import functools


engine = create_engine("mysql+pymysql://root:@KTDB2021@app_db:3306/kerntrafo")
# engine = create_engine('sqlite:///app.db')


def transform(nested_list):
    regular_list = []
    for ele in nested_list:
        if type(ele) is list:
            regular_list.append(ele)
        else:
            regular_list.append([ele])
    return regular_list




#current_user.get_id()


class cleaning():
    def __init__(self,text):
        self.text = text 
    
    def remove_punct(self, text):
        return ("".join([ch for ch in text if ch not in st.punctuation]))
    
    
    def tokenize(self, text):
        text = re.split('\s+',text)
        return [x.lower() for x in text]

    def remove_small_words(self, text):
        return [x for x in text if len(x) > 3]
    
    def remove_stopwords(self,text):

        stop_words= ['aber', 'alle', 'jbzj', 'allem', 'allen', 'aller', 'pngbrsekretariatstätigkeiten','alles', 'als', 'also', 'am', 'an', 'ander', 'andere', 'anderem', 'anderen', 'anderer', 'anderes', 'anderm', 'andern', 'anderr', 'anders', 'auch', 'auf', 'aus', 'bei', 'bin', 'bis', 'bist', 'da', 'damit', 'dann', 'der', 'den', 'des', 'dem', 'die', 'das', 'dass', 'daß', 'derselbe', 'derselben', 'denselben', 'desselben', 'demselben', 'dieselbe', 'dieselben', 'dasselbe', 'dazu', 'dein', 'deine', 'deinem', 'deinen', 'deiner', 'deines', 'denn', 'derer', 'dessen', 'dich', 'dir', 'du', 'dies', 'diese', 'diesem', 'diesen', 'dieser', 'dieses', 'doch', 'dort', 'durch', 'ein', 'eine', 'einem', 'einen', 'einer', 'eines', 'einig', 'einige', 'abbaus', 'operativen', 'banfen', 'deren','gemäß', 'eigen', 'einigem', 'operativer','einigen', 'einiger', 'einiges', 'einmal', 'er', 'ihn', 'ihm', 'es', 'etwas', 'euer', 'eure', 'eurem', 'euren', 'eurer', 'eures', 'für', 'gegen', 'gewesen', 'hab', 'habe', 'haben', 'hat', 'hatte', 'hatten', 'hier', 'hin', 'hinter', 'ich', 'mich', 'mir', 'ihr', 'ihre', 'ihrem', 'ihren', 'ihrer', 'ihres', 'euch', 'im', 'in', 'indem', 'ins', 'ist', 'jede', 'jedem', 'jeden', 'jeder', 'jedes', 'jene', 'jenem', 'jenen', 'jener', 'jenes', 'jetzt', 'kann', 'kein', 'keine', 'keinem', 'keinen', 'keiner', 'keines', 'können','abfr', 'könnte', 'machen', 'man', 'entsorgungs', 'manche', 'manchem', 'manchen', 'mancher', 'manches', 'mein', 'meine', 'meinem', 'meinen', 'meiner', 'meines', 'mit', 'muss', 'musste', 'inkl','wesentlichen','nach', 'nicht', 'nichts', 'noch', 'nun', 'nur', 'ob', 'oder', 'ohne', 'sehr', 'sein', 'seine', 'seinem', 'seinen', 'seiner', 'seines', 'selbst', 'sich', 'sie', 'ihnen', 'sind', 'so', 'solche', 'solchem', 'solchen', 'solcher', 'Sicherheitsingenieursicherheitsingenieur' , 'allgemeine','sicherheitsingenieursicherheitsingenieur', 'solches', 'soll', 'sicherheitstechnikersicherheitstechniker', 'planungs','Sicherheitstechnikersicherheitstechniker','sollte', 'sondern', 'sonst', 'über', 'um', 'und', 'uns', 'unsere', 'unserem', 'unseren', 'unser', 'unseres', 'unter', 'viel', 'vom', 'von', 'vor', 'während', 'war', 'waren', 'warst', 'was', 'weg', 'weil', 'weiter', 'welche', 'welchem', 'welchen', 'welcher', 'welches', 'wenn', 'werde', 'werden', 'wie', 'wieder', 'will', 'wir', 'wird', 'wirst', 'sowie' ,'wo', 'wollen', 'wollte', 'würde', 'würden', 'bitte', 'auswählen', 'zu', 'zum', 'zur', 'zwar', 'zwischen']
        return [word for word in text if word not in stop_words]  #nltk.corpus.stopwords.words('german')]
    
    def stemming(self,text):
        ps = PorterStemmer()
        return [ps.stem(word) for word in text]

    def lemmatize(self, text):
        word_net = WordNetLemmatizer()
        return [word_net.lemmatize(word) for word in text]

    def return_sentences(self, tokens):
        return " ".join([word for word in tokens])





class score():
    
    def __init__(self, n):
        self.n = n 
        # if isinstance(self.n , num.Number):
        #     print("%f is number "%self.n)

    def generate_score(self):

        if self.n < 100 and isinstance(self.n , num.Number):
            return self.n
        else: 
            return 95


class check_words: 
     
    
    def __init__(self) -> None:
        pass
        

    def check_text(str1,str2):
        typ= 0# skills_anzeige
        match = [x for x in str1 if x in str2]


        matched= list(filter(None, match))

        n=len(matched)/(len(str2))  if len(str2) != 0 else 0
        n = n*100
        n_ = round(n *6) #/10
        score_=  score(n_) 
        score_matching = score_.generate_score()

        return (score_matching, match)
    



class uniq_class:
    def uniq_c(lst):
        last = object()
        for item in lst:
            if item == last:
                continue
            yield item
            last = item

    def sort_and_deduplicate_c(l):
        return list(uniq(sorted(l, reverse=True)))
    
    def intersection_c(lst1, lst2):
        lst3=[]
        lst3 = [value for value in lst1 if value in lst2]
        return lst3




def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def not_intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3


class connect_db():
    def __init__(self) -> None:
        pass
    
    def connect_mysql(user_id):


        connection = engine.connect()
        #metadata = db1.MetaData()
        
        #stellenanzeigen = db1.Table('stellenanzeigenotn', metadata, autoload=True, autoload_with=engine)
        #query = db1.select([stellenanzeigen])

        #stellenanzeigen_df = pd.read_sql_query(query, engine)
        ctext = cleaning('text')

        user_data_df = pd.read_sql_table('user_data', connection)
        
        user_skills_df    = pd.read_sql_table('user_skills', connection)        #user_data_df = user_data_df.dropna()
        Skills_sql_df     = pd.read_sql_table('skills', connection) 

        connection.close()


        #user_id = 1

        user_data_df = user_data_df.fillna('')

        user_data_df_id = user_data_df [user_data_df.user_id==user_id]
        
        
        user_data_df_id =  user_data_df_id[user_data_df_id['timestamp']==user_data_df_id['timestamp'].max()]

        #print(user_data_df_id.head(1))


        job_matching_df_1= pd.DataFrame()

        job_matching_df_1['user_data_all_1'] = user_data_df_id['data_studium_schwerpunkt']+ ' ' +  user_data_df_id ['data_ausbildung']+ ' ' + user_data_df_id['data_aktuelle_berufsbeschreibung']+ ' '+ user_data_df_id['data_ausbildung_schwerpunkt'] + ' '+ user_data_df_id['data_aktuelle_berufsbeschreibung'] + ' '+ user_data_df_id['data_projektbezeichnung']

        job_matching_df_1['user_data_all_2'] = user_data_df_id ['data_kenntnisse']+ ' ' +user_data_df_id['data_projektrolle'] + ' ' + user_data_df_id['data_potenzielle_berufe'] + ' ' +user_data_df_id['andere_fachrichtung'] +  ' ' +user_data_df_id['data_sonstige_fachliche'] + ' '+ user_data_df_id['data_projektrolle']+ ' '+ user_data_df_id['data_projektbeschreibung']

        job_matching_df= pd.DataFrame()

        job_matching_df['all'] = job_matching_df_1['user_data_all_1'] + ' '+job_matching_df_1['user_data_all_2']

        job_matching_df['timestamp'] = pd.to_datetime(user_data_df_id['timestamp'])

  
        
                
        ##### stellen auslesen
        #docs.dsserver.meschede.fh-swf.de 
        
        fname= 'Stellenplan_V2.3.xlsx'
        stellenpland_df = pd.read_excel(fname)
        
        stellenpand_needed_df  = stellenpland_df[["Tätigkeit","Stellenbezeichnung", "Hauptaufgaben", "Interessensabfrage","AS-Tauglichkeit","KB-Tauglichkeit","WS-Tauglichkeit","Quali" ]]

        stellenpand_needed_df = stellenpand_needed_df [stellenpand_needed_df["Interessensabfrage"] == 'ja']

    
        
        #print(stellenpand_needed_df)
        stellenpand_needed_df = stellenpand_needed_df.fillna(str(''))

        #print("after_na",stellenpand_needed_df)
        
        stellen_skills= pd.DataFrame()
        stellen_skills['all'] = stellenpand_needed_df['Hauptaufgaben']
        stellen_skills['Stellenbezeichnunskills_anzeigeg']  = stellenpand_needed_df['Stellenbezeichnung']

        stellenplan_q_df = pd.DataFrame()
        stellenplan_q_df['Stellenbezeichnung']= stellenpand_needed_df['Stellenbezeichnung']
        stellenplan_q_df['Quali']= stellenpand_needed_df['Quali']



        
        
        stellen_skills['all'] = stellen_skills['all'].apply(lambda x: ctext.remove_punct(x))

        stellen_skills['all'] = stellen_skills['all'].apply(lambda x: ctext.tokenize(x))

        stellen_skills['all'] = stellen_skills['all'].apply(lambda x: ctext.remove_small_words(x))


        stellen_skills['all'] = stellen_skills['all'].apply(lambda x: ctext.remove_stopwords(x))
        # stellen_skills['all'] = stellen_skills['all'].apply(lambda x: ctext.stemming(x))

        # stellen_skills['all'] = stellen_skills['all'].apply(lambda x: ctext.lemmatize(x))
        
        stellen_merged_df= pd.DataFrame()
        
     
        stellen_merged_df['all']  = stellenpand_needed_df['Tätigkeit']+ ' '+ stellenpand_needed_df['Stellenbezeichnung']+ ' ' + stellenpand_needed_df['Hauptaufgaben']
        
        stellen_merged_df['Stellenbezeichnung'] = stellenpand_needed_df['Stellenbezeichnung']
        
        


        

        

        #text =  ctext.return_sentences( ctext.lemmatize ( ctext.stemming( ctext.remove_stopwords( ctext.remove_small_words ( ctext.tokenize ( ctext.remove_punct(text)))))))
        stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.remove_punct(x))

        stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.tokenize(x))

        stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.remove_small_words(x))


        stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.remove_stopwords(x))
        stellen_skills= pd.DataFrame()
        stellen_skills['all'] = stellen_merged_df['all'] 
        stellen_skills['Stellenbezeichnung']  = stellen_merged_df['Stellenbezeichnung']


        #stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.stemming(x))

        #stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.lemmatize(x))

        #stellen_merged_df['all'] = stellen_merged_df['all'].apply(lambda x: ctext.return_sentences(x))



    


        #### user data cleaning

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.remove_punct(x))

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.tokenize(x))

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.remove_small_words(x))


        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.remove_stopwords(x))


        
    
        #job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.stemming(x))

        #job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.lemmatize(x))
 

        user_skills_df_id = user_skills_df [user_skills_df.user_id==user_id]
        
        job_matching_df = job_matching_df[job_matching_df['timestamp'] ==job_matching_df['timestamp'].max()]
        list_value_list=[]
        if not user_skills_df_id.empty and not Skills_sql_df.empty:
            for i in user_skills_df_id.skill_id:
                list_value = Skills_sql_df[Skills_sql_df['id']==i]
                #print('skill in sql',list_value )
                list_value_list.append( list_value.skill.values[0])


        # dic_df=[]
        # dic_dic={}
        # new_df={}
 
         
        l2=[]
        l3=[]
        index_df = int(job_matching_df.index.values)
        skills = pd.DataFrame()
        skills['all'] = job_matching_df['all']

        top ={}
        add_top={}

        if list_value_list:
            #print("new Skills")
            #list_value_list       =sort_and_deduplicate(list_value_list)

            list_value_list=[item for item in list_value_list if not isinstance(item,list)]

            #print('list_value_list', list_value_list)

       
            l2= list_value_list.copy()

            #print('l2',l2)

            
            for i in l2:
                if type(i) == str:
                    l3.append(list(i.split(" ")))
                else:
                    l3.append(i)

            #print('l3 after for loop',l3)
            
            
            #l2= [item for item in l2 if not isinstance(item,list)]

            #print('list before  job_matching_df.at index_df ass',job_matching_df.at[index_df,'all'])


            l4=job_matching_df.at[index_df,'all'].copy()

            #print('l4 = job_matching_df.at =l4 ', l4)

      

            l3.append(l4)
            l2 = l3.copy()

            #print('l3.copy = l2', l2, 'l3=',l3)

            #print('before transform l2', l2)
            l2=transform(l2)
            #print('after transform l2', l2)
            l2 =  [item for sublist in l2 for item in sublist]
            l2= sort_and_deduplicate(l2)
            l2 = [x.lower() for x in l2]

            #print(' skills user data + skills',l2)

            flagges_checker_df = pd.DataFrame()
            flagges_checker_df ['Stellenbezeichnung'] = stellenpand_needed_df ['Stellenbezeichnung'].drop_duplicates()
            flagges_checker_df['AS-Tauglichkeit'] = stellenpand_needed_df ['AS-Tauglichkeit']
            flagges_checker_df['KB-Tauglichkeit'] = stellenpand_needed_df ['KB-Tauglichkeit']
            flagges_checker_df['WS-Tauglichkeit'] = stellenpand_needed_df ['WS-Tauglichkeit']
            #print("flagges_checker_df",flagges_checker_df)

            sc=0
            match = []
     
            a_ls = []
            skills_stellen= {}
            temp_df = pd.DataFrame()
            match_dic = {}
            match_list= []
            angaben_skills_dic={}
            need_Skills =[]
            inter_Sec = []
            inter_Sec_dic = {}


            need_Skills = Skills_sql_df['skill'].tolist()
            
            for a, i in stellen_merged_df.itertuples(index=False):
                #print('l2', l2)
                sc, match = check_words.check_text(l2,a)

                match = sort_and_deduplicate(match)
     
                match_dic[i]=match
                match_list.append(match)
                angaben_skills_dic[i]= l2

                inter_Sec_dic[i] = sort_and_deduplicate(intersection(need_Skills,a))

                #print('inter_Sec',inter_Sec[i])




                
                
            

            

                #rand_v,need_Skills= check_words.check_text(Skills_sql_df['skill'].values[j],a)


                
                




                temp_df = flagges_checker_df[flagges_checker_df['Stellenbezeichnung'] == i]


                AS = bool(temp_df['AS-Tauglichkeit'].values)==True
                KBT = bool(temp_df['KB-Tauglichkeit'].values)==True
                WS = bool(temp_df['WS-Tauglichkeit'].values)==True

                user_ws = bool(user_data_df_id.gesundheit_schichttauglichkeit.values)
                user_kbt = bool(user_data_df_id.gesundheit_kontrollbereichstauglichkeit.values)
                user_as =  bool(user_data_df_id.gesundheit_atemschutztauglichkeit.values)

                if WS and AS and KBT: #111 ws as kbt
                    if user_kbt and user_ws and user_as:
                        top[i] = sc
                    else:
                        pass

                elif not WS and AS and KBT: #011
                    if AS and KBT:
                        top[i] = sc
                    else:
                        pass

                elif WS and AS and not KBT: #110
                    if  user_as and user_ws:
                        top[i] = sc
                    else:
                        pass

                elif WS and not AS and KBT: #101
                    if user_kbt and user_ws:
                        top[i] = sc
                    else:
                        pass

                elif WS and not AS and not KBT: #100
                    if user_ws:
                        top[i] = sc
                    else:
                        pass

                elif not WS and not AS and KBT: #001
                    if user_kbt:
                        top[i] = sc
                    else:
                        pass

                elif not WS and AS and not KBT:      #010
                    if user_as:
                        top[i] = sc
                    else:
                        pass

                elif not AS and not KBT and not WS:        #000                        
                    top[i] = sc


        
                
                if match_list :
         
                    match_list = transform(match_list)
                    match_list =  [item for sublist in match_list for item in sublist]
                    match_list = sort_and_deduplicate(match_list)

                for a,i in stellen_skills.itertuples(index=False):
                
                    a_ls = list(a)  
                    skills_ls = sort_and_deduplicate(a_ls)
                    #skills_ls = sorted(set( a_ls), key=lambda x:a_ls.index(x))
                    skills_stellen[i] = skills_ls

            # except:
            #     top[0] = 0 

            mylist = []

            up_to_date =len(job_matching_df)-1
            
            #print('sort_orders', top.values())
            #print('\n add_top \n', add_top.values())
        
            sort_orders = sorted(top.items(), key=lambda x: x[1], reverse=True)
            
            #print('\n sort orders \n',sort_orders)


            #print(sort_orders)
            if up_to_date == 0: 
                #print("alles richtig")
                mylist = list(skills['all'].values)
                skills = sorted(mylist, key=lambda x:mylist.index(x))
                #print('match_list', match_list)


            return ( match_list,match_dic, skills, inter_Sec_dic,
                    bool(user_data_df_id.gesundheit_atemschutztauglichkeit.values) ,
                    bool(user_data_df_id.gesundheit_schichttauglichkeit.values)  ,                
                    bool(user_data_df_id.gesundheit_kontrollbereichstauglichkeit.values),         
                    sort_orders, stellenplan_q_df)




        else:
            top ={}
            a_ls = []
            skills_stellen= {}
            temp_df = pd.DataFrame()
            match_dic = {}
            match_list= []
            mylist = []
            l2=[]
            skills['all'] = job_matching_df['all']
            angaben_skills_dic={}
            need_Skills =[]
            inter_Sec = []
            inter_Sec_dic = {}
            need_Skills = Skills_sql_df['skill'].tolist()


            flagges_checker_df = pd.DataFrame()
            flagges_checker_df ['Stellenbezeichnung'] = stellenpand_needed_df ['Stellenbezeichnung'].drop_duplicates()
            flagges_checker_df['AS-Tauglichkeit'] = stellenpand_needed_df ['AS-Tauglichkeit']
            flagges_checker_df['KB-Tauglichkeit'] = stellenpand_needed_df ['KB-Tauglichkeit']
            flagges_checker_df['WS-Tauglichkeit'] = stellenpand_needed_df ['WS-Tauglichkeit']
            l2=job_matching_df.at[index_df,'all']


            for a, i in stellen_merged_df.itertuples(index=False):
                #print('job_matching_df ', job_matching_df.at[index_df,'all'])
                sc, match = check_words.check_text(job_matching_df.at[index_df,'all'],a)
                match = sort_and_deduplicate(match)
                match_dic[i]=match
                match_list.append(match)
                angaben_skills_dic[i]= l2
                inter_Sec_dic[i] = sort_and_deduplicate(intersection(need_Skills,a))

                temp_df = flagges_checker_df[flagges_checker_df['Stellenbezeichnung'] == i]
                temp_df = flagges_checker_df[flagges_checker_df['Stellenbezeichnung'] == i]


                AS = bool(temp_df['AS-Tauglichkeit'].values)==True
                KBT = bool(temp_df['KB-Tauglichkeit'].values)==True
                WS = bool(temp_df['WS-Tauglichkeit'].values)==True

                user_ws = bool(user_data_df_id.gesundheit_schichttauglichkeit.values)
                user_kbt = bool(user_data_df_id.gesundheit_kontrollbereichstauglichkeit.values)
                user_as =  bool(user_data_df_id.gesundheit_atemschutztauglichkeit.values)


                if WS and AS and KBT: #111 ws as kbt
                    if user_kbt and user_ws and user_as:
                        top[i] = sc
                    else:
                        pass

                elif not WS and AS and KBT: #011
                    if AS and KBT:
                        top[i] = sc
                    else:
                        pass

                elif WS and AS and not KBT: #110
                    if  user_as and user_ws:
                        top[i] = sc
                    else:
                        pass

                elif WS and not AS and KBT: #101
                    if user_kbt and user_ws:
                        top[i] = sc
                    else:
                        pass

                elif WS and not AS and not KBT: #100
                    if user_ws:
                        top[i] = sc
                    else:
                        pass

                elif not WS and not AS and KBT: #001
                    if user_kbt:
                        top[i] = sc
                    else:
                        pass

                elif not WS and AS and not KBT:      #010
                    if user_as:
                        top[i] = sc
                    else:
                        pass

                elif not AS and not KBT and not WS:        #000                        
                    top[i] = sc





                  

            # db.session.commit()
                if match_list :
                    match_list =[item for sublist in match_list for item in sublist]
                    match_list = sort_and_deduplicate(match_list)


                for a,i in stellen_skills.itertuples(index=False):
                
                    a_ls = list(a)
                    skills_ls = sort_and_deduplicate(a_ls)
                    #skills_ls = sorted(set( a_ls), key=lambda x:a_ls.index(x))
                    skills_stellen[i] = skills_ls

                

                up_to_date =len(job_matching_df)-1

                sort_orders = sorted(top.items(), key=lambda x: x[1], reverse=True)
                #print(sort_orders)
                if up_to_date == 0: 
                   
                    #print("alles richtig")
                    mylist = list(job_matching_df['all'].values)
                    skills = sorted(mylist, key=lambda x:mylist.index(x))
                    #print(match_dic)
                
            
            return (  match_list,match_dic, skills, inter_Sec_dic,
                        bool(user_data_df_id.gesundheit_atemschutztauglichkeit.values) ,
                        bool(user_data_df_id.gesundheit_schichttauglichkeit.values)  ,                
                        bool(user_data_df_id.gesundheit_kontrollbereichstauglichkeit.values),         
                        sort_orders,stellenplan_q_df)






class connect_db_all():
    def __init__(self) -> None:
        pass
    
    def connect_mysql():


        connection = engine.connect()

        ctext = cleaning('text')

        user_data_df_id = pd.read_sql_table('user_data', connection)
        
        user_skills_df    = pd.read_sql_table('user_skills', connection)       
        Skills_sql_df     = pd.read_sql_table('skills', connection) 

        connection.close()

        job_matching_df_1= pd.DataFrame()

        job_matching_df_1['user_data_all_1'] = user_data_df_id['data_studium_schwerpunkt']+' ' +  user_data_df_id ['data_ausbildung']+ ' ' +user_data_df_id['data_aktuelle_berufsbeschreibung']+ ' '+ user_data_df_id['data_ausbildung_schwerpunkt'] + ' '+ user_data_df_id['data_aktuelle_berufsbeschreibung'] + ' '+ user_data_df_id['data_projektbezeichnung']

        job_matching_df_1['user_data_all_2'] = user_data_df_id ['data_kenntnisse']+ ' ' +user_data_df_id['data_projektrolle'] + ' '+ user_data_df_id['data_potenzielle_berufe'] + ' ' +user_data_df_id['andere_fachrichtung'] + ' ' +user_data_df_id['data_sonstige_fachliche'] + ' '+ user_data_df_id['data_projektrolle']+ ' '+ user_data_df_id['data_projektbeschreibung']


        job_matching_df= pd.DataFrame()

        job_matching_df['all'] = job_matching_df_1['user_data_all_1'] + ' '+job_matching_df_1['user_data_all_2']

        job_matching_df['user_id'] = user_data_df_id['user_id']

        

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.remove_punct(x))

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.tokenize(x))

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.remove_small_words(x))


        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.remove_stopwords(x))


        
    
        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.stemming(x))

        job_matching_df['all'] = job_matching_df['all'].apply(lambda x: ctext.lemmatize(x))
        
        job_matching_df = job_matching_df.drop_duplicates(subset=['user_id'],keep= 'last' ).reset_index(drop=True)
        
        
        job_list=[]
        #if not user_skills_df.empty:
        #UserSkills.query.delete()
        for i in job_matching_df['user_id']:
            job_id = job_matching_df[job_matching_df['user_id']==i]    #user_skill has  user id skill id 
            job_id_list= [item for item in job_id['all']]
            job_id_list = [item for sublist in job_id_list for item in sublist]
      
            user_skill_found = [i for i in job_id_list if i in Skills_sql_df['skill'].values]
            if user_skill_found :
                for j in user_skill_found  :
                    
                    skill_id_push = int(Skills_sql_df[Skills_sql_df['skill']==j].id.values[0] )

                    user_skill_id_df = user_skills_df[user_skills_df['skill_id']==skill_id_push] 

                    if i not in user_skill_id_df.user_id.values :
                       
                        input_vec = UserSkills(user_id= int(i) , skill_id=skill_id_push)
                        db.session.add(input_vec)
                        db.session.commit()
                    

class push_new_skills():
    def __init__(self) -> None:
        pass
    
    def connect_mysql():

        connection        = engine.connect()
        Skills_sql_df     = pd.read_sql_table('skills', connection)
        user_data_df_id      = pd.read_sql_table('user_data', connection)
        user_skills_df    = pd.read_sql_table('user_skills', connection)

        connection.close()
    

        if not Skills_sql_df.empty:
            skills_tab                    = []
            skills_tab                    = [item for item in Skills_sql_df['skill']] 
            max_id_in                     =  user_skills_df['skill_id'].max()



    
        job_matching_df_1         = pd.DataFrame()
        job_matching_df           = pd.DataFrame()


        job_matching_df_1['all1'] = user_data_df_id['data_studium_schwerpunkt']+' ' +  user_data_df_id ['data_ausbildung']+ ' ' +user_data_df_id['data_aktuelle_berufsbeschreibung']+ ' '+ user_data_df_id['data_ausbildung_schwerpunkt'] + ' '+ user_data_df_id['data_aktuelle_berufsbeschreibung'] + ' '+ user_data_df_id['data_projektbezeichnung']
        job_matching_df_1['all2'] = user_data_df_id ['data_kenntnisse']+ ' ' +user_data_df_id['data_projektrolle'] + ' '+ user_data_df_id['data_potenzielle_berufe'] + ' ' +user_data_df_id['andere_fachrichtung'] + ' '+ user_data_df_id['data_sonstige_fachliche'] + ' '+ user_data_df_id['data_projektrolle']+ ' '+ user_data_df_id['data_projektbeschreibung']
        job_matching_df['all']    = job_matching_df_1['all1'] + ' '+job_matching_df_1['all2']


        if not job_matching_df['all'].empty and not user_skills_df.empty:
            ctext = cleaning('push')
            job_matching_df['all']        = job_matching_df['all'].apply(lambda x: ctext.remove_punct(x))
            job_matching_df['all']        = job_matching_df['all'].apply(lambda x: ctext.tokenize(x))
            job_matching_df['all']        = job_matching_df['all'].apply(lambda x: ctext.remove_small_words(x))
            job_matching_df['all']        = job_matching_df['all'].apply(lambda x: ctext.remove_stopwords(x))
            job_matching_df['all']        = job_matching_df['all'].apply(lambda x: sort_and_deduplicate(x))
            skills_list_user_data         = []
            skills_list_user_data         = [i for i in job_matching_df['all']]





            if skills_list_user_data:
                skills_list_user_data          =[item for sublist in skills_list_user_data for item in sublist]
                skills_list_user_data          = sort_and_deduplicate(skills_list_user_data)
                uniq_skills                    = not_intersection(skills_list_user_data, skills_tab) 
                max_sum                        = max_id_in

                for item in uniq_skills:  
                    max_sum       += 1 
                    input_db       = Skills(skill=item )
                    db.session.add(input_db)
                db.session.commit()
    
    




