"""empty message

Revision ID: 1_initial
Revises: 
Create Date: 2019-01-13 15:05:56.578821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gallery_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('master', sa.Boolean(), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gallery_user')
    # ### end Alembic commands ###
