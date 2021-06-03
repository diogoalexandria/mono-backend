"""Users Table

Revision ID: 57ac57a261a9
Revises: 4fda0239475a
Create Date: 2021-06-02 19:39:25.985600

"""
from sqlalchemy.dialects.postgresql.base import UUID
from src.models.courses_model import CoursesModel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57ac57a261a9'
down_revision = '4fda0239475a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id',         UUID(as_uuid=True)  , nullable=False, index=True, primary_key=True),
        sa.Column('email',      sa.String           , nullable=False, index=True, unique=True),
        sa.Column('username',   sa.String           , nullable=False, index=True, unique=True),
        sa.Column('password',   sa.String           , nullable=False),
        sa.Column('first_name', sa.String           , nullable=False),
        sa.Column('last_name',  sa.String           , nullable=False),
        sa.Column('entity',     sa.String           , nullable=False),
        sa.Column('gender',     sa.String           , nullable=True),
        sa.Column('status',     sa.String           , nullable=False),
        sa.Column('course_id',  UUID(as_uuid=True)  , sa.ForeignKey('courses.id'), nullable=True),
        sa.Column('created_at', sa.DateTime         , nullable=False),
        sa.Column('updated_at', sa.DateTime         , nullable=True)
    )

def downgrade():
    op.drop_table('users')
