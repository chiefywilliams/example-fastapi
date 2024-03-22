"""add rank table

Revision ID: ecbc91efb852
Revises: b41fb89016b3
Create Date: 2024-03-22 13:50:41.848955

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecbc91efb852'
down_revision: Union[str, None] = 'b41fb89016b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
