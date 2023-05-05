import ast
import hashlib
import numpy as np
import pandas as pd
from flask import render_template, redirect, request, url_for, abort
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import create_engine
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegisterForm, ResendVerification, PasswordResetForm, ContactForm, ResetPasswordForm, DataForm, MatchingForm, PredictionForm, PredictionContactForm, KompetenzanalyseForm
from app.models import SkillMatching, User, UserData, Stellenanzeigen, UserMessages, Skills, UserSkills
from app.email import send_activation_email, send_password_reset_email, send_contact_email, send_user_message, send_success_email
from app.formdata import data_submit, pre_populate
from app.helper import password_check
from itsdangerous import URLSafeTimedSerializer

from app.preprocessing_all import connect_db
from app.preprocessing_all import connect_db_all
from app.preprocessing_all import push_new_skills

engine = create_engine('mysql+pymysql://root:@KTDB2021@app_db:3306/kerntrafo')
# engine = create_engine('sqlite:///app.db')

ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

development_mode = True


@app.before_first_request
def write_skills():
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


@app.route('/', methods=('GET', 'POST'))
@login_required
def index():
    contact_form = ContactForm()
    prediction_form = PredictionForm()
    predictioncontact_form = PredictionContactForm()
    matching_form = MatchingForm()
    kompetenz_form = KompetenzanalyseForm()
    user_data = UserData.query.filter_by(user_id=current_user.get_id()).first()
    matching_data = Stellenanzeigen.query.all()
    # get all skills
    skills_file = open('needed_skills.txt', 'r')
    skill_data = []
    for line in skills_file.readlines():
        skill_data.append(line.rstrip('\n'))
    # remove duplicates
    skill_data = sorted(list(dict.fromkeys(skill_data)))
    conn = engine.connect()
    user_skills_df = pd.read_sql_table('user_skills', conn)
    conn.close()
    # list user skills in identified skills list...
    user_skills_df = user_skills_df[user_skills_df['user_id'] == int(current_user.get_id())]
    user_skills = []
    for i in user_skills_df['skill_id']:
        skill = Skills.query.filter_by(id=i).first().skill
        user_skills.append(skill)
    # delete user skills from recommendations
    skill_data = sorted(list(set(skill_data) - set(user_skills)))
    user_count = UserData.query.group_by(UserData.user_id).count()
    reload_jobrequest_modal = False
    show_messagesuccess_modal = False
    nav = 'overview'
    f1 = False
    f2 = False
    f3 = False
    skills = False
    match_skills = []
    stellenplan_q_df = pd.DataFrame()
    stellenplan_df = pd.read_excel('Stellenplan_V2.3.xlsx')
    stellenplan_df['Stellenbezeichnung'] = stellenplan_df['Stellenbezeichnung'].replace('', np.nan)
    stellenplan_df = stellenplan_df['Stellenbezeichnung'].dropna()
    skills_jobanzeige = False
    top_ranks = False
    eval_user_with_skill = False
    skill_not_available = False
    if user_data is None:
        user_missing = True
    else:
        user_missing = False
    # prediction
    if prediction_form.prediction_submit.data:
        if prediction_form.validate():
            nav = 'jobprediction'
            # diese Funktion gibt drei Flags und einen Dic zurück:
            # skills, f1 (gesundheit_atemschutztauglichkeit), f2(gesundheit_schichttauglichkeit), f3(gesundheit_kontrollbereichstauglichkeit ),top_ranks =connect_db.connect_mysql(int(user_id))
            # top_ranks entspricht einem Dic, wobei die Schlüssel der Berufsbezeichnung und die Werte den Scores entsprechen.
            # Z.B:  Top_ranks: top_ranks = ('Strahlenschutz Messtechnik', 0.0), ('Sachbearbeiter Dokumentation', 0.0)
            # gesundheit_atemschutztauglichkeit, gesundheit_schichttauglichkeit, gesundheit_kontrollbereichstauglichkeit sind entweder True oder False für weitere Verwendung.
            # skills = ['informatik', 'leiter']
            # match_list = ['Informatik'] falls das gematch wurde
            match_list, match_skills, skills, skills_jobanzeige, f1, f2, f3, top_ranks, stellenplan_q_df = connect_db.connect_mysql(int(current_user.get_id()))
            # push new user skills to db
            conn = engine.connect()
            old_skills = pd.read_sql_table('user_skills', conn)
            conn.close()
            old_skills = list(old_skills[old_skills['user_id']==int(current_user.get_id())]['skill_id'])
            new_skills = []
            for skl in skills[0]:
                try:
                    new_skills.append(Skills.query.filter_by(skill=skl).first().id)
                except AttributeError:
                    skill_inpt = Skills(skill=skl)
                    db.session.add(skill_inpt)
                    db.session.commit() 
                    new_skills.append(Skills.query.filter_by(skill=skl).first().id)

            u_sk = [x for x in new_skills if x not in old_skills]
            u_sk = sorted(list(dict.fromkeys(u_sk)))
            for skill in u_sk:
                skill_inpt = UserSkills(user_id=current_user.get_id(), skill_id=skill)
                db.session.add(skill_inpt)
            db.session.commit()
            user_skills = user_skills + skills[0]
            user_skills = sorted(list(dict.fromkeys(user_skills)))
    # user job request
    elif predictioncontact_form.predictioncontact_submit.data:
        if predictioncontact_form.validate():
            show_messagesuccess_modal = True
            email = User.query.filter_by(
                id=current_user.get_id()).first().email
            subject = predictioncontact_form.predictioncontact_subject.data
            message = predictioncontact_form.predictioncontact_message.data
            send_user_message(email=email, subject=subject, message=message)
            show_messagesuccess_modal = True
        else:
            reload_jobrequest_modal = True
    elif kompetenz_form.kompetenzanalyse_submit.data:
        eval_skill = kompetenz_form.kompetenzanalyse_input.data.lower()
        total_users = len(User.query.all())
        try:
            skill_id = Skills.query.filter_by(skill=eval_skill).first().id
            users_with_skill = UserSkills.query.filter_by(
                skill_id=skill_id).count()
            eval_user_with_skill = int((users_with_skill / total_users) * 100)
            if eval_user_with_skill == 0:
                skill_not_available = True
        except AttributeError:
            skill_not_available = True
        nav = 'kompetenzanalyse'
    elif request.method == 'POST':
        if request.form['submitkompetenz'] in ['SaveUserSkills']:
            # write manually added user skills to user_skills table
            manual_user_skills = [x.split('\xa0')[0] for x in request.form.getlist('user_skills_checkbox') if x != '']
            manual_user_skills = sorted(list(dict.fromkeys(manual_user_skills)))
            # update user skills in db
            UserSkills.query.filter_by(user_id=current_user.get_id()).delete()
            for skill in manual_user_skills:
                try:
                    skill_inpt = int(Skills.query.filter_by(skill=skill).first().id)
                except AttributeError:
                    new_skill = Skills(skill=skill)
                    db.session.add(new_skill)
                    db.session.commit()
                    skill_inpt = int(Skills.query.filter_by(skill=skill).first().id)
                skill_inpt = UserSkills(
                    user_id = current_user.get_id(),
                    skill_id = skill_inpt)
                db.session.add(skill_inpt)
            db.session.commit()
            user_skills = manual_user_skills
            nav = 'kompetenzanalyse'
    return render_template(
        'index.html',
        title='index',
        development_mode=development_mode,
        contactForm=contact_form,
        userMissing=user_missing,
        userCount=user_count,
        matchingForm=matching_form,
        matchingData=matching_data,
        predictionForm=prediction_form,
        predictioncontactForm=predictioncontact_form,
        kompetenzForm=kompetenz_form,
        reload_jobrequest_modal=reload_jobrequest_modal,
        show_messagesuccess_modal=show_messagesuccess_modal,
        nav=nav,
        f1=f1,
        f2=f2,
        f3=f3,
        skills=skills,
        match_skills=match_skills,
        skills_jobanzeige=skills_jobanzeige,
        stellenplan=stellenplan_df,
        skill_data=skill_data,
        top_ranks=top_ranks,
        eval_user_with_skill=eval_user_with_skill,
        skill_not_available=skill_not_available,
        user_skills=user_skills
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    register_form = RegisterForm()
    resend_form = ResendVerification()
    pwreset_form = PasswordResetForm()
    contact_form = ContactForm()
    show_domain_notification = False
    show_password_notification = False
    reload_register_form = False
    reload_login_form = False
    reload_pw_reset = False
    reload_contact_form = False
    message_success = False
    wrong_invite_code = False
    emailConfirmed = False
    emailConfirmednon = False
    # login
    if login_form.login_submit.data and login_form.validate():
        user = User.query.filter_by(
            email=login_form.login_email.data.lower()).first()
        if user is None or not user.check_password(
                login_form.login_password.data):
            reload_login_form = True
        elif user.email_confirmed == False:
            resend_form.verification_email.data = login_form.login_email.data
            emailConfirmed = 'resend'
        else:
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    # register
    elif register_form.register_submit.data:
        if register_form.validate():
            # only allow registration for specific domains
            allowed_domains = [
                'rwe.com',
                'kkw.rwe.com',
                'fh-swf.de',
                'gmail.com']
            email_domain = register_form.register_email.data.lower().split(
                '@')[-1]
            if email_domain in allowed_domains:
                # enforce complex passwords
                if password_check(
                        register_form.register_password.data)['password_ok']:
                    hash = hashlib.sha256()
                    hash.update(
                        register_form.register_email.data.lower().encode('utf-8'))
                    user = User(
                        email=register_form.register_email.data.lower(),
                        email_confirmed=False,
                        pseudonym=hash.hexdigest()
                    )
                    user.set_password(register_form.register_password.data)
                    db.session.add(user)
                    db.session.commit()
                    token = ts.dumps(user.email, salt='email-confirm-key')
                    confirm_url = url_for(
                        'confirm_email', token=token, _external=True)
                    send_activation_email(user.email, confirm_url)
                    emailConfirmed = 'registered'
                else:
                    show_password_notification = True
                    reload_register_form = True
            else:
                show_domain_notification = True
                reload_register_form = True
        else:
            reload_register_form = True
    # resend e-mail verification
    elif resend_form.verification_submit.data:
        if resend_form.validate():
            user = User.query.filter_by(
                email=resend_form.verification_email.data).first()
            if user:
                token = ts.dumps(user.email, salt='email-confirm-key')
                confirm_url = url_for(
                    'confirm_email', token=token, _external=True)
                send_activation_email(user.email, confirm_url)
            else:
                emailConfirmed = 'resend'
                emailConfirmednon = True
        else:
            emailConfirmed = 'resend'
    # password reset
    elif pwreset_form.pwreset_submit.data:
        if pwreset_form.validate():
            user = User.query.filter_by(
                email=pwreset_form.pwreset_email.data.lower()).first()
            if user:
                send_password_reset_email(user)
            else:
                reload_pw_reset = True
        else:
            reload_pw_reset = True
    # contactya
    elif contact_form.contact_submit.data:
        if contact_form.validate():
            # anti spam honeypot
            if contact_form.contact_body.data == '':
                name = contact_form.contact_name.data
                email = contact_form.contact_email.data.lower()
                message = contact_form.contact_message.data
                send_contact_email(name=name, email=email, message=message)
                message_success = True
        else:
            reload_contact_form = True
    return render_template(
        'login.html',
        title='login',
        development_mode=development_mode,
        loginForm=login_form,
        registerForm=register_form,
        resendVerification=resend_form,
        pwresetrequestForm=pwreset_form,
        contactForm=contact_form,
        show_domain_notification=show_domain_notification,
        show_password_notification=show_password_notification,
        emailConfirmed=emailConfirmed,
        emailConfirmednon=emailConfirmednon,
        reload_register_form=reload_register_form,
        reload_login_form=reload_login_form,
        reload_pw_reset=reload_pw_reset,
        reload_contact_form=reload_contact_form,
        message_success=message_success,
        wrong_invite_code=wrong_invite_code
    )


@app.route('/confirm_email/<token>', methods=['GET', 'POST'])
def confirm_email(token):
    try:
        email = ts.loads(token, salt='email-confirm-key', max_age=86400)
    except BaseException:
        abort(404)
    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True
    db.session.add(user)
    db.session.commit()
    return render_template(
        'confirm.html',
        title='confirm',
        development_mode=development_mode,
    )


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    pwreset_form = ResetPasswordForm()
    contact_form = ContactForm()
    show_password_notification = False
    password_reset_success = False
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('login'))
    if pwreset_form.validate_on_submit():
        if password_check(pwreset_form.pwreset_password.data)['password_ok']:
            user.set_password(pwreset_form.pwreset_password.data)
            db.session.commit()
            password_reset_success = True
        else:
            show_password_notification = True
    return render_template(
        'reset_password.html',
        title='reset_password',
        development_mode=development_mode,
        contactForm=contact_form,
        pwresetForm=pwreset_form,
        show_password_notification=show_password_notification,
        password_reset_success=password_reset_success
    )


