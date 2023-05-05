# function to get the form data
from flask import request
from flask_login import current_user
from app.models import UserData
from app.forms import DataForm
from datetime import datetime


def data_submit():
    data_form = DataForm(request.form)
    data = UserData(
        user_id=current_user.get_id(),
        # Persönliche Daten
        data_bildungsgrad=data_form.data_bildungsgrad.data,
        fachrichtung_elektrotechnik=data_form.fachrichtung_elektrotechnik.data,
        fachrichtung_maschinentechnik=data_form.fachrichtung_maschinentechnik.data,
        fachrichtung_verfahrenstechnik=data_form.fachrichtung_verfahrenstechnik.data,
        fachrichtung_strahlenschutz=data_form.fachrichtung_strahlenschutz.data,
        fachrichtung_strahlenschutzwerker=data_form.fachrichtung_strahlenschutzwerker.data,
        fachrichtung_strahlenschutzfachkraft=data_form.fachrichtung_strahlenschutzfachkraft.data,
        andere_fachrichtung=data_form.andere_fachrichtung.data,
        data_vorname=data_form.data_vorname.data,
        data_nachname=data_form.data_nachname.data,
        data_geburtsdatum=data_form.data_geburtsdatum.data,
        data_geschlecht=data_form.data_geschlecht.data,
        data_familienstand=data_form.data_familienstand.data,
        data_plz=data_form.data_plz.data,
        data_ort=data_form.data_ort.data,
        data_reisebereitschaft=data_form.data_reisebereitschaft.data,
        data_sonstige_persoenliche=data_form.data_sonstige_persoenliche.data,
        # Fachliche Qualifikation
        data_studium=str(
            [x.lower() for x in request.form.getlist('data_studium') if x != '']),
        data_studium_schwerpunkt=str(
            [x.lower() for x in request.form.getlist('data_studium_schwerpunkt') if x != '']),
        data_studium_von=str(
            [x for x in request.form.getlist('data_studium_von') if x != '']),
        data_studium_bis=str(
            [x for x in request.form.getlist('data_studium_bis') if x != '']),
        data_ausbildung=str(
            [x.lower() for x in request.form.getlist('data_ausbildung') if x != '']),
        data_ausbildung_schwerpunkt=str(
            [x.lower() for x in request.form.getlist('data_ausbildung_schwerpunkt') if x != '']),
        data_ausbildung_von=str(
            [x for x in request.form.getlist('data_ausbildung_von') if x != '']),
        data_ausbildung_bis=str(
            [x for x in request.form.getlist('data_ausbildung_bis') if x != '']),
        data_kenntnisse=str(
            [x.lower() for x in request.form.getlist('data_kenntnisse') if x != '']),
        data_kenntnisse_niveau=str(
            [x for x in request.form.getlist('data_kenntnisse_niveau') if x != '']),
        data_sprachen=str(
            [x.lower() for x in request.form.getlist('data_sprachen') if x != '']),
        data_sprachen_niveau=str(
            [x for x in request.form.getlist('data_sprachen_niveau') if x != '']),
        data_fuehrerschein_AM=data_form.data_fuehrerschein_AM.data,
        data_fuehrerschein_A1=data_form.data_fuehrerschein_A1.data,
        data_fuehrerschein_A2=data_form.data_fuehrerschein_A2.data,
        data_fuehrerschein_A=data_form.data_fuehrerschein_A.data,
        data_fuehrerschein_B1=data_form.data_fuehrerschein_B1.data,
        data_fuehrerschein_B=data_form.data_fuehrerschein_B.data,
        data_fuehrerschein_C1=data_form.data_fuehrerschein_C1.data,
        data_fuehrerschein_C=data_form.data_fuehrerschein_C.data,
        data_fuehrerschein_D1=data_form.data_fuehrerschein_D1.data,
        data_fuehrerschein_D=data_form.data_fuehrerschein_D.data,
        data_fuehrerschein_BE=data_form.data_fuehrerschein_BE.data,
        data_fuehrerschein_C1E=data_form.data_fuehrerschein_C1E.data,
        data_fuehrerschein_CE=data_form.data_fuehrerschein_CE.data,
        data_fuehrerschein_D1E=data_form.data_fuehrerschein_D1E.data,
        data_fuehrerschein_DE=data_form.data_fuehrerschein_DE.data,
        data_fuehrerschein_L=data_form.data_fuehrerschein_L.data,
        data_fuehrerschein_M=data_form.data_fuehrerschein_M.data,
        data_fuehrerschein_S=data_form.data_fuehrerschein_S.data,
        data_fuehrerschein_T=data_form.data_fuehrerschein_T.data,
        data_fuehrerschein_Staplerschein=data_form.data_fuehrerschein_Staplerschein.data,
        data_fuehrerschein_Kranschein=data_form.data_fuehrerschein_Kranschein.data,
        data_potenzielle_berufe=data_form.data_potenzielle_berufe.data,
        data_missing_skills=data_form.data_missing_skills.data,
        data_sonstige_fachliche=data_form.data_sonstige_fachliche.data,
        # Berufserfahrung
        data_aktuelle_berufsbezeichnung=data_form.data_aktuelle_berufsbezeichnung.data.lower(),
        data_aktuelle_berufsbeschreibung=data_form.data_aktuelle_berufsbeschreibung.data.lower(),
        data_taetigkeitsstandort=data_form.data_taetigkeitsstandort.data,
        data_bei_rwe_seit=data_form.data_bei_rwe_seit.data,
        data_berufsbezeichnung=str(
            [x.lower() for x in request.form.getlist('data_berufsbezeichnung') if x != '']),
        data_berufsbeschreibung=str(
            [x.lower() for x in request.form.getlist('data_berufsbeschreibung') if x != '']),
        data_unternehmen=str(
            [x for x in request.form.getlist('data_unternehmen') if x != '']),
        data_beruf_von=str(
            [x for x in request.form.getlist('data_beruf_von') if x != '']),
        data_beruf_bis=str(
            [x for x in request.form.getlist('data_beruf_bis') if x != '']),
        data_sonstige_berufserfahrung=data_form.data_sonstige_berufserfahrung.data,
        # Projekterfahrung
        data_projekttitel=str(
            [x.lower() for x in request.form.getlist('data_projekttitel') if x != '']),
        data_projektrolle=str(
            [x for x in request.form.getlist('data_projektrolle') if x != '']),
        data_projektbezeichnung=str(
            [x.lower() for x in request.form.getlist('data_projektbezeichnung') if x != '']),
        data_projektbeschreibung=str(
            [x.lower() for x in request.form.getlist('data_projektbeschreibung') if x != '']),
        data_projekt_von=str(
            [x for x in request.form.getlist('data_projekt_von') if x != '']),
        data_projekt_bis=str(
            [x for x in request.form.getlist('data_projekt_bis') if x != '']),
        data_sonstige_projekterfahrung=data_form.data_sonstige_projekterfahrung.data,
        # Weiterbildungen
        data_weiterbildungsbezeichnung=str(
            [x.lower() for x in request.form.getlist('data_weiterbildungsbezeichnung') if x != '']),
        data_weiterbildungsbeschreibung=str(
            [x.lower() for x in request.form.getlist('data_weiterbildungsbeschreibung') if x != '']),
        data_weiterbildung_von=str(
            [x for x in request.form.getlist('data_weiterbildung_von') if x != '']),
        data_weiterbildung_bis=str(
            [x for x in request.form.getlist('data_weiterbildung_bis') if x != '']),
        data_sonstige_weiterbildung=data_form.data_sonstige_weiterbildung.data,
        # Geplante Weiterbildungen
        data_weiterbildung_thema=str(
            [x.lower() for x in request.form.getlist('data_weiterbildung_thema') if x != '']),
        data_weiterbildung_warum=str(
            [x.lower() for x in request.form.getlist('data_weiterbildung_warum') if x != '']),
        data_sonstige_geplante=data_form.data_sonstige_geplante.data,
        # Gesundheit
        gesundheit_atemschutztauglichkeit=data_form.gesundheit_atemschutztauglichkeit.data,
        gesundheit_atemschutztauglichkeit_date=request.form.get(
            'gesundheit_atemschutztauglichkeit_date'),
        gesundheit_kontrollbereichstauglichkeit=data_form.gesundheit_kontrollbereichstauglichkeit.data,
        gesundheit_kontrollbereichstauglichkeit_date=request.form.get(
            'gesundheit_kontrollbereichstauglichkeit_date'),
        gesundheit_schichttauglichkeit=data_form.gesundheit_schichttauglichkeit.data,
        gesundheit_schichttauglichkeit_date=request.form.get(
            'gesundheit_schichttauglichkeit_date'),
        data_sonstige_gesundheit=data_form.data_sonstige_gesundheit.data,
        # Interessen
        data_freizeit=str(
            [x.lower() for x in request.form.getlist('data_freizeit') if x != '']),
        data_ehrenamtlich=str(
            [x.lower() for x in request.form.getlist('data_ehrenamtlich') if x != '']),
        data_nebenjobs=str(
            [x.lower() for x in request.form.getlist('data_nebenjobs') if x != '']),
        data_sonstige_interessen=data_form.data_sonstige_interessen.data,
    )
    return data


