"""empty message

Revision ID: 47b35e5afff0
Revises: 5f21d19f7c2b
Create Date: 2019-04-03 13:32:38.919900

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '47b35e5afff0'
down_revision = '5f21d19f7c2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cmdb_user', sa.Column('_password', sa.String(length=100), nullable=False))
    op.drop_column('cmdb_user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cmdb_user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('cmdb_user', '_password')
    # ### end Alembic commands ###