@app.route('/daten', methods=('GET', 'POST'))
@login_required
def daten():
    contact_form = ContactForm()
    data_form = DataForm(request.form)
    user_missing = False
    studium = False
    ausbildung = False
    kenntnisse = False
    sprachen = False
    berufe = False
    projekte = False
    weiterbildungen = False
    geplanteweiterbildungen = False
    freizeit = False
    ehrenamtlich = False
    nebenjobs = False
    if request.method == 'POST':
        if request.form['submitbutton'] == 'Datenfreigabe':
            inpt = data_submit()
            db.session.add(inpt)
            db.session.commit()
            user = User.query.filter_by(id=current_user.get_id()).first()
            send_success_email(user)

            return redirect(url_for('submission_success'))
    user_data = UserData.query.filter_by(
        user_id=current_user.get_id()).order_by(
        UserData.timestamp.desc()).first()
    if user_data is None:
        user_missing = True
    else:
        studium_bezeichnung = ast.literal_eval(user_data.data_studium)
        studium_schwerpunkt = ast.literal_eval(
            user_data.data_studium_schwerpunkt)
        studium_von = ast.literal_eval(user_data.data_studium_von)
        studium_bis = ast.literal_eval(user_data.data_studium_bis)
        studium = list(
            zip(studium_bezeichnung, studium_schwerpunkt, studium_von, studium_bis))
        if len(studium) == 0:
            studium = False
        ausbildung_bezeichnung = ast.literal_eval(user_data.data_ausbildung)
        ausbildung_schwerpunkt = ast.literal_eval(
            user_data.data_ausbildung_schwerpunkt)
        ausbildung_von = ast.literal_eval(user_data.data_ausbildung_von)
        ausbildung_bis = ast.literal_eval(user_data.data_ausbildung_bis)
        ausbildung = list(zip(ausbildung_bezeichnung,
                              ausbildung_schwerpunkt,
                              ausbildung_von,
                              ausbildung_bis))
        if len(ausbildung) == 0:
            ausbildung = False
        kenntnisse_select = ast.literal_eval(user_data.data_kenntnisse)
        kenntnisse_niveau = ast.literal_eval(user_data.data_kenntnisse_niveau)
        kenntnisse = list(zip(kenntnisse_select, kenntnisse_niveau))
        if len(kenntnisse) == 0:
            kenntnisse = False
        sprachen_select = ast.literal_eval(user_data.data_sprachen)
        sprachen_niveau = ast.literal_eval(user_data.data_sprachen_niveau)
        sprachen = list(zip(sprachen_select, sprachen_niveau))
        if len(sprachen) == 0:
            sprachen = False
        beruf_bezeichnung = ast.literal_eval(user_data.data_berufsbezeichnung)
        beruf_beschreibung = ast.literal_eval(
            user_data.data_berufsbeschreibung)
        beruf_unternehmen = ast.literal_eval(user_data.data_unternehmen)
        beruf_von = ast.literal_eval(user_data.data_beruf_von)
        beruf_bis = ast.literal_eval(user_data.data_beruf_bis)
        berufe = list(zip(beruf_bezeichnung, beruf_beschreibung,
                      beruf_unternehmen, beruf_von, beruf_bis))
        if len(berufe) == 0:
            berufe = False
        projekt_titel = ast.literal_eval(user_data.data_projekttitel)
        projekt_rolle = ast.literal_eval(user_data.data_projektrolle)
        projekt_bezeichnung = ast.literal_eval(
            user_data.data_projektbezeichnung)
        projekt_beschreibung = ast.literal_eval(
            user_data.data_projektbeschreibung)
        projekt_von = ast.literal_eval(user_data.data_projekt_von)
        projekt_bis = ast.literal_eval(user_data.data_projekt_bis)
        projekte = list(zip(projekt_titel,
                            projekt_rolle,
                            projekt_bezeichnung,
                            projekt_beschreibung,
                            projekt_von,
                            projekt_bis))
        if len(projekte) == 0:
            projekte = False
        weiterbildung_bezeichnung = ast.literal_eval(
            user_data.data_weiterbildungsbezeichnung)
        weiterbildung_beschreibung = ast.literal_eval(
            user_data.data_weiterbildungsbeschreibung)
        weiterbildung_von = ast.literal_eval(user_data.data_weiterbildung_von)
        weiterbildung_bis = ast.literal_eval(user_data.data_weiterbildung_bis)
        weiterbildungen = list(zip(weiterbildung_bezeichnung,
                                   weiterbildung_beschreibung,
                                   weiterbildung_von,
                                   weiterbildung_bis))
        if len(weiterbildungen) == 0:
            weiterbildungen = False
        weiterbildung_thema = ast.literal_eval(
            user_data.data_weiterbildung_thema)
        weiterbildung_warum = ast.literal_eval(
            user_data.data_weiterbildung_warum)
        geplanteweiterbildungen = list(
            zip(weiterbildung_thema, weiterbildung_warum))
        if len(geplanteweiterbildungen) == 0:
            geplanteweiterbildungen = False
        freizeit = ast.literal_eval(user_data.data_freizeit)
        if len(freizeit) == 0:
            freizeit = False
        ehrenamtlich = ast.literal_eval(user_data.data_ehrenamtlich)
        if len(ehrenamtlich) == 0:
            ehrenamtlich = False
        nebenjobs = ast.literal_eval(user_data.data_nebenjobs)
        if len(nebenjobs) == 0:
            nebenjobs = False
        data_form = pre_populate()
    return render_template(
        'daten.html',
        title='daten',
        development_mode=development_mode,
        contactForm=contact_form,
        dataForm=data_form,
        userData=user_data,
        userMissing=user_missing,
        studium=studium,
        ausbildung=ausbildung,
        kenntnisse=kenntnisse,
        sprachen=sprachen,
        berufe=berufe,
        projekte=projekte,
        weiterbildungen=weiterbildungen,
        geplanteweiterbildungen=geplanteweiterbildungen,
        freizeit=freizeit,
        ehrenamtlich=ehrenamtlich,
        nebenjobs=nebenjobs,
    )


