"""Attendances table

Revision ID: 7982287b85e8
Revises: ccfa4ec88065
Create Date: 2021-06-23 00:02:39.135065

"""
from sqlalchemy.dialects.postgresql.base import UUID
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7982287b85e8'
down_revision = 'ccfa4ec88065'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'attendances',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('course_id',  UUID(as_uuid=True)  , sa.ForeignKey('courses.id'), nullable=True),
        sa.Column('subject_id', UUID(as_uuid=True)  , sa.ForeignKey('subjects.id'), nullable=True),
        sa.Column('status',     sa.String           , nullable=False),
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )

def downgrade():
    op.drop_table('attendances')
