from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import HiddenField
from wtforms.form import Form
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    login_email = StringField(
        'login_email',
        render_kw={
            'placeholder': 'E-Mail',
            'autocomplete': 'email'},
        validators=[
            DataRequired(),
            Length(
                min=5,
                max=35),
            Email()])
    login_password = PasswordField(
        'login_password',
        render_kw={
            'placeholder': 'Passwort',
            'autocomplete': 'current-password'},
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=15)])
    login_submit = SubmitField('loginbutton')


class RegisterForm(FlaskForm):
    register_email = StringField(
        'register_email',
        render_kw={
            'placeholder': 'E-Mail',
            'autocomplete': 'email'},
        validators=[
            DataRequired(),
            Length(
                min=5,
                max=35),
            Email()])
    register_password = PasswordField(
        'register_password',
        render_kw={
            'placeholder': 'Passwort',
            'autocomplete': 'new-password'},
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=15)])
    register_password_confirm = PasswordField(
        'register_password_confirm',
        render_kw={
            'placeholder': 'Passwort wiederholen',
            'autocomplete': 'new-password'},
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=15),
            EqualTo(
                'register_password',
                message='Die Passwörter stimmen nicht überein.')])
    register_submit = SubmitField('registerbutton')

    def validate_register_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Diese E-Mail ist bereits registriert.')


class ResendVerification(FlaskForm):
    verification_email = StringField(
        'verification_email',
        render_kw={
            'placeholder': 'E-Mail',
            'autocomplete': 'email'},
        validators=[
            DataRequired(),
            Length(
                min=5,
                max=35),
            Email()])
    verification_submit = SubmitField('verificationbutton')


class PasswordResetForm(FlaskForm):
    pwreset_email = StringField(
        'pwreset_email',
        render_kw={
            'placeholder': 'E-Mail',
            'autocomplete': 'email'},
        validators=[
            DataRequired(),
            Length(
                min=5,
                max=35),
            Email()])
    pwreset_submit = SubmitField('pwresetbutton')


class ResetPasswordForm(FlaskForm):
    pwreset_password = PasswordField(
        'pwreset_password',
        render_kw={
            'placeholder': 'Passwort',
            'autocomplete': 'new-password'},
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=15)])
    pwreset_password_confirm = PasswordField(
        'pwreset_password_confirm',
        render_kw={
            'placeholder': 'Passwort wiederholen',
            'autocomplete': 'new-password'},
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=15),
            EqualTo(
                'pwreset_password',
                message='Die Passwörter stimmen nicht überein.')])
    pwreset_submit = SubmitField('resetpasswordbutton')


class PredictionForm(FlaskForm):
    prediction_submit = SubmitField('predictionbutton')


class PredictionContactForm(FlaskForm):
    predictioncontact_subject = TextAreaField(
        'predictioncontact_subject',
        render_kw={
            'placeholder': 'Betreff',
            'rows': '1'},
        validators=[
            DataRequired()])
    predictioncontact_message = TextAreaField(
        'predictioncontact_message',
        render_kw={
            'placeholder': 'Nachricht',
            'rows': '5'},
        validators=[
            DataRequired()])
    predictioncontact_submit = SubmitField('predictioncontactbutton')


class ContactForm(FlaskForm):
    contact_name = StringField(
        'contact_name',
        render_kw={
            'placeholder': 'Ihr Name',
            'autocomplete': 'name'},
        validators=[
            DataRequired()])
    contact_email = StringField(
        'contact_email',
        render_kw={
            'placeholder': 'Ihre E-Mail',
            'autocomplete': 'email'},
        validators=[
            DataRequired(),
            Email()])
    contact_message = TextAreaField(
        'contact_message',
        render_kw={
            'placeholder': 'Ihre Nachricht',
            'rows': '5'},
        validators=[
            DataRequired()])
    contact_body = TextAreaField(
        'honeypot',
        render_kw={
            'placeholder': 'Bitte hier nichts eintragen',
            'rows': '1'})
    contact_submit = SubmitField('contactbutton')


