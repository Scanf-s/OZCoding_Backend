"""empty message

Revision ID: 51f5c927dbbc
Revises: be5e349d24f1
Create Date: 2024-05-07 02:41:58.730946

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '51f5c927dbbc'
down_revision = 'be5e349d24f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=60), nullable=True))
        batch_op.drop_column('password')
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', mysql.VARCHAR(length=120), nullable=True))
        batch_op.add_column(sa.Column('password', mysql.VARCHAR(length=60), nullable=True))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
