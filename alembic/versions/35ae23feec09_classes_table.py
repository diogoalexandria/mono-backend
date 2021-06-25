"""Classes table

Revision ID: 35ae23feec09
Revises: d6e351d1dc58
Create Date: 2021-06-22 23:27:24.841774

"""
from sqlalchemy.dialects.postgresql.base import UUID
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ae23feec09'
down_revision = 'd6e351d1dc58'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'classes',
        sa.Column('id',           UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('name',         sa.String           , nullable=False),
        sa.Column('subject_id',   UUID(as_uuid=True)  , sa.ForeignKey('subjects.id'), nullable=True),
        sa.Column('professor_id', UUID(as_uuid=True)  , sa.ForeignKey('users.id'), nullable=True),
        sa.Column('status',       sa.String           , nullable=False),
        sa.Column('created_at',   sa.DateTime         , nullable=False),
        sa.Column('updated_at',   sa.DateTime         , nullable=True)
    )


def downgrade():
    op.drop_table('classes')
