from datetime import datetime, timezone

from sqlalchemy import Boolean, Float, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class TrainedModel(Base):
    __tablename__ = "trained_models"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    model_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    model_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    model_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    observation_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    primary_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    secondary_metrics: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="trained_models"
    )