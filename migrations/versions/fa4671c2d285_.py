"""empty message

Revision ID: fa4671c2d285
Revises: 5b4e1146fb1c
Create Date: 2020-08-17 13:51:46.755761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa4671c2d285'
down_revision = '5b4e1146fb1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('outline', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'outline')
    # ### end Alembic commands ###
