class TrainingError(Exception):
    """Base exception for all training pipeline errors."""


class DatasetNotFoundError(TrainingError):
    """Raised when the requested category does not exist."""

class TypeConversionError(TrainingError):
    """Raised when a value cannot be converted."""

class DatasetValidationError(TrainingError):
    """Raised when a dataset cannot be used for training."""


class MissingFeatureError(DatasetValidationError):
    """Raised when an observation is missing a required feature."""


class DuplicateFeatureValueError(DatasetValidationError):
    """Raised when an observation contains duplicate values for a feature."""


class InvalidFeatureValueError(DatasetValidationError):
    """Raised when a feature value is missing or cannot be converted to its declared type."""


class InvalidTargetValueError(DatasetValidationError):
    """Raised when a target value cannot be converted."""


class InsufficientDataError(DatasetValidationError):
    """Raised when a dataset does not contain enough information to train."""

class UnexpectedFeatureError(DatasetValidationError):
    """Raised when an observation contains a feature not belonging to the category."""