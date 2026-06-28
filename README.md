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

---

## 👤 1. CUSTOMERS (Dimension Table)

Represents individual bank clients.

### Primary Key
* customer_id

### Fields
| Column	| Type | Description |
| --- | --- | --- | 
| customer_id	| INT | Unique customer identifier |
| first_name	| STRING |	Synthetic first name |
| last_name	| STRING |	Synthetic last name |
| date_of_birth	| DATE |	Used to derive age |
| age	| INT |	Customer age |
| occupation	| STRING |	Employment category |
| income_band	| STRING |	Low / Mid / High |
| city	| STRING |	Vancouver region |
| province	| STRING |	BC |
| postal_code	| STRING |	Canadian postal code |
| country	| STRING |	Canada |
| customer_since	| DATE |	Account opening date |
| home_branch_id	| INT |	FK → BRANCHES |
| high_value_client	| BOOLEAN |	Net worth > $500,000 |
| digital_adoption_score	| FLOAT |	(0–100) target variable |

---

## 💳 2. ACCOUNTS (Dimension Table)

Represents bank accounts held by customers.

### Primary Key
* account_id
* Foreign Keys
* customer_id → CUSTOMERS
* transit_number → BRANCHES

### Fields
| Column	| Type | Description |
| --- | --- | --- | 
| account_id	|	INT |	Unique account ID |
| customer_id	|	INT |	Account owner |
| account_type	|	STRING |	Chequing, Savings, Credit, etc. |
| opened_date	|	DATE |	Account creation date |
| transit_number	|	STRING |	Branch identifier |
| account_number	|	STRING |	Synthetic account number |
| current_balance	|	FLOAT |	Simulated balance |
| currency	|	STRING |	CAD / USD |
| status	|	STRING |	Active / Dormant |

---
