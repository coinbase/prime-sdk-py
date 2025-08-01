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

from ...client import Client
from ...utils import append_query_param, append_pagination_params
from .get_activity import GetActivityRequest, GetActivityResponse
from .get_entity_activity import GetEntityActivityRequest, GetEntityActivityResponse
from .list_activities import ListActivitiesRequest, ListActivitiesResponse
from .list_entity_activities import ListEntityActivitiesRequest, ListEntityActivitiesResponse


class ActivitiesService:
    def __init__(self, client: Client):
        self.client = client

    def get_activity(self, request: GetActivityRequest) -> GetActivityResponse:
        path = f"/portfolios/{request.portfolio_id}/activities/{request.activity_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetActivityResponse(**response.json())

    def get_entity_activity(self, request: GetEntityActivityRequest) -> GetEntityActivityResponse:
        path = f"/activities/{request.activity_id}"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetEntityActivityResponse(**response.json())

    def list_activities(self, request: ListActivitiesRequest) -> ListActivitiesResponse:
        path = f"/portfolios/{request.portfolio_id}/activities"

        query_params = append_query_param("", 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'categories', request.categories)
        query_params = append_query_param(query_params, 'statuses', request.statuses)

        if request.start_time:
            query_params = append_query_param(
                query_params,
                'start_time',
                request.start_time.isoformat() + 'Z')
        if request.end_time:
            query_params = append_query_param(
                query_params,
                'end_time',
                request.end_time.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListActivitiesResponse(**response.json())

    def list_entity_activities(self, request: ListEntityActivitiesRequest) -> ListEntityActivitiesResponse:
        path = f"/entities/{request.entity_id}/activities"

        query_params = append_query_param("", 'activity_level', request.activity_level)
        query_params = append_query_param(query_params, 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'categories', request.categories)
        query_params = append_query_param(query_params, 'statuses', request.statuses)

        if request.start_time:
            query_params = append_query_param(
                query_params,
                'start_time',
                request.start_time.isoformat() + 'Z')
        if request.end_time:
            query_params = append_query_param(
                query_params,
                'end_time',
                request.end_time.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListEntityActivitiesResponse(**response.json())