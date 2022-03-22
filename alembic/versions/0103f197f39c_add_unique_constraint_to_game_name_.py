"""add_unique_constraint_to_game_name_column

Revision ID: 0103f197f39c
Revises: 062938fc39ac
Create Date: 2022-03-08 16:41:27.905011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0103f197f39c'
down_revision = '062938fc39ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'result', ['game_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'result', type_='unique')
    # ### end Alembic commands ###
