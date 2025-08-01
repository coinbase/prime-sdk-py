from prime_sdk.services.portfolios import ListPortfoliosResponse
from prime_sdk.model import Portfolio


def test_list_portfolios_response_parsing():
    # Complete mock portfolio data with all required fields
    mock_portfolios_data = [
        {
            "id": "fake-portfolio-id-123",
            "name": "CryptoBalances",
            "entity_id": "fake-entity-id",
            "organization_id": "fake-org-id",
            "entity_name": "Sample Prime Entity"
        }
    ]

    # Initialize with the actual field values
    response = ListPortfoliosResponse(portfolios=mock_portfolios_data)

    assert isinstance(response.portfolios, list)
    assert len(response.portfolios) == 1
    assert isinstance(response.portfolios[0], Portfolio)

    portfolio = response.portfolios[0]
    assert portfolio.id == "fake-portfolio-id-123"
    assert portfolio.name == "CryptoBalances"
    assert portfolio.entity_id == "fake-entity-id"
    assert portfolio.organization_id == "fake-org-id"
    assert portfolio.entity_name == "Sample Prime Entity"
