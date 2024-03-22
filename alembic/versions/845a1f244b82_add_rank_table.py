"""add rank table

Revision ID: 845a1f244b82
Revises: caf5842aec24
Create Date: 2024-03-22 13:59:59.266505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '845a1f244b82'
down_revision: Union[str, None] = 'caf5842aec24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
