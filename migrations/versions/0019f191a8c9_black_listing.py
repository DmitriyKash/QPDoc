"""black listing

Revision ID: 0019f191a8c9
Revises: a6ef41be20ed
Create Date: 2023-11-17 22:51:00.049813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0019f191a8c9'
down_revision: Union[str, None] = 'a6ef41be20ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blacklist_tokens_token'), 'blacklist_tokens', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blacklist_tokens_token'), table_name='blacklist_tokens')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
