"""add rank table

Revision ID: caf5842aec24
Revises: ecbc91efb852
Create Date: 2024-03-22 13:56:32.716561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'caf5842aec24'
down_revision: Union[str, None] = 'ecbc91efb852'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
