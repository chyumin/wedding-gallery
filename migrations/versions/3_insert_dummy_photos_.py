"""empty message

Revision ID: 2_photos_table
Revises: 1_initial
Create Date: 2019-01-13 15:36:17.329234

"""
from alembic import op
import sqlalchemy as sa

from wedding_gallery.models import DBSession, core

# revision identifiers, used by Alembic.
revision = '3_insert_dummy_photos'
down_revision = '2_photos_table'
branch_labels = None
depends_on = None


def upgrade():
    first_user = core.GalleryUser.query.first()
    links = [
        'https://sba.ubc.ca/sites/sba.ubc.ca/files/weddingplanningbouquetshoes_0.jpg',
        'http://www.motelacqua.com.br/blog/wp-content/uploads/2015/09/Wedding-Photo-750x410.jpg',
        'https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBPSWzK.img?h=416&w=624&m=6&q=60&o=f&l=f',
        'https://images.megapixl.com/6325/63256194.jpg',
        'https://www.loromedia.com/wp-content/uploads/2013/10/happy-friends-on-beach.jpg'
    ]
    for link in links:
        photo = core.Photo(link=link, user_id=first_user.id)
        DBSession.add(photo)

    approved_photos = [
        'https://amp.thisisinsider.com/images/5b9eb0ef3cccd11d008b4576-750-500.jpg',
        'http://thelocalchurchintoronto.org/wp-content/uploads/2018/04/wedding-invite.jpg',
    ]

    for link in approved_photos:
        photo = core.Photo(link=link, user_id=first_user.id, approved=True)
        DBSession.add(photo)
    DBSession.commit()


def downgrade():
    op.drop_table('photo')
    op.create_table('photo',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('link', sa.String(), nullable=False),
                    sa.Column('approved', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['gallery_user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_photo_timestamp'), 'photo', ['timestamp'], unique=False)
