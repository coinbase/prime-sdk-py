import dataclasses
import importlib
import json
from pathlib import Path

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "service_model_surface.json"


def _load_service_classes() -> dict[str, type]:
    classes: dict[str, type] = {}
    package_root = Path(__file__).resolve().parents[1] / "prime_sdk"
    for path in sorted((package_root / "services").glob("*/*.py")):
        if path.name in {"__init__.py", "service.py"}:
            continue
        relative = path.relative_to(package_root).with_suffix("")
        module_path = "prime_sdk." + ".".join(relative.parts)
        module = importlib.import_module(module_path)
        for name, value in vars(module).items():
            if (
                (name.endswith(("Request", "Response")))
                and isinstance(value, type)
                and dataclasses.is_dataclass(value)
            ):
                classes[name] = value
    return classes


def test_service_model_surface_is_compatible_superset():
    surface = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    classes = _load_service_classes()

    for class_name, expected_fields in surface.items():
        assert class_name in classes, f"Missing service class: {class_name}"
        actual_fields = [
            field.name for field in dataclasses.fields(classes[class_name])
        ]
        for field_name in expected_fields:
            assert field_name in actual_fields, (
                f"{class_name} is missing field {field_name}"
            )
