from ..extensions import db
from ..tables import event_characters


class Event(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing primary key
    name = db.Column(db.String(200), nullable=False)
    # event_count = db.Column(db.Integer, unique=True, nullable=False) # Add if needed

    characters_involved = db.relationship(
        "Character",
        secondary=event_characters,
        back_populates="history",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"<Event {self.id}: {self.name}>"
