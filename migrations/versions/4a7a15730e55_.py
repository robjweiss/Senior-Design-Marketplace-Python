"""empty message

Revision ID: 4a7a15730e55
Revises: 2c1e87af63e1
Create Date: 2018-10-18 13:29:26.836743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7a15730e55'
down_revision = '2c1e87af63e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proposals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('desc', sa.String(length=5000), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('sponsors', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proposals_author'), 'proposals', ['author'], unique=False)
    op.create_index(op.f('ix_proposals_date'), 'proposals', ['date'], unique=False)
    op.create_index(op.f('ix_proposals_title'), 'proposals', ['title'], unique=True)
    op.create_index(op.f('ix_proposals_views'), 'proposals', ['views'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proposals_views'), table_name='proposals')
    op.drop_index(op.f('ix_proposals_title'), table_name='proposals')
    op.drop_index(op.f('ix_proposals_date'), table_name='proposals')
    op.drop_index(op.f('ix_proposals_author'), table_name='proposals')
    op.drop_table('proposals')
    # ### end Alembic commands ###
