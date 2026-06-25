from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ObservationValue(Base):
    __tablename__ = "observation_values"

    observation_id: Mapped[int] = mapped_column(
        ForeignKey("observations.id"),
        primary_key=True
    )

    feature_id: Mapped[int] = mapped_column(
        ForeignKey("features.id"),
        primary_key=True
    )

    value: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    observation: Mapped["Observation"] = relationship(
        back_populates="values"
    )

    feature: Mapped["Feature"] = relationship(
        back_populates="observation_values"
    )