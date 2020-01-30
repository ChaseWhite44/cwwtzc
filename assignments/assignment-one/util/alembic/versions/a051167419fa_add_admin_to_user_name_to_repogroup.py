"""Add admin to User, name to RepoGroup

Revision ID: a051167419fa
Revises: 2eaa930b1f5a
Create Date: 2019-02-17 13:09:42.138936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a051167419fa'
down_revision = '2eaa930b1f5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('repo_group', sa.Column('name', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('administrator', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'administrator')
    op.drop_column('repo_group', 'name')
    # ### end Alembic commands ###
