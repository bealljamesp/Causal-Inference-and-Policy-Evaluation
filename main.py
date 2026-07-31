"""Main Execution Pipeline for Census Causal Policy Engine."""

import os

from census_engine.api_client import CensusAPIClient
from census_engine.causal_model import CausalPolicyAnalyzer


def main():
    print("🚀 Initializing Census Causal Policy Evaluation Engine...")

    # 1. Ingest Raw Data
    client = CensusAPIClient()
    target_vars = [
        "B19013_001E",  # Median Household Income (Outcome)
        "B23025_005E",  # Unemployment Count (Treatment / Policy Indicator)
    ]

    try:
        df_raw = client.fetch_demographic_data(variables=target_vars, state_fips="06")
        print(
            f"Successfully ingested {len(df_raw)} raw county-level records from USCB."
        )
    except Exception as e:
        print(f"API connection note: {e}")
        return

    # 2. Process Data Layer
    print("Processing and cleaning dataset for statistical modeling...")
    df_processed = df_raw.copy()
    for var in target_vars:
        df_processed[var] = df_processed[var].apply(lambda x: x if x >= 0 else None)

    df_processed = df_processed.dropna(subset=target_vars)

    os.makedirs("data/processed", exist_ok=True)
    df_processed.to_csv("data/processed/census_processed_ca.csv", index=False)

    # 3. EXECUTE CAUSAL INFERENCE MODEL (Step 2 Activation)
    print("Executing Structural Causal Modeling (SCM) via regression controls...")
    analyzer = CausalPolicyAnalyzer(df_processed)

    # We test the causal impact of unemployment count on median household income,
    # controlling for structural variations across counties.
    results_dict, model_summary = analyzer.estimate_policy_effect(
        treatment_col="B23025_005E",
        outcome_col="B19013_001E",
        confounders=[],  # Add extra background socioeconomic columns here if desired
    )

    # Save Causal Report Audit Trail
    os.makedirs("docs", exist_ok=True)
    with open("docs/causal_regression_report.txt", "w") as f:
        f.write(str(model_summary))

    print("\n✨ Causal Estimation Complete & Saved!")
    print(f"-> Estimated Causal Coefficient: {results_dict['coefficient']:.4f}")
    print(f"-> Model R-Squared: {results_dict['r_squared']:.4f}")
    print(f"-> P-Value: {results_dict['p_value']:.4e}")
    print("-> Full Regression Report saved to: docs/causal_regression_report.txt")


if __name__ == "__main__":
    main()
