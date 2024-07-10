"""created database

Revision ID: d617445e7f85
Revises: e2b470663693
Create Date: 2024-07-10 12:07:00.471442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd617445e7f85'
down_revision = 'e2b470663693'
branch_labels = None
depends_on = None


def upgrade():
    # Add columns and create foreign keys
    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.add_column(sa.Column('trainingSession_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_coaches_trainingSession_id', 'trainingSessions', ['trainingSession_id'], ['id'])

    with op.batch_alter_table('swimmers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('trainingSession_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_swimmers_trainingSession_id', 'trainingSessions', ['trainingSession_id'], ['id'])

    with op.batch_alter_table('trainingSessions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_trainingSessions_student_id', 'swimmers', ['student_id'], ['id'])


def downgrade():
    # Drop columns and constraints
    with op.batch_alter_table('trainingSessions', schema=None) as batch_op:
        batch_op.drop_constraint('fk_trainingSessions_student_id', type_='foreignkey')
        batch_op.drop_column('student_id')

    with op.batch_alter_table('swimmers', schema=None) as batch_op:
        batch_op.drop_constraint('fk_swimmers_trainingSession_id', type_='foreignkey')
        batch_op.drop_column('trainingSession_id')

    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.drop_constraint('fk_coaches_trainingSession_id', type_='foreignkey')
        batch_op.drop_column('trainingSession_id')
