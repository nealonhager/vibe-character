from .extensions import db

character_siblings = db.Table(
    "character_siblings",
    db.Column(
        "character_id",
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id"),
        primary_key=True,
    ),
    db.Column(
        "sibling_id",
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id"),
        primary_key=True,
    ),
)

event_characters = db.Table(
    "event_characters",
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
    db.Column(
        "character_id",
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id"),
        primary_key=True,
    ),
)
