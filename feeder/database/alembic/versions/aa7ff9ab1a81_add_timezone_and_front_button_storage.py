"""Add timezone and front button storage

Revision ID: aa7ff9ab1a81
Revises: ffdfb147fffc
Create Date: 2020-11-06 16:05:12.970832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "aa7ff9ab1a81"
down_revision = "ffdfb147fffc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    connection = op.get_bind()
    connection.execute("pragma foreign_keys=OFF")
    with op.batch_alter_table("kronos_device", schema=None) as batch_op:
        batch_op.add_column(sa.Column("frontButton", sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column("timezone", sa.Text(), nullable=True))
    connection.execute("pragma foreign_keys=ON")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    connection = op.get_bind()
    connection.execute("pragma foreign_keys=OFF")
    with op.batch_alter_table("kronos_device", schema=None) as batch_op:
        batch_op.drop_column("timezone")
        batch_op.drop_column("frontButton")
    connection.execute("pragma foreign_keys=ON")
    # ### end Alembic commands ###