"""empty message

Revision ID: 3840091d609f
Revises: 
Create Date: 2018-02-27 23:56:50.237855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3840091d609f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ctype', 'bugs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ctype', sa.Column('bugs', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
