# Copyright 2024-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import dataclasses
import json
import sys
import types
from dataclasses import asdict, dataclass, fields
from typing import Any, TypeVar, Union, get_args, get_origin, get_type_hints

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

T = TypeVar("T")


def _unwrap_optional(expected_type: Any) -> Any:
    origin = get_origin(expected_type)
    if origin is Union or origin is types.UnionType:
        args = [arg for arg in get_args(expected_type) if arg is not type(None)]
        if len(args) == 1:
            return _unwrap_optional(args[0])
    return expected_type


def _get_list_inner_type(expected_type: Any) -> Any | None:
    expected_type = _unwrap_optional(expected_type)
    origin = get_origin(expected_type)
    if origin is list:
        args = get_args(expected_type)
        return args[0] if args else None
    return None


def filter_known_fields(cls: type[T], data: dict[str, Any]) -> dict[str, Any]:
    """Filter a dictionary to only include fields known to the dataclass.

    This prevents the SDK from breaking when the API adds new fields
    that aren't yet defined in the dataclass models.
    """
    if not dataclasses.is_dataclass(cls) or not isinstance(data, dict):
        return data
    known_fields = {f.name for f in fields(cls)}
    return {k: v for k, v in data.items() if k in known_fields}


def safe_instantiate(cls: type[T], data: dict[str, Any]) -> T:
    """Safely instantiate a dataclass, filtering out unknown fields."""
    filtered = filter_known_fields(cls, data)
    return cls(**filtered)


@dataclass
class BaseResponse:
    def __post_init__(self):
        type_hints = get_type_hints(self.__class__)
        for f in fields(self):
            value = getattr(self, f.name)
            if value is None:
                continue
            expected_type = type_hints.get(f.name)
            list_inner_type = _get_list_inner_type(expected_type)
            if list_inner_type is not None:
                if dataclasses.is_dataclass(list_inner_type) and isinstance(
                    value, list
                ):
                    setattr(
                        self,
                        f.name,
                        [
                            safe_instantiate(list_inner_type, v)
                            if isinstance(v, dict)
                            else v
                            for v in value
                        ],
                    )
            else:
                expected_type = _unwrap_optional(expected_type)
                if dataclasses.is_dataclass(expected_type) and isinstance(value, dict):
                    setattr(self, f.name, safe_instantiate(expected_type, value))

    @classmethod
    def from_response(cls, data: dict[str, Any]) -> Self:
        """Create a response instance from API data, ignoring unknown fields.

        Use this instead of direct instantiation to prevent SDK breakage
        when the API adds new fields.
        """
        return safe_instantiate(cls, data)

    def __str__(self):
        return json.dumps(asdict(self), indent=2)

    def __repr__(self):
        return self.__str__()
