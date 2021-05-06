"""init

Revision ID: 4fda0239475a
Revises: 
Create Date: 2021-05-02 20:41:59.824011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fda0239475a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id',         sa.Integer  , nullable=False, index=True, primary_key=True),
        sa.Column('email',      sa.String   , nullable=False, index=True, unique=True),
        sa.Column('username',   sa.String   , nullable=False, index=True, unique=True),
        sa.Column('password',   sa.String   , nullable=False),
        sa.Column('first_name', sa.String   , nullable=False),
        sa.Column('last_name',  sa.String   , nullable=False),
        sa.Column('entity',     sa.String   , nullable=False),
        sa.Column('gender',     sa.String   , nullable=True),
        sa.Column('status',     sa.String   , nullable=False),
        sa.Column('created_at', sa.DateTime , nullable=False),
        sa.Column('updated_at', sa.DateTime , nullable=True)
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
