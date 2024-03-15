"""Add content column to posts table

Revision ID: 557df485004a
Revises: a96c9d99da95
Create Date: 2024-03-13 17:25:24.785496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '557df485004a'
down_revision: Union[str, None] = 'a96c9d99da95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))

    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass