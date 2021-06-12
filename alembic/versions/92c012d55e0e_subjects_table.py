"""Subjects table

Revision ID: 92c012d55e0e
Revises: 57ac57a261a9
Create Date: 2021-06-03 11:48:43.806556

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '92c012d55e0e'
down_revision = '57ac57a261a9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subjects',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('name',       sa.String           , nullable=False, index=True, unique=True),
        sa.Column('status',     sa.String           , nullable=False),       
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )

def downgrade():
    op.drop_table('subjects')
