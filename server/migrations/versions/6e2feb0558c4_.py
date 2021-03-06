"""empty message

Revision ID: 6e2feb0558c4
Revises: bfbab5d0edbe
Create Date: 2019-07-25 15:06:52.644000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e2feb0558c4'
down_revision = 'bfbab5d0edbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'article_tag', 'articles', ['article_id'], ['id'])
    op.create_foreign_key(None, 'article_tag', 'tags', ['tag_id'], ['id'])
    op.add_column('articles', sa.Column('edit_content', sa.Text(), nullable=True))
    op.create_foreign_key(None, 'articles', 'categories', ['category_id'], ['id'])
    op.create_foreign_key(None, 'articles', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'comments', ['refer_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'articles', ['article_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'userinfos', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'userinfos', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_column('articles', 'edit_content')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    op.drop_constraint(None, 'article_tag', type_='foreignkey')
    # ### end Alembic commands ###
