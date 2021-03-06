"""empty message

Revision ID: 4cd5366ebdad
Revises: ae4fe43054dd
Create Date: 2020-08-01 23:16:13.549619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cd5366ebdad'
down_revision = 'ae4fe43054dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("INSERT INTO todo_lists (name) VALUES ('Uncategorized');")
    op.execute('UPDATE todos SET list_id=1 WHERE list_id IS NULL;')
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
