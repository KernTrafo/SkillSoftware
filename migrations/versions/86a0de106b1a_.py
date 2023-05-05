"""empty message

Revision ID: 86a0de106b1a
Revises: cb6958886c8d
Create Date: 2021-09-29 12:07:48.630104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86a0de106b1a'
down_revision = 'cb6958886c8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'skills', ['skill'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'skills', type_='unique')
    # ### end Alembic commands ###