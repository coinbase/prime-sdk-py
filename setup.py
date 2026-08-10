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

from pathlib import Path

from setuptools import find_packages, setup

# Keep in sync with VERSION in prime_sdk/version.py.
VERSION = "1.10.0"

setup(
    name="prime-sdk-py",
    version=VERSION,
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["prime_sdk.examples", "prime_sdk.examples.*"]),
    install_requires=[
        "requests",
        # `Self` is only available in typing on Python 3.11+
        "typing_extensions; python_version < '3.11'",
    ],
    project_urls={
        "Source": "https://github.com/coinbase/prime-sdk-py",
        "Issue Tracker": "https://github.com/coinbase/prime-sdk-py/issues",
    },
    entry_points={
        "console_scripts": [
            "prime-sdk=prime_sdk.__main__:main",
        ],
    },
)
