"""Registries table

Revision ID: d6e351d1dc58
Revises: 92c012d55e0e
Create Date: 2021-06-22 23:21:26.683119

"""
from sqlalchemy.dialects.postgresql.base import UUID
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6e351d1dc58'
down_revision = '92c012d55e0e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'registries',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('course_id',  UUID(as_uuid=True)  , sa.ForeignKey('courses.id'), nullable=True),
        sa.Column('subject_id', UUID(as_uuid=True)  , sa.ForeignKey('subjects.id'), nullable=True),
        sa.Column('status',     sa.String           , nullable=False),
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )

def downgrade():
    op.drop_table('registries')    
