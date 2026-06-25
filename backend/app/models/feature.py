from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Feature(Base):
    __tablename__ = "features"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    data_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="features"
    )
    observation_values: Mapped[list["ObservationValue"]] = relationship(
    back_populates="feature",
    cascade="all, delete-orphan"
    )