def pre_populate():
    data_form = DataForm(request.form)
    user_data = UserData.query.filter_by(
        user_id=current_user.get_id()).order_by(
        UserData.timestamp.desc()).first()
    data_form.data_bildungsgrad.data = user_data.data_bildungsgrad
    data_form.fachrichtung_elektrotechnik.data = user_data.fachrichtung_elektrotechnik
    data_form.fachrichtung_maschinentechnik.data = user_data.fachrichtung_maschinentechnik
    data_form.fachrichtung_verfahrenstechnik.data = user_data.fachrichtung_verfahrenstechnik
    data_form.fachrichtung_strahlenschutz.data = user_data.fachrichtung_strahlenschutz
    data_form.fachrichtung_strahlenschutzwerker.data = user_data.fachrichtung_strahlenschutzwerker
    data_form.fachrichtung_strahlenschutzfachkraft.data = user_data.fachrichtung_strahlenschutzfachkraft
    data_form.andere_fachrichtung.data = user_data.andere_fachrichtung
    data_form.data_vorname.data = user_data.data_vorname
    data_form.data_nachname.data = user_data.data_nachname
    try:
        data_form.data_geburtsdatum.data = datetime.strptime(
            user_data.data_geburtsdatum, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_geschlecht.data = user_data.data_geschlecht
    data_form.data_familienstand.data = user_data.data_familienstand
    data_form.data_plz.data = user_data.data_plz
    data_form.data_ort.data = user_data.data_ort
    data_form.data_reisebereitschaft.data = user_data.data_reisebereitschaft
    data_form.data_sonstige_persoenliche.data = user_data.data_sonstige_persoenliche
    # Fachliche Qualifikation
    data_form.data_studium.data = user_data.data_studium
    data_form.data_studium_schwerpunkt.data = user_data.data_studium_schwerpunkt
    try:
        data_form.data_studium_von.data = datetime.strptime(
            user_data.data_studium_von, '%Y-%M')
    except BaseException:
        pass
    try:
        data_form.data_studium_bis.data = datetime.strptime(
            user_data.data_studium_bis, '%Y-%M')
    except BaseException:
        pass
    data_form.data_ausbildung.data = user_data.data_ausbildung
    data_form.data_ausbildung_schwerpunkt.data = user_data.data_ausbildung_schwerpunkt
    try:
        data_form.data_ausbildung_von.data = datetime.strptime(
            user_data.data_ausbildung_von, '%Y-%m-%d')
    except BaseException:
        pass
    try:
        data_form.data_ausbildung_bis.data = datetime.strptime(
            user_data.data_ausbildung_bis, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_kenntnisse.data = user_data.data_kenntnisse
    data_form.data_kenntnisse_niveau.data = user_data.data_kenntnisse_niveau
    data_form.data_sprachen.data = user_data.data_sprachen
    data_form.data_sprachen_niveau.data = user_data.data_sprachen_niveau
    data_form.data_fuehrerschein_AM.data = user_data.data_fuehrerschein_AM
    data_form.data_fuehrerschein_A1.data = user_data.data_fuehrerschein_A1
    data_form.data_fuehrerschein_A2.data = user_data.data_fuehrerschein_A2
    data_form.data_fuehrerschein_A.data = user_data.data_fuehrerschein_A
    data_form.data_fuehrerschein_B1.data = user_data.data_fuehrerschein_B1
    data_form.data_fuehrerschein_B.data = user_data.data_fuehrerschein_B
    data_form.data_fuehrerschein_C1.data = user_data.data_fuehrerschein_C1
    data_form.data_fuehrerschein_C.data = user_data.data_fuehrerschein_C
    data_form.data_fuehrerschein_D1.data = user_data.data_fuehrerschein_D1
    data_form.data_fuehrerschein_D.data = user_data.data_fuehrerschein_D
    data_form.data_fuehrerschein_BE.data = user_data.data_fuehrerschein_BE
    data_form.data_fuehrerschein_C1E.data = user_data.data_fuehrerschein_C1E
    data_form.data_fuehrerschein_CE.data = user_data.data_fuehrerschein_CE
    data_form.data_fuehrerschein_D1E.data = user_data.data_fuehrerschein_D1E
    data_form.data_fuehrerschein_DE.data = user_data.data_fuehrerschein_DE
    data_form.data_fuehrerschein_L.data = user_data.data_fuehrerschein_L
    data_form.data_fuehrerschein_M.data = user_data.data_fuehrerschein_M
    data_form.data_fuehrerschein_S.data = user_data.data_fuehrerschein_S
    data_form.data_fuehrerschein_T.data = user_data.data_fuehrerschein_T
    data_form.data_fuehrerschein_Staplerschein.data = user_data.data_fuehrerschein_Staplerschein
    data_form.data_fuehrerschein_Kranschein.data = user_data.data_fuehrerschein_Kranschein
    data_form.data_potenzielle_berufe.data = user_data.data_potenzielle_berufe
    data_form.data_missing_skills.data = user_data.data_missing_skills
    data_form.data_sonstige_fachliche.data = user_data.data_sonstige_fachliche
    # Berufserfahrung
    data_form.data_aktuelle_berufsbezeichnung.data = user_data.data_aktuelle_berufsbezeichnung
    data_form.data_aktuelle_berufsbeschreibung.data = user_data.data_aktuelle_berufsbeschreibung
    data_form.data_taetigkeitsstandort.data = user_data.data_taetigkeitsstandort
    try:
        data_form.data_bei_rwe_seit.data = datetime.strptime(
            user_data.data_bei_rwe_seit, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_berufsbezeichnung.data = user_data.data_berufsbezeichnung
    data_form.data_berufsbeschreibung.data = user_data.data_berufsbeschreibung
    data_form.data_unternehmen.data = user_data.data_unternehmen
    try:
        data_form.data_beruf_von.data = datetime.strptime(
            user_data.data_beruf_von, '%Y-%m-%d')
    except BaseException:
        pass
    try:
        data_form.data_beruf_bis.data = datetime.strptime(
            user_data.data_beruf_bis, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_sonstige_berufserfahrung.data = user_data.data_sonstige_berufserfahrung
    # Projekterfahrung
    data_form.data_projekttitel.data = user_data.data_projekttitel
    data_form.data_projektrolle.data = user_data.data_projektrolle
    data_form.data_projektbezeichnung.data = user_data.data_projektbezeichnung
    data_form.data_projektbeschreibung.data = user_data.data_projektbeschreibung
    try:
        data_form.data_projekt_von.data = datetime.strptime(
            user_data.data_projekt_von, '%Y-%m-%d')
    except BaseException:
        pass
    try:
        data_form.data_projekt_bis.data = datetime.strptime(
            user_data.data_projekt_bis, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_sonstige_projekterfahrung.data = user_data.data_sonstige_projekterfahrung
    # Weiterbildungen
    data_form.data_weiterbildungsbezeichnung.data = user_data.data_weiterbildungsbezeichnung
    data_form.data_weiterbildungsbeschreibung.data = user_data.data_weiterbildungsbeschreibung
    try:
        data_form.data_weiterbildung_von.data = datetime.strptime(
            user_data.data_weiterbildung_von, '%Y-%m-%d')
    except BaseException:
        pass
    try:
        data_form.data_weiterbildung_bis.data = datetime.strptime(
            user_data.data_weiterbildung_bis, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_sonstige_weiterbildung.data = user_data.data_sonstige_weiterbildung
    # Geplante Weiterbildungen
    data_form.data_weiterbildung_thema.data = user_data.data_weiterbildung_thema
    data_form.data_weiterbildung_warum.data = user_data.data_weiterbildung_warum
    data_form.data_sonstige_geplante.data = user_data.data_sonstige_geplante
    # Gesundheit
    data_form.gesundheit_atemschutztauglichkeit.data = user_data.gesundheit_atemschutztauglichkeit
    try:
        data_form.gesundheit_atemschutztauglichkeit_date.data = datetime.strptime(
            str(user_data.gesundheit_atemschutztauglichkeit_date), '%Y-%m-%d')
    except BaseException:
        pass
    data_form.gesundheit_kontrollbereichstauglichkeit.data = user_data.gesundheit_kontrollbereichstauglichkeit
    try:
        data_form.gesundheit_kontrollbereichstauglichkeit_date.data = datetime.strptime(
            user_data.gesundheit_kontrollbereichstauglichkeit_date, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.gesundheit_schichttauglichkeit.data = user_data.gesundheit_schichttauglichkeit
    try:
        data_form.gesundheit_schichttauglichkeit_date.data = datetime.strptime(
            user_data.gesundheit_schichttauglichkeit_date, '%Y-%m-%d')
    except BaseException:
        pass
    data_form.data_sonstige_gesundheit.data = user_data.data_sonstige_gesundheit
    # Interessen
    data_form.data_freizeit.data = user_data.data_freizeit
    data_form.data_ehrenamtlich.data = user_data.data_ehrenamtlich
    data_form.data_nebenjobs.data = user_data.data_nebenjobs
    data_form.data_sonstige_interessen.data = user_data.data_sonstige_interessen
    return data_form
