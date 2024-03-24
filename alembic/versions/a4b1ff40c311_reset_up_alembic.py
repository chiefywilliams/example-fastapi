"""reset up alembic

Revision ID: a4b1ff40c311
Revises: dc1deb997d15
Create Date: 2024-03-24 11:22:06.891714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4b1ff40c311'
down_revision: Union[str, None] = 'dc1deb997d15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
