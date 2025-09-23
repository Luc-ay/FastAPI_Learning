import enum
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from databases.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'


class OrderStatus(enum.Enum):
    PENDING = "Pending"
    IN_TRANSIT = "In-Transit"
    DELIVERED = "Delivered"


class PizzaSize(enum.Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    EXTRA_LARGE = "Extra-Large"


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    pizza_size = Column(Enum(PizzaSize), default=PizzaSize.MEDIUM, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return (f'<Order {self.id} - {self.pizza_size.value} - '
                f'{self.quantity} pcs - Status: {self.order_status.value}>')
