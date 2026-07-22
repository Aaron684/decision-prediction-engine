from app.training.exceptions import TypeConversionError


def convert_feature_value(
    value: str,
    data_type: str,
):
    """
    Convert a feature value from its database representation
    into a machine learning compatible Python value
    """

    try:
        if data_type == "numeric":
            return float(value)

        if data_type == "boolean":

            if isinstance(value, bool):
                return value


            if isinstance(value, str):

                normalized = value.lower()

                if normalized == "true":
                    return True

                if normalized == "false":
                    return False


            raise ValueError(
            f"Invalid boolean value: {value}"
        )

        raise TypeConversionError(
            f"Unsupported feature data type: {data_type}"
        )

    except (ValueError, TypeError) as exc:
        raise TypeConversionError(
            f"Could not convert value '{value}' "
            f"to type '{data_type}'."
        ) from exc


def convert_target_value(
    value: str,
    target_type: str,
):
    """
    Convert a target value into a machine learning compatible value
    """

    try:
        if target_type == "regression":
            return float(value)

        if target_type == "classification":
            return convert_boolean(value)

        raise TypeConversionError(
            f"Unsupported target type: {target_type}"
        )

    except (ValueError, TypeError) as exc:
        raise TypeConversionError(
            f"Could not convert target value '{value}' "
            f"to type '{target_type}'."
        ) from exc


def convert_boolean(value: str) -> int:
    """
    Convert a string boolean representation into 0 or 1
    """

    normalized = value.strip().lower()

    if normalized == "true":
        return 1

    if normalized == "false":
        return 0

    raise TypeConversionError(
        f"Invalid boolean value: '{value}'. "
        "Expected 'true' or 'false'."
    )