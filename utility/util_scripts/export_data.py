from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
engine = create_engine("mysql+pymysql://root:@KTDB2021@db:3306/kerntrafo")
print('engine created')
dbConnection = engine.connect()
print('connected to db')
query_user = "SELECT id, pseudonym FROM user;"
query_user_data = "SELECT * FROM user_data;"
user_df = pd.read_sql_query(query_user, dbConnection)
print('reading user table done')
private_columns = ['data_vorname', 'data_nachname', 'data_geburtsdatum', 'data_geschlecht', 'data_familienstand']
userdata_df = pd.read_sql_query(query_user_data, dbConnection).drop(columns=private_columns)
print('reading user data done')
#print(userdata_df.head())
total_df = userdata_df.merge(user_df, left_on='user_id', right_on='id')
print("merging done")
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
total_df.to_csv('data_export_{}.csv'.format(date))
print("exporting data successful")
