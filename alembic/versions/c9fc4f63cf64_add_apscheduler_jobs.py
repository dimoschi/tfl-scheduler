"""Add apscheduler jobs table

Revision ID: c9fc4f63cf64
Revises:
Create Date: 2022-03-22 23:51:21.897818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c9fc4f63cf64"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "apscheduler_jobs",
        sa.Column("id", sa.String(191), nullable=False),
        sa.Column(
            "next_run_time", sa.dialects.postgresql.DOUBLE_PRECISION(), nullable=True
        ),
        sa.Column("job_state", sa.dialects.postgresql.BYTEA(), nullable=False),
        sa.PrimaryKeyConstraint("id", name="apscheduler_jobs_pkey"),
    )
    op.create_index(
        op.f("ix_apscheduler_jobs_next_run_time"),
        "apscheduler_jobs",
        ["next_run_time"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_apscheduler_jobs_next_run_time"), table_name="apscheduler_jobs"
    )
    op.drop_table("apscheduler_jobs")
    # ### end Alembic commands ###