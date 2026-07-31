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

## ⚡ Quick Start

### 1. Clone & Set Up Environment
```bash
# Clone Repository
git clone [https://github.com/bealljamesp/census-causal-policy-engine.git](https://github.com/bealljamesp/census-causal-policy-engine.git)
cd census-causal-policy-engine

# Install Package with Development Dependencies
pip install -e .[dev]
