"""empty message

Revision ID: 8335e65184fa
Revises: 
Create Date: 2023-10-02 10:19:44.248930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8335e65184fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('address', sa.String(length=564), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('personal_phone', sa.String(length=20), nullable=True),
    sa.Column('personal_celphone', sa.String(length=20), nullable=True),
    sa.Column('contact_group_id', sa.Integer(), nullable=False),
    sa.Column('gender_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contact_group_id'], ['contact_group.id'], ),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    op.drop_table('gender')
    op.drop_table('contact_group')
    # ### end Alembic commands ###
