"""empty message

Revision ID: b6d582f32223
Revises: 344f1697ab7c
Create Date: 2019-05-06 18:03:44.501000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b6d582f32223'
down_revision = '344f1697ab7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userinfos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qq', sa.String(length=16), nullable=True),
    sa.Column('wechart', sa.String(length=16), nullable=True),
    sa.Column('weibo', sa.String(length=16), nullable=True),
    sa.Column('zfb', sa.String(length=16), nullable=True),
    sa.Column('github', sa.String(length=16), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('github'),
    sa.UniqueConstraint('qq'),
    sa.UniqueConstraint('wechart'),
    sa.UniqueConstraint('weibo'),
    sa.UniqueConstraint('zfb')
    )
    op.create_table('article_tag',
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    op.drop_table('plates')
    op.create_foreign_key(None, 'articles', 'categories', ['category_id'], ['id'])
    op.create_foreign_key(None, 'articles', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'articles', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'articles', ['article_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_table('plates',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=16), nullable=False),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('category_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('order_num', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    op.drop_table('article_tag')
    op.drop_table('userinfos')
    # ### end Alembic commands ###