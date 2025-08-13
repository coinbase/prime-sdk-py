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

from dataclasses import dataclass
import os
import json


@dataclass
class Credentials:
    access_key: str
    passphrase: str
    signing_key: str
    portfolio_id: str
    entity_id: str
    svc_account_id: str

    @staticmethod
    def from_json(data: str) -> 'Credentials':
        credentials_dict = json.loads(data)
        return Credentials(
            access_key=credentials_dict['accessKey'],
            passphrase=credentials_dict['passphrase'],
            signing_key=credentials_dict['signingKey'],
            portfolio_id=credentials_dict['portfolioId'],
            entity_id=credentials_dict['entityId'],
            svc_account_id=credentials_dict['svcAccountId']
        )

    @staticmethod
    def from_env(variable_name: str = 'PRIME_CREDENTIALS') -> 'Credentials':
        """
        Load credentials from environment variables.
        
        New format:
        - PRIME_CREDENTIALS: JSON with accessKey, passphrase, signingKey, svcAccountId
        - PRIME_PORTFOLIO_ID: Portfolio ID 
        - PRIME_ENTITY_ID: Entity ID
        
        Legacy format (backwards compatible):
        - PRIME_CREDENTIALS: JSON with all fields including portfolioId and entityId
        """
        env_var = os.getenv(variable_name)
        if not env_var:
            raise EnvironmentError(
                f"{variable_name} not set as environment variable")
        
        credentials_dict = json.loads(env_var)
        
        portfolio_id = os.getenv('PRIME_PORTFOLIO_ID')
        entity_id = os.getenv('PRIME_ENTITY_ID')
        
        if portfolio_id and entity_id:
            return Credentials(
                access_key=credentials_dict['accessKey'],
                passphrase=credentials_dict['passphrase'],
                signing_key=credentials_dict['signingKey'],
                portfolio_id=portfolio_id,
                entity_id=entity_id,
                svc_account_id=credentials_dict['svcAccountId']
            )
        else:
            # Legacy format - all fields in PRIME_CREDENTIALS
            return Credentials(
                access_key=credentials_dict['accessKey'],
                passphrase=credentials_dict['passphrase'],
                signing_key=credentials_dict['signingKey'],
                portfolio_id=credentials_dict['portfolioId'],
                entity_id=credentials_dict['entityId'],
                svc_account_id=credentials_dict['svcAccountId']
            )
