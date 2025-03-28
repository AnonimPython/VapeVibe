"""empty message

Revision ID: 379bc30feb30
Revises: 14faf705d8a9
Create Date: 2025-03-28 23:12:55.275665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '379bc30feb30'
down_revision: Union[str, None] = '14faf705d8a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.Uuid(), nullable=True))
        batch_op.create_foreign_key(None, 'product', ['product_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('product_id')

    # ### end Alembic commands ###
