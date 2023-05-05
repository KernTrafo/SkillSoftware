import jwt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from time import time
from app import app, db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    passwort = db.Column(db.Text)
    email_confirmed = db.Column(db.Boolean)
    pseudonym = db.Column(db.Text)
    userdata = db.relationship('UserData', lazy='dynamic')
    usermessages = db.relationship('UserMessages', lazy='dynamic')
    userconsents = db.relationship('UserConsents', lazy='dynamic')
    skillmatching = db.relationship('SkillMatching', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.passwort = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwort, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'exp': time(
        ) + expires_in}, app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithms=['HS256'])['reset_password']
        except BaseException:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)

    # Persönliche Daten
    data_bildungsgrad = db.Column(db.Text)
    fachrichtung_elektrotechnik = db.Column(db.Boolean)
    fachrichtung_maschinentechnik = db.Column(db.Boolean)
    fachrichtung_verfahrenstechnik = db.Column(db.Boolean)
    fachrichtung_strahlenschutz = db.Column(db.Boolean)
    fachrichtung_strahlenschutzwerker = db.Column(db.Boolean)
    fachrichtung_strahlenschutzfachkraft = db.Column(db.Boolean)
    andere_fachrichtung = db.Column(db.Text)
    data_vorname = db.Column(db.Text)
    data_nachname = db.Column(db.Text)
    data_geburtsdatum = db.Column(db.Text)
    data_geschlecht = db.Column(db.Text)
    data_familienstand = db.Column(db.Text)
    data_plz = db.Column(db.Integer)
    data_ort = db.Column(db.Text)
    data_reisebereitschaft = db.Column(db.Text)
    data_sonstige_persoenliche = db.Column(db.Text)

    # Fachliche Qualifikation
    data_studium = db.Column(db.Text)
    data_studium_schwerpunkt = db.Column(db.Text)
    data_studium_von = db.Column(db.Text)
    data_studium_bis = db.Column(db.Text)
    data_ausbildung = db.Column(db.Text)
    data_ausbildung_schwerpunkt = db.Column(db.Text)
    data_ausbildung_von = db.Column(db.Text)
    data_ausbildung_bis = db.Column(db.Text)
    data_kenntnisse = db.Column(db.Text)
    data_kenntnisse_niveau = db.Column(db.Text)
    data_sprachen = db.Column(db.Text)
    data_sprachen_niveau = db.Column(db.Text)
    data_fuehrerschein_AM = db.Column(db.Boolean)
    data_fuehrerschein_A1 = db.Column(db.Boolean)
    data_fuehrerschein_A2 = db.Column(db.Boolean)
    data_fuehrerschein_A = db.Column(db.Boolean)
    data_fuehrerschein_B1 = db.Column(db.Boolean)
    data_fuehrerschein_B = db.Column(db.Boolean)
    data_fuehrerschein_C1 = db.Column(db.Boolean)
    data_fuehrerschein_C = db.Column(db.Boolean)
    data_fuehrerschein_D1 = db.Column(db.Boolean)
    data_fuehrerschein_D = db.Column(db.Boolean)
    data_fuehrerschein_BE = db.Column(db.Boolean)
    data_fuehrerschein_C1E = db.Column(db.Boolean)
    data_fuehrerschein_CE = db.Column(db.Boolean)
    data_fuehrerschein_D1E = db.Column(db.Boolean)
    data_fuehrerschein_DE = db.Column(db.Boolean)
    data_fuehrerschein_L = db.Column(db.Boolean)
    data_fuehrerschein_M = db.Column(db.Boolean)
    data_fuehrerschein_S = db.Column(db.Boolean)
    data_fuehrerschein_T = db.Column(db.Boolean)
    data_fuehrerschein_Staplerschein = db.Column(db.Boolean)
    data_fuehrerschein_Kranschein = db.Column(db.Boolean)
    data_potenzielle_berufe = db.Column(db.Text)
    data_missing_skills = db.Column(db.Text)
    data_sonstige_fachliche = db.Column(db.Text)

    # Berufserfahrung
    data_aktuelle_berufsbezeichnung = db.Column(db.Text)
    data_aktuelle_berufsbeschreibung = db.Column(db.Text)
    data_taetigkeitsstandort = db.Column(db.Text)
    data_bei_rwe_seit = db.Column(db.Text)
    data_berufsbezeichnung = db.Column(db.Text)
    data_berufsbeschreibung = db.Column(db.Text)
    data_unternehmen = db.Column(db.Text)
    data_beruf_von = db.Column(db.Text)
    data_beruf_bis = db.Column(db.Text)
    data_sonstige_berufserfahrung = db.Column(db.Text)

    # Projekterfahrung
    data_projekttitel = db.Column(db.Text)
    data_projektrolle = db.Column(db.Text)
    data_projektbezeichnung = db.Column(db.Text)
    data_projektbeschreibung = db.Column(db.Text)
    data_projekt_von = db.Column(db.Text)
    data_projekt_bis = db.Column(db.Text)
    data_sonstige_projekterfahrung = db.Column(db.Text)

    # Weiterbildungen
    data_weiterbildungsbezeichnung = db.Column(db.Text)
    data_weiterbildungsbeschreibung = db.Column(db.Text)
    data_weiterbildung_von = db.Column(db.Text)
    data_weiterbildung_bis = db.Column(db.Text)
    data_sonstige_weiterbildung = db.Column(db.Text)

    # Geplante Weiterbildungen
    data_weiterbildung_thema = db.Column(db.Text)
    data_weiterbildung_warum = db.Column(db.Text)
    data_sonstige_geplante = db.Column(db.Text)

    # Gesundheit
    gesundheit_atemschutztauglichkeit = db.Column(db.Boolean)
    gesundheit_atemschutztauglichkeit_date = db.Column(db.Text)
    gesundheit_kontrollbereichstauglichkeit = db.Column(db.Boolean)
    gesundheit_kontrollbereichstauglichkeit_date = db.Column(db.Text)
    gesundheit_schichttauglichkeit = db.Column(db.Boolean)
    gesundheit_schichttauglichkeit_date = db.Column(db.Text)
    data_sonstige_gesundheit = db.Column(db.Text)

    # Interessen
    data_freizeit = db.Column(db.Text)
    data_ehrenamtlich = db.Column(db.Text)
    data_nebenjobs = db.Column(db.Text)
    data_sonstige_interessen = db.Column(db.Text)


