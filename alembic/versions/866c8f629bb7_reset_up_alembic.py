"""reset up alembic

Revision ID: 866c8f629bb7
Revises: 6329a9b5e547
Create Date: 2024-03-24 07:38:37.385919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '866c8f629bb7'
down_revision: Union[str, None] = '6329a9b5e547'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
