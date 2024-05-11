"""Add created_at

Revision ID: cf5540f43bf0
Revises: fd6b09e0e299
Create Date: 2024-03-12 18:30:48.345410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cf5540f43bf0"
down_revision = "fd6b09e0e299"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("participant", schema=None) as batch_op:
        batch_op.add_column(sa.Column("created_at", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("participant", schema=None) as batch_op:
        batch_op.drop_column("created_at")

    # ### end Alembic commands ###
