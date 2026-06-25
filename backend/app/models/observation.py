from datetime import datetime, UTC

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Observation(Base):
    __tablename__ = "observations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    target_value: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    default=lambda: datetime.now(UTC)
    )

    category: Mapped["Category"] = relationship(
        back_populates="observations"
    )

    values: Mapped[list["ObservationValue"]] = relationship(
        back_populates="observation",
        cascade="all, delete-orphan"
    )