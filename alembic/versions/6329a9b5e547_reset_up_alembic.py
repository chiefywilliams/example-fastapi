"""reset up alembic

Revision ID: 6329a9b5e547
Revises: e96d38554f16
Create Date: 2024-03-23 22:47:36.076603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6329a9b5e547'
down_revision: Union[str, None] = 'e96d38554f16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
