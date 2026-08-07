# Copyright 2025-present Coinbase Global, Inc.
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

from dataclasses import dataclass

from ...base_request import BasePaginatedRequest
from ...base_response import BaseResponse
from ...model import GetEntityActivitiesRequest as _GetEntityActivitiesRequest
from ...model import GetEntityActivitiesResponse as _GetEntityActivitiesResponse


@dataclass(kw_only=True)
class ListEntityActivitiesRequest(BasePaginatedRequest, _GetEntityActivitiesRequest):
    """
    List Entity Activities

    Attributes:
        entity_id: Entity to retrieve activities for
        activity_level: Activity level to retrieve activities for
        symbols: Filter by list of currencies
        categories: Filter by list of activity categories [order, transaction, account,
            allocation, lending]
        statuses: Filter by list of statuses
        start_time: Filter created time by start date (RFC3339 format)
        end_time: Filter created time by end date (RFC3339 format)
        get_network_unified_activities: Flag to request retrieval of all activities across
            all networks for a given symbol
    """


@dataclass
class ListEntityActivitiesResponse(BaseResponse, _GetEntityActivitiesResponse):
    """ListEntityActivitiesResponse(activities: 'list[Activity]' = None, pagination: 'PaginatedResponse' = None)"""
