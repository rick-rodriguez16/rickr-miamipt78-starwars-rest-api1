from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

# many-to-many relationship between User and Person
# UserPerson = Table('user_person_favorites',
#                     db.metadata,
#                     Column('user_id', ForeignKey('user.id'), primary_key=True, nullable=False),
#                     Column('person_id', ForeignKey('person.id'), primary_key=True, nullable=False),
#                     )


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # relationships
    user_person: Mapped[list['Favorite_Character']] = relationship(back_populates='user')

    def __repr__(self):
        return f'<User "{self.username}">'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }


class Person(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(120), nullable=True)

    # relationships
    user_person: Mapped[list['Favorite_Character']] = relationship(back_populates='person')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'hair_color': self.hair_color,
        }


class Favorite_Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    # test: Mapped[int] = mapped_column(Integer, nullable=False)

    # relationships
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    user: Mapped[list['User']] = relationship('User')
    person_id: Mapped[int] = mapped_column(ForeignKey('person.id'), nullable=False)
    person: Mapped[list['Person']] = relationship('Person')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "person_id": self.person_id,
        }
