# Census Causal Policy & Demographic Evaluation Engine

[![CI Test Suite](https://github.com/bealljamesp/Causal-Inference-and-Policy-Evaluation/actions/workflows/tests.yml/badge.svg)](https://github.com/bealljamesp/Causal-Inference-and-Policy-Evaluation/actions/workflows/tests.yml)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Overview

The **Census Causal Policy & Demographic Evaluation Engine** is a specialized analytical framework designed to programmatically ingest, clean, and model socio-demographic microdata directly from the **U.S. Census Bureau (USCB) REST API**.

Built for rigorous statistical and public policy research, this framework moves beyond static datasets by implementing **Structural Causal Models (SCMs)** and **Directed Acyclic Graphs (DAGs)** to control for confounding variables and estimate unbiased policy intervention impacts across regional populations.

---

## 🛠️ Key Features & Technical Stack

* **Live API Data Ingestion:** Programmatically queries multi-variable demographic and economic indicators (e.g., American Community Survey microdata) straight from USCB REST endpoints.
* **Structural Causal Modeling (SCM):** Employs causal inference estimators and DAG-based confounding control to isolate true policy intervention drivers from regional demographic noise.
* **Production MLOps Governance:** Automated unit testing suite via `pytest` and continuous integration pipelines through `GitHub Actions` (Python 3.12) ensuring data provenance and computational auditability.

---

## Sample Output
```
                            OLS Regression Results
==============================================================================
Dep. Variable:            B19013_001E   R-squared:                       0.026
Model:                            OLS   Adj. R-squared:                  0.009
Method:                 Least Squares   F-statistic:                     1.522
Date:                Thu, 30 Jul 2026   Prob (F-statistic):              0.223
Time:                        19:56:05   Log-Likelihood:                -668.33
No. Observations:                  58   AIC:                             1341.
Df Residuals:                      56   BIC:                             1345.
Df Model:                           1
Covariance Type:            nonrobust
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
const        8.123e+04   3557.784     22.830      0.000    7.41e+04    8.84e+04
B23025_005E     0.0788      0.064      1.234      0.223      -0.049       0.207
==============================================================================
Omnibus:                       12.452   Durbin-Watson:                   1.466
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               13.031
Skew:                           1.110   Prob(JB):                      0.00148
Kurtosis:                       3.683   Cond. No.                     6.07e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 6.07e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
```
---

## ⚡ Quick Start

### 1. Clone & Set Up Environment
```bash
# Clone Repository
git clone [https://github.com/bealljamesp/census-causal-policy-engine.git](https://github.com/bealljamesp/census-causal-policy-engine.git)
cd census-causal-policy-engine

# Install Package with Development Dependencies
pip install -e .[dev]
