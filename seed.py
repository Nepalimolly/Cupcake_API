from app import app
from models import db, Cupcake

# Create an application context
with app.app_context():
    # Drop all existing tables
    db.drop_all()

    # Create all defined tables
    db.create_all()

    # Create and add Cupcake instances
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    db.session.add_all([c1, c2])
    db.session.commit()
