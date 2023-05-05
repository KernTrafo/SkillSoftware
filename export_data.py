from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
import os

# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
engine = create_engine("mysql+pymysql://root:@KTDB2021@app_db:3306/kerntrafo")
print('engine created')
dbConnection = engine.connect()
print('connected to db')
query_user = "SELECT id, pseudonym FROM user;"
query_user_data = "SELECT * FROM user_data;"
user_df = pd.read_sql_query(query_user, dbConnection)
print('reading user table done')
private_columns = ['data_vorname', 'data_nachname', 'data_geburtsdatum', 'data_geschlecht', 'data_familienstand']
userdata_df = pd.read_sql_query(query_user_data, dbConnection).drop(columns=private_columns)
print('reading userdata_done')
#print(userdata_df.head())
total_df = userdata_df.merge(user_df, left_on='user_id', right_on='id')
print("merging done")
date = datetime.now().strftime("%Y_%m_%d")
total_df.to_csv('data_export_{}.csv'.format(date))
print("Exporting data successful")

query_skills = "SELECT * FROM skills;"
skills_df = pd.read_sql_query(query_skills, dbConnection)
query_user_skills = "SELECT * FROM user_skills;"
user_skills_df = pd.read_sql_query(query_user_skills, dbConnection)
skills_df = user_skills_df.merge(skills_df, left_on='skill_id', right_on="id")
skills_df.to_csv('skills_export_{}.csv'.format(date))