class DataForm(Form):
    # Persönliche Daten
    data_bildungsgrad = SelectField(
        'data_geschlecht',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('Handwerker',
             'Handwerker'),
            ('Kaufmännische Fachkraft',
             'Kaufmännische Fachkraft'),
            ('Bachelor',
             'Bachelor'),
            ('Meister / Techniker',
             'Meister / Techniker'),
            ('Master / Diplom (oder vergleichbar)',
             'Master / Diplom (oder vergleichbar)'),
            ('Ingenieur (TU/FH)',
             'Ingenieur (TU/FH)'),
            ('Doktor',
             'Doktor'),
            ('Prof. Dr.',
             'Prof. Dr.')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    fachrichtung_elektrotechnik = BooleanField(
        'fachrichtung_elektrotechnik', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    fachrichtung_maschinentechnik = BooleanField(
        'fachrichtung_maschinentechnik', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    fachrichtung_verfahrenstechnik = BooleanField(
        'fachrichtung_verfahrenstechnik', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    fachrichtung_strahlenschutz = BooleanField(
        'fachrichtung_strahlenschutz', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    fachrichtung_strahlenschutzwerker = BooleanField(
        'fachrichtung_strahlenschutzwerker', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    fachrichtung_strahlenschutzfachkraft = BooleanField(
        'fachrichtung_strahlenschutzfachkraft', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    andere_fachrichtung = StringField(
        'andere_fachrichtung',
        render_kw={
            'placeholder': 'Andere Fachrichtung',
            'onkeydown': 'return event.key != "Enter";'})
    data_vorname = StringField(
        'data_vorname',
        render_kw={
            'placeholder': 'Vorname',
            'onkeydown': 'return event.key != "Enter";'})
    data_nachname = StringField(
        'data_nachname',
        render_kw={
            'placeholder': 'Nachname',
            'onkeydown': 'return event.key != "Enter";'})
    data_geburtsdatum = DateField(
        'data_geburtsdatum',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_geschlecht = SelectField(
        'data_geschlecht',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('männlich',
             'männlich'),
            ('weiblich',
             'weiblich'),
            ('divers',
             'divers')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_familienstand = SelectField(
        'data_familienstand',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('ledig',
             'ledig'),
            ('verheiratet',
             'verheiratet'),
            ('verwitwet',
             'verwitwet'),
            ('geschieden',
             'geschieden'),
            ('Ehe aufgehoben',
             'Ehe aufgehoben'),
            ('in eingetragener Lebenspartnerschaft',
             'in eingetragener Lebenspartnerschaft'),
            ('durch Tod aufgelöste Lebenspartnerschaft',
             'durch Tod aufgelöste Lebenspartnerschaft')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_plz = IntegerField(
        'data_plz',
        render_kw={
            'placeholder': 'PLZ',
            'onkeydown': 'return event.key != "Enter";'})
    data_ort = StringField(
        'data_ort',
        render_kw={
            'placeholder': 'Ort',
            'onkeydown': 'return event.key != "Enter";'})
    data_reisebereitschaft = SelectField(
        'data_reisebereitschaft',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('Ortsgebunden und reisebereit',
             'Ortsgebunden und reisebereit'),
            ('Ortsgebunden und nicht reisebereit',
             'Ortsgebunden und nicht reisebereit'),
            ('Ortsungebunden und reisebereit',
             'Ortsungebunden und reisebereit'),
            ('Ortsungebunden und nicht reisebereit',
             'Ortsungebunden und nicht reisebereit')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_persoenliche = TextAreaField(
        'data_sonstige_persoenliche', render_kw={
            'placeholder': 'Sonstige persönliche Daten'})
    # Fachliche Qualifikation
    data_studium = StringField(
        'data_studium',
        render_kw={
            'placeholder': 'Studium',
            'onkeydown': 'return event.key != "Enter";'})
    data_studium_schwerpunkt = TextAreaField(
        'data_studium_schwerpunkt', render_kw={
            'placeholder': 'Schwerpunkt des Studiums', 'rows': '2'})
    data_studium_von = DateField(
        'data_studium_von',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_studium_bis = DateField(
        'data_studium_bis', render_kw={
            'min': date(
                1900, 1, 1), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    data_ausbildung = StringField(
        'data_ausbildung',
        render_kw={
            'placeholder': 'Ausbildung',
            'onkeydown': 'return event.key != "Enter";'})
    data_ausbildung_schwerpunkt = TextAreaField(
        'data_ausbildung_schwerpunkt', render_kw={
            'placeholder': 'Schwerpunkt der Ausbildung', 'rows': '2'})
    data_ausbildung_von = DateField(
        'data_ausbildung_von',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_ausbildung_bis = DateField(
        'data_ausbildung_bis', render_kw={
            'min': date(
                1900, 1, 1), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    data_kenntnisse = StringField(
        'data_kenntnisse',
        render_kw={
            'placeholder': 'Tool / Skill',
            'onkeydown': 'return event.key != "Enter";'})
    data_kenntnisse_niveau = SelectField(
        'data_kenntnisse_niveau',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('Grundkenntnisse',
             'Grundkenntnisse'),
            ('Gute Kenntnisse',
             'Gute Kenntnisse'),
            ('Professionelle Kenntnisse',
             'Professionelle Kenntnisse')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_sprachen = StringField(
        'data_sprachen',
        render_kw={
            'placeholder': 'Sprache',
            'onkeydown': 'return event.key != "Enter";'})
    data_sprachen_niveau = SelectField(
        'data_sprachen_niveau',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('Grundkenntnisse',
             'Grundkenntnisse'),
            ('Gute Kenntnisse',
             'Gute Kenntnisse'),
            ('Verhandlungssicher',
             'Verhandlungssicher'),
            ('Fliessend',
             'Fliessend'),
            ('Muttersprache oder zweisprachig',
             'Muttersprache oder zweisprachig')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_AM = BooleanField(
        'data_fuehrerschein_AM', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_A1 = BooleanField(
        'data_fuehrerschein_A1', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_A2 = BooleanField(
        'data_fuehrerschein_A2', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_A = BooleanField(
        'data_fuehrerschein_A', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_B1 = BooleanField(
        'data_fuehrerschein_B1', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_B = BooleanField(
        'data_fuehrerschein_B', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_C1 = BooleanField(
        'data_fuehrerschein_C1', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_C = BooleanField(
        'data_fuehrerschein_C', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_D1 = BooleanField(
        'data_fuehrerschein_D1', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_D = BooleanField(
        'data_fuehrerschein_D', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_BE = BooleanField(
        'data_fuehrerschein_BE', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_C1E = BooleanField(
        'data_fuehrerschein_C1E', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_CE = BooleanField(
        'data_fuehrerschein_CE', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_D1E = BooleanField(
        'data_fuehrerschein_D1E', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_DE = BooleanField(
        'data_fuehrerschein_DE', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_L = BooleanField(
        'data_fuehrerschein_L', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_M = BooleanField(
        'data_fuehrerschein_M', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_S = BooleanField(
        'data_fuehrerschein_S', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_T = BooleanField(
        'data_fuehrerschein_T', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_Staplerschein = BooleanField(
        'data_fuehrerschein_Staplerschein', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_fuehrerschein_Kranschein = BooleanField(
        'data_fuehrerschein_Kranschein', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_potenzielle_berufe = StringField(
        'data_potenzielle_berufe',
        render_kw={
            'placeholder': 'Themen / Berufe',
            'onkeydown': 'return event.key != "Enter";'})
    data_missing_skills = StringField(
        'data_missing_skills',
        render_kw={
            'placeholder': 'Fehlende Fähigkeiten',
            'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_fachliche = TextAreaField(
        'data_sonstige_fachliche', render_kw={
            'placeholder': 'Sonstige Angaben zur fachlichen Qualifikation', 'rows': '2'})
    # Berufserfahrung
    data_aktuelle_berufsbezeichnung = StringField(
        'data_aktuelle_berufsbezeichnung',
        render_kw={
            'placeholder': 'Berufsbezeichnung',
            'onkeydown': 'return event.key != "Enter";'})
    data_aktuelle_berufsbeschreibung = TextAreaField(
        'data_aktuelle_berufsbeschreibung', render_kw={
            'placeholder': 'Berufsbeschreibung', 'rows': '2'})
    data_taetigkeitsstandort = SelectField(
        'data_sprachen_niveau',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('Übergreifend',
             'Übergreifend'),
            ('Biblis',
             'Biblis'),
            ('Essen',
             'Essen'),
            ('Gundremmingen',
             'Gundremmingen')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_bei_rwe_seit = DateField(
        'data_bei_rwe_seit',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_berufsbezeichnung = StringField(
        'data_berufsbezeichnung',
        render_kw={
            'placeholder': 'Vergangene Berufsbezeichnung',
            'onkeydown': 'return event.key != "Enter";'})
    data_berufsbeschreibung = TextAreaField(
        'data_berufsbeschreibung', render_kw={
            'placeholder': 'Vergangene Berufsbeschreibung', 'rows': '2'})
    data_unternehmen = StringField(
        'data_unternehmen',
        render_kw={
            'placeholder': 'Vergangenes Unternehmen',
            'onkeydown': 'return event.key != "Enter";'})
    data_beruf_von = DateField(
        'data_beruf_von',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_beruf_bis = DateField(
        'data_beruf_bis', render_kw={
            'min': date(
                1900, 1, 1), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_berufserfahrung = TextAreaField(
        'data_sonstige_berufserfahrung', render_kw={
            'placeholder': 'Sonstige Angaben zur Berufserfahrung', 'rows': '2'})
    # Projekterfahrung
    data_projekttitel = StringField(
        'data_projekttitel',
        render_kw={
            'placeholder': 'Titel des Projekts',
            'onkeydown': 'return event.key != "Enter";'})
    data_projektrolle = SelectField(
        'data_sprachen_niveau',
        choices=[
            ('Bitte auswählen...',
             'Bitte auswählen...'),
            ('Teammitglied',
             'Teammitglied'),
            ('Leitung',
             'Leitung')],
        render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    data_projektbezeichnung = StringField(
        'data_projektbezeichnung',
        render_kw={
            'placeholder': 'Tätigkeitsbezeichnung',
            'onkeydown': 'return event.key != "Enter";'})
    data_projektbeschreibung = TextAreaField(
        'data_projektbeschreibung', render_kw={
            'placeholder': 'Tätigkeitsbeschreibung', 'rows': '2'})
    data_projekt_von = DateField(
        'data_projekt_von',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_projekt_bis = DateField(
        'data_projekt_bis', render_kw={
            'min': date(
                1900, 1, 1), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_projekterfahrung = TextAreaField(
        'data_sonstige_projekterfahrung', render_kw={
            'placeholder': 'Sonstige Angaben zur Projekterfahrung', 'rows': '2'})
    # Weiterbildungen
    data_weiterbildungsbezeichnung = StringField(
        'data_weiterbildungsbezeichnung',
        render_kw={
            'placeholder': 'Weiterbildung / Training',
            'onkeydown': 'return event.key != "Enter";'})
    data_weiterbildungsbeschreibung = TextAreaField(
        'data_weiterbildungsbeschreibung', render_kw={
            'placeholder': 'Kurzbeschreibung', 'rows': '2'})
    data_weiterbildung_von = DateField(
        'data_weiterbildung_von',
        render_kw={
            'min': date(
                1900,
                1,
                1),
            'max': date.today(),
            'onkeydown': 'return event.key != "Enter";'})
    data_weiterbildung_bis = DateField(
        'data_weiterbildung_bis', render_kw={
            'min': date(
                1900, 1, 1), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_weiterbildung = TextAreaField(
        'data_sonstige_weiterbildung',
        render_kw={
            'placeholder': 'Sonstige Angaben zu abgeschlossenenen Weiterbildungen',
            'rows': '2'})
    # Geplante Weiterbildungen
    data_weiterbildung_thema = StringField(
        'data_weiterbildung_thema',
        render_kw={
            'placeholder': 'Thema',
            'onkeydown': 'return event.key != "Enter";'})
    data_weiterbildung_warum = TextAreaField(
        'data_weiterbildung_warum', render_kw={
            'placeholder': 'Warum wird die Fähigkeit als wichtig erachtet?', 'rows': '2'})
    data_sonstige_geplante = TextAreaField(
        'data_sonstige_geplante', render_kw={
            'placeholder': 'Sonstige Angaben zu geplanten Weiterbildungen', 'rows': '2'})
    # Gesundheit
    gesundheit_atemschutztauglichkeit = BooleanField(
        'gesundheit_atemschutztauglichkeit', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    gesundheit_atemschutztauglichkeit_date = DateField(
        'gesundheit_atemschutztauglichkeit_date', render_kw={
            'min': date.today(), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    gesundheit_kontrollbereichstauglichkeit = BooleanField(
        'gesundheit_kontrollbereichstauglichkeit', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    gesundheit_kontrollbereichstauglichkeit_date = DateField(
        'gesundheit_kontrollbereichstauglichkeit_date', render_kw={
            'min': date.today(), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    gesundheit_schichttauglichkeit = BooleanField(
        'gesundheit_schichttauglichkeit', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    gesundheit_schichttauglichkeit_date = DateField(
        'gesundheit_schichttauglichkeit_date', render_kw={
            'min': date.today(), 'max': date(
                2029, 12, 31), 'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_gesundheit = TextAreaField(
        'data_sonstige_gesundheit', render_kw={
            'placeholder': 'Sonstige Angaben zu Gesundheitsdaten', 'rows': '2'})
    # Interessen
    data_freizeit = StringField(
        'data_freizeit',
        render_kw={
            'placeholder': 'Freizeitaktivität',
            'onkeydown': 'return event.key != "Enter";'})
    data_ehrenamtlich = StringField(
        'data_ehrenamtlich',
        render_kw={
            'placeholder': 'Ehrenamtliche Tätigkeit',
            'onkeydown': 'return event.key != "Enter";'})
    data_nebenjobs = StringField(
        'data_nebenjobs',
        render_kw={
            'placeholder': 'Nebenjob',
            'onkeydown': 'return event.key != "Enter";'})
    data_sonstige_interessen = TextAreaField(
        'data_sonstige_interessen', render_kw={
            'placeholder': 'Sonstige Angaben zu persönlichen Interessen', 'rows': '2'})


class MatchingForm(FlaskForm):
    matching_stellenbezeichnung = StringField(
        'matching_stellenbezeichnung',
        render_kw={
            'placeholder': 'Stellenbezeichnung',
            'onkeydown': 'return event.key != "Enter";'})
    matching_ort = StringField(
        'matching_ort',
        render_kw={
            'placeholder': 'Ort',
            'onkeydown': 'return event.key != "Enter";'})
    matching_fachgebiet = StringField(
        'matching_fachgebiet',
        render_kw={
            'placeholder': 'Fachgebiet',
            'onkeydown': 'return event.key != "Enter";'})
    matching_erfahrung = StringField(
        'matching_erfahrung',
        render_kw={
            'placeholder': 'Erfahrung',
            'onkeydown': 'return event.key != "Enter";'})
    matching_skills = HiddenField(
        'matching_skills', render_kw={
            'onkeydown': 'return event.key != "Enter";'})
    matching_submit = SubmitField('matchingsubmit')


class KompetenzanalyseForm(FlaskForm):
    kompetenzanalyse_input = StringField(
        'kompetenzanalyse_input',
        render_kw={
            'placeholder': 'Skill',
            'onkeydown': 'return event.key != "Enter";'})
    kompetenzanalyse_submit = SubmitField('kompetenzanalysesubmit')
