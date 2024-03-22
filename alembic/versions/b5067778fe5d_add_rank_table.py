"""add rank table

Revision ID: b5067778fe5d
Revises: ffbe81256709
Create Date: 2024-03-22 18:02:36.565014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5067778fe5d'
down_revision: Union[str, None] = 'ffbe81256709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
