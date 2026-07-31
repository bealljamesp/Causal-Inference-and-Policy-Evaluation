"""Structural Causal Modeling and Policy Confounding Control."""

import pandas as pd
import statsmodels.api as sm


class CausalPolicyAnalyzer:
    """Isolates causal policy impacts by controlling for structural confounders identified via DAGs."""

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def estimate_policy_effect(
        self, treatment_col: str, outcome_col: str, confounders: list[str]
    ) -> dict:
        """Estimates the average treatment effect of a policy intervention controlling for DAG-derived confounders."""
        X = self.data[[treatment_col] + confounders]
        X = sm.add_constant(X)
        y = self.data[outcome_col]

        model = sm.OLS(y, X).fit()

        return {
            "coefficient": model.params[treatment_col],
            "p_value": model.pvalues[treatment_col],
            "confidence_interval": model.conf_int().loc[treatment_col].to_dict(),
            "r_squared": model.rsquared,
        }
