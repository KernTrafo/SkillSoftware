"""empty message

Revision ID: cb6958886c8d
Revises: 
Create Date: 2021-08-19 17:31:49.237664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb6958886c8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recruiter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('passwort', sa.Text(), nullable=True),
    sa.Column('vorname', sa.Text(), nullable=True),
    sa.Column('nachname', sa.Text(), nullable=True),
    sa.Column('abteilung', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recruiter_email'), 'recruiter', ['email'], unique=True)
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('passwort', sa.Text(), nullable=True),
    sa.Column('email_confirmed', sa.Boolean(), nullable=True),
    sa.Column('pseudonym', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pseudonym')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('stellenanzeigen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recruiter_id', sa.Integer(), nullable=True),
    sa.Column('job_title', sa.Text(), nullable=True),
    sa.Column('ort', sa.Text(), nullable=True),
    sa.Column('fachgebiet', sa.Text(), nullable=True),
    sa.Column('erfahrung', sa.Text(), nullable=True),
    sa.Column('skills', sa.Text(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('besetzt', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['recruiter_id'], ['recruiter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_consents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('data_privacy', sa.Boolean(), nullable=True),
    sa.Column('ai_privacy', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('data_bildungsgrad', sa.Text(), nullable=True),
    sa.Column('fachrichtung_elektrotechnik', sa.Boolean(), nullable=True),
    sa.Column('fachrichtung_maschinentechnik', sa.Boolean(), nullable=True),
    sa.Column('fachrichtung_verfahrenstechnik', sa.Boolean(), nullable=True),
    sa.Column('fachrichtung_strahlenschutz', sa.Boolean(), nullable=True),
    sa.Column('fachrichtung_strahlenschutzwerker', sa.Boolean(), nullable=True),
    sa.Column('fachrichtung_strahlenschutzfachkraft', sa.Boolean(), nullable=True),
    sa.Column('andere_fachrichtung', sa.Text(), nullable=True),
    sa.Column('data_vorname', sa.Text(), nullable=True),
    sa.Column('data_nachname', sa.Text(), nullable=True),
    sa.Column('data_geburtsdatum', sa.Text(), nullable=True),
    sa.Column('data_geschlecht', sa.Text(), nullable=True),
    sa.Column('data_familienstand', sa.Text(), nullable=True),
    sa.Column('data_plz', sa.Integer(), nullable=True),
    sa.Column('data_ort', sa.Text(), nullable=True),
    sa.Column('data_reisebereitschaft', sa.Text(), nullable=True),
    sa.Column('data_sonstige_persoenliche', sa.Text(), nullable=True),
    sa.Column('data_studium', sa.Text(), nullable=True),
    sa.Column('data_studium_schwerpunkt', sa.Text(), nullable=True),
    sa.Column('data_studium_von', sa.Text(), nullable=True),
    sa.Column('data_studium_bis', sa.Text(), nullable=True),
    sa.Column('data_ausbildung', sa.Text(), nullable=True),
    sa.Column('data_ausbildung_schwerpunkt', sa.Text(), nullable=True),
    sa.Column('data_ausbildung_von', sa.Text(), nullable=True),
    sa.Column('data_ausbildung_bis', sa.Text(), nullable=True),
    sa.Column('data_kenntnisse', sa.Text(), nullable=True),
    sa.Column('data_kenntnisse_niveau', sa.Text(), nullable=True),
    sa.Column('data_sprachen', sa.Text(), nullable=True),
    sa.Column('data_sprachen_niveau', sa.Text(), nullable=True),
    sa.Column('data_fuehrerschein_AM', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_A1', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_A2', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_A', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_B1', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_B', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_C1', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_C', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_D1', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_D', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_BE', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_C1E', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_CE', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_D1E', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_DE', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_L', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_M', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_S', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_T', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_Staplerschein', sa.Boolean(), nullable=True),
    sa.Column('data_fuehrerschein_Kranschein', sa.Boolean(), nullable=True),
    sa.Column('data_potenzielle_berufe', sa.Text(), nullable=True),
    sa.Column('data_missing_skills', sa.Text(), nullable=True),
    sa.Column('data_sonstige_fachliche', sa.Text(), nullable=True),
    sa.Column('data_aktuelle_berufsbezeichnung', sa.Text(), nullable=True),
    sa.Column('data_aktuelle_berufsbeschreibung', sa.Text(), nullable=True),
    sa.Column('data_taetigkeitsstandort', sa.Text(), nullable=True),
    sa.Column('data_bei_rwe_seit', sa.Text(), nullable=True),
    sa.Column('data_berufsbezeichnung', sa.Text(), nullable=True),
    sa.Column('data_berufsbeschreibung', sa.Text(), nullable=True),
    sa.Column('data_unternehmen', sa.Text(), nullable=True),
    sa.Column('data_beruf_von', sa.Text(), nullable=True),
    sa.Column('data_beruf_bis', sa.Text(), nullable=True),
    sa.Column('data_sonstige_berufserfahrung', sa.Text(), nullable=True),
    sa.Column('data_projekttitel', sa.Text(), nullable=True),
    sa.Column('data_projektrolle', sa.Text(), nullable=True),
    sa.Column('data_projektbezeichnung', sa.Text(), nullable=True),
    sa.Column('data_projektbeschreibung', sa.Text(), nullable=True),
    sa.Column('data_projekt_von', sa.Text(), nullable=True),
    sa.Column('data_projekt_bis', sa.Text(), nullable=True),
    sa.Column('data_sonstige_projekterfahrung', sa.Text(), nullable=True),
    sa.Column('data_weiterbildungsbezeichnung', sa.Text(), nullable=True),
    sa.Column('data_weiterbildungsbeschreibung', sa.Text(), nullable=True),
    sa.Column('data_weiterbildung_von', sa.Text(), nullable=True),
    sa.Column('data_weiterbildung_bis', sa.Text(), nullable=True),
    sa.Column('data_sonstige_weiterbildung', sa.Text(), nullable=True),
    sa.Column('data_weiterbildung_thema', sa.Text(), nullable=True),
    sa.Column('data_weiterbildung_warum', sa.Text(), nullable=True),
    sa.Column('data_sonstige_geplante', sa.Text(), nullable=True),
    sa.Column('gesundheit_atemschutztauglichkeit', sa.Boolean(), nullable=True),
    sa.Column('gesundheit_atemschutztauglichkeit_date', sa.Text(), nullable=True),
    sa.Column('gesundheit_kontrollbereichstauglichkeit', sa.Boolean(), nullable=True),
    sa.Column('gesundheit_kontrollbereichstauglichkeit_date', sa.Text(), nullable=True),
    sa.Column('gesundheit_schichttauglichkeit', sa.Boolean(), nullable=True),
    sa.Column('gesundheit_schichttauglichkeit_date', sa.Text(), nullable=True),
    sa.Column('data_sonstige_gesundheit', sa.Text(), nullable=True),
    sa.Column('data_freizeit', sa.Text(), nullable=True),
    sa.Column('data_ehrenamtlich', sa.Text(), nullable=True),
    sa.Column('data_nebenjobs', sa.Text(), nullable=True),
    sa.Column('data_sonstige_interessen', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_data_timestamp'), 'user_data', ['timestamp'], unique=False)
    op.create_table('user_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('recruiter_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.Text(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('subject', sa.Text(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('link', sa.Text(), nullable=True),
    sa.Column('type', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recruiter_id'], ['recruiter.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_messages_date'), 'user_messages', ['date'], unique=False)
    op.create_table('user_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill_matching',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['stellenanzeigen.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skill_matching')
    op.drop_table('user_skills')
    op.drop_index(op.f('ix_user_messages_date'), table_name='user_messages')
    op.drop_table('user_messages')
    op.drop_index(op.f('ix_user_data_timestamp'), table_name='user_data')
    op.drop_table('user_data')
    op.drop_table('user_consents')
    op.drop_table('stellenanzeigen')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('skills')
    op.drop_index(op.f('ix_recruiter_email'), table_name='recruiter')
    op.drop_table('recruiter')
    # ### end Alembic commands ###
