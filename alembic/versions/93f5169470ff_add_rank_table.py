"""add rank table

Revision ID: 93f5169470ff
Revises: 98ca983a135d
Create Date: 2024-03-22 18:13:01.130390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93f5169470ff'
down_revision: Union[str, None] = '98ca983a135d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
