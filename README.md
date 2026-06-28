# 🏦 BDA Synthetic Banking Data Model  
## *La Banque D’Avoine — Vancouver Branch Simulation (2019–2024)*

---

## 📌 Overview

This synthetic dataset models customer banking behavior for a retail bank operating in downtown Vancouver, BC.

It is designed for research and machine learning applications focused on:

- Digital banking adoption  
- Customer behavioral segmentation  
- Branch vs digital channel usage  
- Operational impacts of external events (weather, holidays, pandemic, sports)  

The data follows a **relational schema** with fact and dimension tables similar to a real banking system.

---

# 🧱 Entity Relationship Structure

```text
CUSTOMERS ────< ACCOUNTS ────< TRANSACTIONS
     │                          │
     │                          ├── External event joins (time-based)
     │
     ├── CUSTOMER_PROFILE (simulation layer)
     ├── DIGITAL_ADOPTION_SCORE (target variable)
     │
BRANCHES ────────────────┐
                         └── TRANSACTIONS

EXTERNAL_EVENTS ────────(joined via date/time)
```

