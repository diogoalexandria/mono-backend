"""Subscriptions table

Revision ID: 9cee7aa27382
Revises: 35ae23feec09
Create Date: 2021-06-22 23:36:23.339899

"""
from sqlalchemy.dialects.postgresql.base import UUID
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cee7aa27382'
down_revision = '35ae23feec09'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subscriptions',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('sub_date',   sa.DateTime         , nullable=False),
        sa.Column('student_id', UUID(as_uuid=True)  , sa.ForeignKey('users.id'), nullable=True),
        sa.Column('class_id',   UUID(as_uuid=True)  , sa.ForeignKey('classes.id'), nullable=True),
        sa.Column('status',     sa.String           , nullable=False),
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )


def downgrade():
    op.drop_table('subscriptions')
