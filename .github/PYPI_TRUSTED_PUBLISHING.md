# PyPI trusted publishing setup

Configure trusted publishing on [pypi.org/manage/project/prime-sdk-py/settings/publishing/](https://pypi.org/manage/project/prime-sdk-py/settings/publishing/) before the first release from this repository.

## coinbase/prime-sdk-py (active publisher)

| Field | Value |
|-------|-------|
| Owner | `coinbase` |
| Repository | `prime-sdk-py` |
| Workflow name | `publish prime-sdk-py` |
| Environment | `release` |

Ensure the GitHub **release** environment exists in this repository with the same protection rules as the former coinbase-samples repo.

## coinbase-samples/prime-sdk-py (retire after 1.7.2)

After PyPI shows `1.7.2`, remove the trusted publisher entry for `coinbase-samples/prime-sdk-py` so only this repository can publish `1.8.0` and later.