class UserMessages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'))
    category = db.Column(db.Text)
    post_id = db.Column(db.Integer)
    subject = db.Column(db.Text)
    message = db.Column(db.Text)
    link = db.Column(db.Text)
    type = db.Column(db.Text)
    date = db.Column(db.DateTime, index=True, default=datetime.now)


class UserConsents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_privacy = db.Column(db.Boolean)
    ai_privacy = db.Column(db.Boolean)


class SkillMatching(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('stellenanzeigen.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Float)


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.Text)
    userskills = db.relationship('UserSkills', lazy='dynamic')


class UserSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'))


class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    passwort = db.Column(db.Text)
    vorname = db.Column(db.Text)
    nachname = db.Column(db.Text)
    abteilung = db.Column(db.Text)
    stellenanzeigen_id = db.relationship('Stellenanzeigen', lazy='dynamic')
    usermessages_id = db.relationship('UserMessages', lazy='dynamic')


class Stellenanzeigen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'))
    job_title = db.Column(db.Text)
    ort = db.Column(db.Text)
    fachgebiet = db.Column(db.Text)
    erfahrung = db.Column(db.Text)
    skills = db.Column(db.Text)
    body = db.Column(db.Text)
    besetzt = db.Column(db.Boolean)
    skillmatching_id = db.relationship('SkillMatching', lazy='dynamic')