@app.route('/submission_success', methods=['GET', 'POST'])
def submission_success():
    return render_template(
        'submission_success.html',
    )


@app.route('/nachrichten', methods=('GET', 'POST'))
@login_required
def nachrichten():
    contact_form = ContactForm()
    user_messages = UserMessages.query.filter_by(
        user_id=current_user.get_id()).order_by(
        UserMessages.date.desc()).all()
    return render_template(
        'nachrichten.html',
        title='nachrichten',
        development_mode=development_mode,
        contactForm=contact_form,
        userMessages=user_messages,
    )


@app.route('/impressum')
def impressum():
    register_form = RegisterForm()
    login_form = LoginForm()
    pwreset_form = PasswordResetForm()
    contact_form = ContactForm()
    return render_template(
        'impressum.html',
        title='impressum',
        development_mode=development_mode,
        loginForm=login_form,
        registerForm=register_form,
        pwresetrequestForm=pwreset_form,
        contactForm=contact_form,
    )


@app.route('/datenschutz')
def datenschutz():
    register_form = RegisterForm()
    login_form = LoginForm()
    pwreset_form = PasswordResetForm()
    contact_form = ContactForm()
    return render_template(
        'datenschutz.html',
        title='datenschutz',
        development_mode=development_mode,
        loginForm=login_form,
        registerForm=register_form,
        pwresetrequestForm=pwreset_form,
        contactForm=contact_form,
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/message', methods=['POST'])
@login_required
def message():
    contact_form = ContactForm()
    matching_form = MatchingForm()
    user_data = UserData.query.filter_by(user_id=current_user.get_id()).first()
    matching_data = Stellenanzeigen.query.all()
    user_count = UserData.query.group_by(UserData.user_id).count()
    show_messagesuccess_modal = True
    if user_data is None:
        user_missing = True
    else:
        user_missing = False
    subject = request.form['contact-subject']
    message = request.form['contact-message']
    if request.form['messageType'] == 'userRequest':
        nav = 'overview'
        id = request.form['hidden_user_id']
        recruiter_id = current_user.get_id()
        category = 'Skillmatching'
        type = 'recruiter'
        send_user_message(
            id=id,
            recruiter_id=recruiter_id,
            subject=subject,
            message=message,
            category=category,
            type=type)
        return render_template(
            'index.html',
            title='index',
            development_mode=development_mode,
            contactForm=contact_form,
            userMissing=user_missing,
            userCount=user_count,
            matchingForm=matching_form,
            matchingData=matching_data,
            show_messagesuccess_modal=show_messagesuccess_modal,
            nav=nav,
        )
    elif request.form['messageType'] == 'userReply':
        user_messages = UserMessages.query.filter_by(
            user_id=current_user.get_id()).order_by(
            UserMessages.date.desc()).all()
        id = current_user.get_id()
        recruiter_id = request.form['hidden_recruiter_id']
        category = 'Skillmatching'
        type = 'user'
        send_user_message(
            id=id,
            recruiter_id=recruiter_id,
            subject=subject,
            message=message,
            category=category,
            type=type)
        return render_template(
            'nachrichten.html',
            title='nachrichten',
            development_mode=development_mode,
            contactForm=contact_form,
            userMessages=user_messages,
            show_messagesuccess_modal=show_messagesuccess_modal,
        )


@app.route('/matching', methods=['POST'])
def matching():
    contact_form = ContactForm()
    matching_form = MatchingForm()
    user_data = UserData.query.filter_by(user_id=current_user.get_id()).first()
    matching_data = Stellenanzeigen.query.all()
    user_count = UserData.query.group_by(UserData.user_id).count()
    nav = 'overview'
    usermatches = False
    match_skills = ''
    stellenanzeige_body = ''
    if user_data is None:
        user_missing = True
    else:
        user_missing = False
    if request.method == 'POST':
        if request.form['submitbutton'] in ['SaveMatching', 'Matchen']:
            if matching_form.matching_stellenbezeichnung.data != '':
                stellenanzeige_body = ''
                inpt = Stellenanzeigen(
                    recruiter_id=current_user.get_id(),
                    job_title=matching_form.matching_stellenbezeichnung.data,
                    ort=matching_form.matching_ort.data,
                    fachgebiet=matching_form.matching_fachgebiet.data,
                    erfahrung=matching_form.matching_erfahrung.data,
                    skills=matching_form.matching_skills.data,
                    body=stellenanzeige_body,
                    besetzt=False,
                )
                db.session.add(inpt)
                db.session.commit()
                # write job id in hidden field
                # request.form['job_id'] = Stellenanzeigen.query.order_by(Stellenanzeigen.id.desc()).first()
                if request.form['submitbutton'] == 'Matchen':
                    pass
    return render_template(
        'index.html',
        title='index',
        development_mode=development_mode,
        contactForm=contact_form,
        userMissing=user_missing,
        userCount=user_count,
        matchingForm=matching_form,
        matchingData=matching_data,
        nav=nav,
        stellenanzeigeBody=stellenanzeige_body,
        userMatches=usermatches,
        matchSkills=match_skills,
    )
