"""init

Revision ID: 4fda0239475a
Revises: 
Create Date: 2021-05-02 20:41:59.824011

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '4fda0239475a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'courses',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('name',       sa.String           , nullable=False, index=True, unique=True),
        sa.Column('status',     sa.String           , nullable=False),       
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )

def downgrade():
    op.drop_table('courses')
    