from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship
from database import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'
    

class order(Base):

    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('IN-TRANSIT', 'in-ransit'),
        ('DELIVERED', 'delivered'),    
    )

    PIZZA_SIZES = (
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('ETXRRA-LARGE', 'Extra-Large'),
    )

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices = ORDER_STATUS), default = 'PENDING')
    pizza_size = Column(ChoiceType(choices = PIZZA_SIZES), default = 'MEDIUM')
    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f'<Order {self.id} - {self.pizza_size} - {self.quantity}>'