"""add rank table

Revision ID: 98ca983a135d
Revises: b5067778fe5d
Create Date: 2024-03-22 18:03:54.710397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98ca983a135d'
down_revision: Union[str, None] = 'b5067778fe5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
