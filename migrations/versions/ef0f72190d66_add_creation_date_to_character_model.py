"""Add creation_date to Character model

Revision ID: ef0f72190d66
Revises: 58addbb015ee
Create Date: 2025-05-03 17:58:49.859459

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ef0f72190d66"
down_revision = "58addbb015ee"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # Column already exists due to previous failed attempt, so skip adding it.
    # with op.batch_alter_table('character', schema=None) as batch_op:
    #     # Add the column as nullable initially
    #     batch_op.add_column(sa.Column('creation_date', sa.DateTime(), nullable=True))
    #     # Removed the non-nullable constraint from the initial add_column

    # Update existing rows with a default value (using CURRENT_TIMESTAMP for compatibility)
    # This is still needed as the previous attempt failed before setting NOT NULL
    op.execute(
        "UPDATE character SET creation_date = CURRENT_TIMESTAMP WHERE creation_date IS NULL"
    )

    # Now, alter the column to be non-nullable
    with op.batch_alter_table("character", schema=None) as batch_op:
        batch_op.alter_column(
            "creation_date", existing_type=sa.DateTime(), nullable=False
        )

        batch_op.alter_column(
            "id", existing_type=sa.NUMERIC(), type_=sa.UUID(), existing_nullable=False
        )
        batch_op.alter_column(
            "mother_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "father_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=True,
        )

    with op.batch_alter_table("character_siblings", schema=None) as batch_op:
        batch_op.alter_column(
            "character_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "sibling_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=False,
        )

    with op.batch_alter_table("event_characters", schema=None) as batch_op:
        batch_op.alter_column(
            "character_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=False,
        )

    with op.batch_alter_table("relationship", schema=None) as batch_op:
        batch_op.alter_column(
            "character1_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "character2_id",
            existing_type=sa.NUMERIC(),
            type_=sa.UUID(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "type",
            existing_type=sa.VARCHAR(length=12),
            type_=sa.Enum(
                "PARENT",
                "CHILD",
                "SIBLING",
                "SPOUSE",
                "PARTNER",
                "FRIEND",
                "CLOSE_FRIEND",
                "ACQUAINTANCE",
                "ROMANTIC_INTEREST",
                "COLLEAGUE",
                "MENTOR",
                "MENTEE",
                "RIVAL",
                "ENEMY",
                "GUARDIAN",
                "WARD",
                name="relationshiptype",
            ),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("relationship", schema=None) as batch_op:
        batch_op.alter_column(
            "type",
            existing_type=sa.Enum(
                "PARENT",
                "CHILD",
                "SIBLING",
                "SPOUSE",
                "PARTNER",
                "FRIEND",
                "CLOSE_FRIEND",
                "ACQUAINTANCE",
                "ROMANTIC_INTEREST",
                "COLLEAGUE",
                "MENTOR",
                "MENTEE",
                "RIVAL",
                "ENEMY",
                "GUARDIAN",
                "WARD",
                name="relationshiptype",
            ),
            type_=sa.VARCHAR(length=12),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "character2_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "character1_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=False,
        )

    with op.batch_alter_table("event_characters", schema=None) as batch_op:
        batch_op.alter_column(
            "character_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=False,
        )

    with op.batch_alter_table("character_siblings", schema=None) as batch_op:
        batch_op.alter_column(
            "sibling_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "character_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=False,
        )

    with op.batch_alter_table("character", schema=None) as batch_op:
        batch_op.drop_column("creation_date")
        batch_op.alter_column(
            "father_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "mother_id",
            existing_type=sa.UUID(),
            type_=sa.NUMERIC(),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "id", existing_type=sa.UUID(), type_=sa.NUMERIC(), existing_nullable=False
        )

    # ### end Alembic commands ###
