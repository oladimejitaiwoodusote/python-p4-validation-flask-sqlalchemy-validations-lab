from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


    # def __repr__(self):
    #     return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name cannot be null")
        return value

    @validates('phone_number')
    def validate_number(self, key, number):
        if len(number) != 10:
            raise ValueError("Number has to be 10 digits")
        return number

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now()) 


    @validates('title')
    def validate_title(self, key, value):
        if not value:
            raise ValueError("All posts must have a title")
        return value

    @validates('content')
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError("Content has to be atleast 250 characters")
        return value

    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) > 250:
            raise ValueError("Summary cannot be more than 250 characters")
        return value
    
    @validates('category')
    def validate_category(self, key, value):
        if value != "Fiction" and value != "Non-Fiction":
            raise ValueError("Category has to be either fiction or non-fiction")
        return value

    @validates('title')
    def validate_title(self, key, value):
        if "Won't Believe" or "Secret" or "Top" or "Guess" not in value:
            raise ValueError("Title has to be clickbait-y")
        return value

    

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
