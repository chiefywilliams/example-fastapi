"""add rank table

Revision ID: d6b37a0c7e14
Revises: 845a1f244b82
Create Date: 2024-03-22 14:02:49.052533

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6b37a0c7e14'
down_revision: Union[str, None] = '845a1f244b82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
