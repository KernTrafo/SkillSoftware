from app import app, db
from app.models import User
from flask_migrate import Migrate
from app.models import Skills
from app.preprocessing_all import connect_db 
from app.preprocessing_all import connect_db_all
from app.preprocessing_all import push_new_skills
from sqlalchemy import create_engine
import pandas as pd

# engine = create_engine('mysql+pymysql://root:@KTDB2021@app_db:3306/kerntrafo')
engine = create_engine('sqlite:///app.db')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    # write skills into skills table
    new_skills = []
    for line in open('needed_skills.txt', 'r').readlines():
        new_skills.append(line.rstrip('\n'))
    # remove duplicates
    new_skills = list(dict.fromkeys(new_skills))
    # get old skills
    conn = engine.connect()
    old_skills = list(pd.read_sql_table('skills', conn)['skill'])
    conn.close()
    # combine old and new skills
    skills_list = old_skills + new_skills
    skills_list = list(dict.fromkeys(skills_list))
    skills_list = [x for x in skills_list if x not in old_skills]
    # add skills
    for skill in skills_list:
        skill_inpt = Skills(skill=skill)
        db.session.add(skill_inpt)
    db.session.commit()
    connect_db_all.connect_mysql()

    # start app
    migrate = Migrate(app, db)
    app.run()   
    