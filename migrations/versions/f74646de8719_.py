"""empty message

Revision ID: f74646de8719
Revises: 
Create Date: 2023-09-03 08:52:29.966303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_file


# revision identifiers, used by Alembic.
revision: str = 'f74646de8719'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(max_length=1024), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    op.create_table('UsedRefreshToken',
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('Course',
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('cover', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('access_modifier', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['access_modifier'], ['AccessModifier.id'], ),
    sa.ForeignKeyConstraint(['author'], ['User.id'], ),
    sa.ForeignKeyConstraint(['cover'], ['Cover.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Deck',
    sa.Column('course', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('cover', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['course'], ['Course.id'], ),
    sa.ForeignKeyConstraint(['cover'], ['Cover.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Card',
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('ordinal', sa.Integer(), nullable=False),
    sa.Column('attachment', sa.Integer(), nullable=True),
    sa.Column('deck', sa.Integer(), nullable=False),
    sa.Column('last_version', sa.Integer(), nullable=True),
    sa.Column('is_hided', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['attachment'], ['Attachment.id'], ),
    sa.ForeignKeyConstraint(['deck'], ['Deck.id'], ),
    sa.ForeignKeyConstraint(['last_version'], ['Card.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Attachment',
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.Column('file', sqlalchemy_file.types.ImageField(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Cover',
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.Column('file', sqlalchemy_file.types.ImageField(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserIcon',
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.Column('file', sqlalchemy_file.types.ImageField(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserIcon')
    op.drop_table('Cover')
    op.drop_table('Attachment')
    op.drop_table('Card')
    op.drop_table('Deck')
    op.drop_table('Course')
    op.drop_table('UsedRefreshToken')
    op.drop_table('User')
    # ### end Alembic commands ###
