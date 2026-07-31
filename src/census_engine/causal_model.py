import pandas as pd
import statsmodels.api as sm


class CausalPolicyAnalyzer:

    def __init__(self, data: pd.DataFrame):
        self.data = data.dropna()  # Clean missing values for regression

    def estimate_policy_effect(
        self, treatment_col: str, outcome_col: str, confounders: list[str]
    ) -> dict:
        """Estimates the policy effect via OLS while controlling for DAG confounders."""
        X = self.data[[treatment_col] + confounders]
        X = sm.add_constant(X)
        y = self.data[outcome_col]

        model = sm.OLS(y, X).fit()

        # Create a structured dictionary of results
        results = {
            "treatment_variable": treatment_col,
            "outcome_variable": outcome_col,
            "coefficient": model.params[treatment_col],
            "std_error": model.bse[treatment_col],
            "p_value": model.pvalues[treatment_col],
            "r_squared": model.rsquared,
            "observations": int(model.nobs),
        }

        return results, model.summary()
