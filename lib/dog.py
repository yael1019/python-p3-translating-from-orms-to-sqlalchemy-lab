from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).where(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).where(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).where(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    return session.query(Dog).where(Dog.id == dog.id).update({Dog.breed: breed})