"""Main Execution Pipeline for Census Causal Policy Engine."""

import os

from census_engine.api_client import CensusAPIClient
from census_engine.causal_model import CausalPolicyAnalyzer


def main():
    print("🚀 Initializing Census Causal Policy Evaluation Engine...")

    # 1. Ingest Raw Data (Saves untouched snapshot to data/raw/)
    client = CensusAPIClient()
    target_vars = [
        "B19013_001E",  # Median Household Income
        "B23025_005E",  # Unemployment Count
    ]

    try:
        df_raw = client.fetch_demographic_data(variables=target_vars, state_fips="06")
        print(
            f"Successfully ingested {len(df_raw)} raw county-level records from USCB."
        )
    except Exception as e:
        print(f"API connection note: {e}")
        return

    # 2. TRANSFORM LAYER: Build Processed Dataset
    print("Processing and cleaning dataset for statistical modeling...")
    df_processed = df_raw.copy()

    # Clean invalid/negative Census missing data codes if present
    for var in target_vars:
        df_processed[var] = df_processed[var].apply(lambda x: x if x >= 0 else None)

    # Drop rows with missing analytical values for clean estimation
    df_processed = df_processed.dropna(subset=target_vars)

    # Feature Engineering: Add a derived analytical ratio column
    df_processed["Income_Unemployment_Ratio"] = df_processed["B19013_001E"] / (
        df_processed["B23025_005E"] + 1
    )

    # PERSISTENCE: Save processed layer to disk
    os.makedirs("data/processed", exist_ok=True)
    df_processed.to_csv("data/processed/census_processed_ca.csv", index=False)
    print(f"Processed dataset saved: {len(df_processed)} valid records retained.")

    # 3. Run Causal Estimation on Processed Data
    analyzer = CausalPolicyAnalyzer(df_processed)
    print("Executing Structural Causal Modeling (SCM) via regression controls...")

    results_dict, model_summary = analyzer.estimate_policy_effect(
        treatment_col="B23025_005E",
        outcome_col="B19013_001E",
        confounders=["B19013_001E"],
    )

    # Save Causal Report Audit Trail
    os.makedirs("docs", exist_ok=True)
    with open("docs/causal_regression_report.txt", "w") as f:
        f.write(str(model_summary))

    print("✨ Pipeline execution complete!")
    print("-> Raw Snapshot: data/raw/census_raw_ca.csv")
    print("-> Processed Layer: data/processed/census_processed_ca.csv")
    print("-> Audit Report: docs/causal_regression_report.txt")


if __name__ == "__main__":
    main()
