import dataclasses
import json
from pathlib import Path

from prime_sdk import model

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "model_surface.json"


def test_model_surface_is_compatible_superset():
    surface = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    for class_name, expected_fields in surface.items():
        assert hasattr(model, class_name), f"Missing model class: {class_name}"

        cls = getattr(model, class_name)
        assert dataclasses.is_dataclass(cls), f"{class_name} is not a dataclass"

        actual_fields = [field.name for field in dataclasses.fields(cls)]

        for index, field_name in enumerate(expected_fields):
            assert field_name in actual_fields, (
                f"{class_name} is missing field {field_name}"
            )
            assert actual_fields[index] == field_name, (
                f"{class_name} field order mismatch at position {index}: "
                f"expected {field_name}, got {actual_fields[index]}"
            )
