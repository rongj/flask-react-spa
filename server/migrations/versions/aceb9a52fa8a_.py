"""empty message

Revision ID: aceb9a52fa8a
Revises: 6e2feb0558c4
Create Date: 2019-07-30 18:34:19.212000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aceb9a52fa8a'
down_revision = '6e2feb0558c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'article_tag', 'tags', ['tag_id'], ['id'])
    op.create_foreign_key(None, 'article_tag', 'articles', ['article_id'], ['id'])
    op.create_foreign_key(None, 'articles', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'articles', 'categories', ['category_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'comments', ['refer_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'articles', ['article_id'], ['id'])
    op.create_foreign_key(None, 'userinfos', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('token', sa.String(length=300), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token')
    op.drop_constraint(None, 'userinfos', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    # ### end Alembic commands ###
