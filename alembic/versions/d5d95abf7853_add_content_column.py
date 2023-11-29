"""add content column

Revision ID: d5d95abf7853
Revises: 9d302f1ce970
Create Date: 2023-11-28 18:13:57.398146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5d95abf7853'
down_revision: Union[str, None] = '9d302f1ce970'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
