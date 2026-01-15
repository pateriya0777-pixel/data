from fastapi import Depends, FastAPI
app  = FastAPI()
from models import product
from config import session,engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods =["*"])

database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def Greet():
    return "Welcoome fastpi"

products=[product(id=1,name='mmouse',description='portonics product',price=499,quantity=10),
          product(id=2,name='keyboard',description='portonics product',price=599,quantity=20),
          product(id=3,name='notepad',description='portonics product',price=5,quantity=50)]


def get_db():
    try:
        db= session()
        yield db 
    finally:
         db.close()

def init_db():
    db = session()
    count = db.query(database_models.product).count
    if count ==0:
        for prod in products:
            db.add(database_models.product(**prod.model_dump()))
        db.commit()
init_db()

@app.get("/products")
def get_all_product(db:Session = Depends(get_db)):
    db_product = db.query(database_models.product).all()
    return db_product

@app.get("/products/{id}")
def get_product_by_id(id:int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_product:
        return db_product
    return "product not found"

@app.post("/products")
def add_product(product:product, db:Session = Depends(get_db)):
    db.add(database_models.product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}") 
def update_product(id:int, product:product, db:Session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "update successfully"
    return "product id not found"

@app.delete("/products/{id}") 
def delete_product(id:int, db:Session = Depends(get_db)):
    db_product = db.query(database_models.product).filter(database_models.product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "delete successfully"
    return "product id not found"
