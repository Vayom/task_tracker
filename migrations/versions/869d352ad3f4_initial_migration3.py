"""Initial migration3

Revision ID: 869d352ad3f4
Revises: 2fbe332823f0
Create Date: 2024-04-24 01:21:43.645918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '869d352ad3f4'
down_revision: Union[str, None] = '2fbe332823f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
