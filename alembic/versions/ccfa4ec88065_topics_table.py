"""Topics table

Revision ID: ccfa4ec88065
Revises: 9cee7aa27382
Create Date: 2021-06-22 23:53:41.431090

"""
from sqlalchemy.dialects.postgresql.base import UUID
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccfa4ec88065'
down_revision = '9cee7aa27382'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'topics',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('topic_date', sa.DateTime         , nullable=False),        
        sa.Column('class_id',   UUID(as_uuid=True)  , sa.ForeignKey('classes.id'), nullable=True),
        sa.Column('status',     sa.String           , nullable=False),
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )


def downgrade():
    op.drop_table('topics')
