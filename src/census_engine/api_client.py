"""U.S. Census Bureau (USCB) REST API Client."""

import os

import pandas as pd
import requests


class CensusAPIClient:
    """Handles authentication and data retrieval from the U.S. Census Bureau API."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("CENSUS_API_KEY")
        self.base_url = "https://api.census.gov/data/2022/acs/acs5"

    def fetch_demographic_data(
        self, variables: list[str], state_fips: str = "06"
    ) -> pd.DataFrame:
        """Queries socio-demographic indicators for a target state (default: California)."""
        var_string = ",".join(variables)
        params = {
            "get": f"NAME,{var_string}",
            "for": "county:*",
            "in": f"state:{state_fips}",
        }
        if self.api_key:
            params["key"] = self.api_key

        response = requests.get(self.base_url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()
        header, rows = data[0], data[1:]
        df = pd.DataFrame(rows, columns=header)

        # Convert numeric columns
        for var in variables:
            df[var] = pd.to_numeric(df[var], errors="coerce")

        return df
