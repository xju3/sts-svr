from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import Mapped
import uuid

def generate_uuid():
    return str(uuid.uuid1())

class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid)