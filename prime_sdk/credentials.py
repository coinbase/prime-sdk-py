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

import json
import os
from dataclasses import dataclass

_REQUIRED_CREDENTIAL_KEYS = ("accessKey", "passphrase", "signingKey")


def _require_core_credentials(credentials_dict: dict) -> None:
    missing = [
        key for key in _REQUIRED_CREDENTIAL_KEYS if not credentials_dict.get(key)
    ]
    if missing:
        raise ValueError(
            f"PRIME_CREDENTIALS JSON must include {', '.join(_REQUIRED_CREDENTIAL_KEYS)}; "
            f"missing: {', '.join(missing)}"
        )


@dataclass
class Credentials:
    access_key: str
    passphrase: str
    signing_key: str
    portfolio_id: str | None = None
    entity_id: str | None = None
    svc_account_id: str | None = None

    @staticmethod
    def from_json(data: str) -> "Credentials":
        credentials_dict = json.loads(data)
        _require_core_credentials(credentials_dict)
        return Credentials(
            access_key=credentials_dict["accessKey"],
            passphrase=credentials_dict["passphrase"],
            signing_key=credentials_dict["signingKey"],
            portfolio_id=credentials_dict.get("portfolioId"),
            entity_id=credentials_dict.get("entityId"),
            svc_account_id=credentials_dict.get("svcAccountId"),
        )

    @staticmethod
    def from_env(variable_name: str = "PRIME_CREDENTIALS") -> "Credentials":
        """
        Load credentials from environment variables.

        Required in PRIME_CREDENTIALS JSON: accessKey, passphrase, signingKey.

        Optional:
        - PRIME_PORTFOLIO_ID / PRIME_ENTITY_ID (new format), or portfolioId / entityId in JSON
        - svcAccountId in PRIME_CREDENTIALS JSON
        """
        env_var = os.getenv(variable_name)
        if not env_var:
            raise OSError(f"{variable_name} not set as environment variable")

        credentials_dict = json.loads(env_var)
        _require_core_credentials(credentials_dict)

        portfolio_id = os.getenv("PRIME_PORTFOLIO_ID") or credentials_dict.get(
            "portfolioId"
        )
        entity_id = os.getenv("PRIME_ENTITY_ID") or credentials_dict.get("entityId")

        return Credentials(
            access_key=credentials_dict["accessKey"],
            passphrase=credentials_dict["passphrase"],
            signing_key=credentials_dict["signingKey"],
            portfolio_id=portfolio_id,
            entity_id=entity_id,
            svc_account_id=credentials_dict.get("svcAccountId"),
        )
