from ..extensions import db
from enums import (
    RelationshipStatus,
    RelationshipType,
)
from sqlalchemy import CheckConstraint


class Relationship(db.Model):
    __tablename__ = "relationship"

    id = db.Column(db.Integer, primary_key=True)
    character1_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    character2_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    relationship_type = db.Column("type", db.Enum(RelationshipType), nullable=False)
    status = db.Column(db.Enum(RelationshipStatus), nullable=False)
    start_date = db.Column(db.Date, nullable=True)

    character1 = db.relationship(
        "Character", foreign_keys=[character1_id], back_populates="relationships"
    )
    # Define relationship to character2 if needed for querying from Relationship side
    character2 = db.relationship(
        "Character",
        foreign_keys=[character2_id],
        back_populates="related_to",
    )

    # Ensure character1 and character2 are not the same
    __table_args__ = (
        CheckConstraint(
            "character1_id != character2_id", name="ck_relationship_not_self"
        ),
        # Optional: Unique constraint for a pair in one direction
        # db.UniqueConstraint('character1_id', 'character2_id', 'relationship_type', name='uq_relationship_pair_type')
    )

    def __repr__(self):
        return f"<Relationship {self.character1_id} -> {self.character2_id} ({self.relationship_type.value}, {self.status.value})>"
