"""add rank table

Revision ID: 2ca55d736ac8
Revises: d6b37a0c7e14
Create Date: 2024-03-22 14:03:29.659156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ca55d736ac8'
down_revision: Union[str, None] = 'd6b37a0c7e14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
