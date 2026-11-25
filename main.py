from models.database import Base, engine

Base.metadata.create_all(engine)
print("Datbase tables created successfully")