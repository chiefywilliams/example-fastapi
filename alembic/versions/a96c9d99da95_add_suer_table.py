"""add suer table

Revision ID: a96c9d99da95
Revises: 0f96a28a8816
Create Date: 2024-03-13 17:23:56.605995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a96c9d99da95'
down_revision: Union[str, None] = '0f96a28a8816'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(), nullable = False),
                    sa.Column('email',sa.String(), nullable = False),
                    sa.Column('password',sa.String(), nullable = False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass