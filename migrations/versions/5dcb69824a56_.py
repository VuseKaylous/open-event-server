"""empty message

Revision ID: 5dcb69824a56
Revises: c79e6d36a194
Create Date: 2017-06-16 14:35:52.300308

"""

# revision identifiers, used by Alembic.
revision = '5dcb69824a56'
down_revision = 'c79e6d36a194'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'background_url', new_column_name='original_image_url')
    op.alter_column('events', 'logo', new_column_name='logo_url')
    op.alter_column('events', 'large', new_column_name='large_image_url')
    op.alter_column('events', 'thumbnail', new_column_name='thumbnail_image_url')
    op.alter_column('events', 'icon', new_column_name='icon_image_url')

    op.alter_column('events_version', 'background_url', new_column_name='original_image_url')
    op.alter_column('events_version', 'logo', new_column_name='logo_url')
    op.alter_column('events_version', 'large', new_column_name='large_image_url')
    op.alter_column('events_version', 'thumbnail', new_column_name='thumbnail_image_url')
    op.alter_column('events_version', 'icon', new_column_name='icon_image_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.alter_column('events', 'original_image_url', new_column_name='background_url')
    op.alter_column('events', 'logo_url', new_column_name='logo')
    op.alter_column('events', 'large_image_url', new_column_name='large')
    op.alter_column('events', 'thumbnail_image_url', new_column_name='thumbnail')
    op.alter_column('events', 'icon_image_url', new_column_name='icon')

    op.alter_column('events_version', 'original_image_url', new_column_name='background_url')
    op.alter_column('events_version', 'logo_url', new_column_name='logo')
    op.alter_column('events_version', 'large_image_url', new_column_name='large')
    op.alter_column('events_version', 'thumbnail_image_url', new_column_name='thumbnail')
    op.alter_column('events_version', 'icon_image_url', new_column_name='icon')
    # ### end Alembic commands ###