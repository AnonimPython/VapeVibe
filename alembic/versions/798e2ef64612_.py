"""empty message

Revision ID: 798e2ef64612
Revises: fcba953c7245
Create Date: 2025-04-02 00:27:27.836212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '798e2ef64612'
down_revision: Union[str, None] = 'fcba953c7245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_index('ix_product_name')
        batch_op.drop_column('nicotine')
        batch_op.drop_column('battery')
        batch_op.drop_column('device_type')
        batch_op.drop_column('flavor')
        batch_op.drop_column('is_active')
        batch_op.drop_column('capacity')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('capacity', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('flavor', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('device_type', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('battery', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('nicotine', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
        batch_op.create_index('ix_product_name', ['name'], unique=False)

    # ### end Alembic commands ###
