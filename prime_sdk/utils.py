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

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class PaginationParams:
    cursor: str = ""
    limit: str = ""
    sort_direction: str = ""

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def append_query_param(
    query_params: str, key: str, value: str | list[str] | None
) -> str:
    if value:
        if isinstance(value, list):
            for v in value:
                query_params = (
                    f"{query_params}&{key}={v}" if query_params else f"{key}={v}"
                )
        else:
            query_params = (
                f"{query_params}&{key}={value}" if query_params else f"{key}={value}"
            )
    return query_params


def append_pagination_params(
    query_params: str, pagination: PaginationParams | None
) -> str:
    if pagination:
        query_params = append_query_param(query_params, "cursor", pagination.cursor)
        query_params = append_query_param(query_params, "limit", pagination.limit)
        query_params = append_query_param(
            query_params, "sort_direction", pagination.sort_direction
        )
    return query_params


@dataclass
class Pagination:
    next_cursor: str = ""
    sort_direction: str = ""
    has_next: bool = False

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def to_body_dict(obj: Any) -> dict[str, Any]:
    """
    Convert a dataclass to a dictionary, converting enum values to their string representation.
    This is used for request objects that need to be serialized for API calls.
    """
    result = {}
    for k, v in asdict(obj).items():
        if v is not None:
            # Convert enums to their string values
            if hasattr(v, "value"):
                result[k] = v.value
            else:
                result[k] = v
    return result
