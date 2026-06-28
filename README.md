# BDA-Synthetic-Bank-Dataset
This is a synthetic dataset for a fictional bank called BDA, La Banque D'Avoine, focusing on a location in downtown Vancouver, it has restrictions that incorporate human behavior, due to the environment, and personal barriers. This can be used for data analysis or model fitting if necessary. 

🏦 BDA Synthetic Banking Data Model

La Banque D’Avoine — Vancouver Branch Simulation (2019–2024)

📌 Overview

This synthetic dataset models customer banking behavior for a retail bank operating in downtown Vancouver, BC. It is designed for research and machine learning applications focused on:

Digital banking adoption
Customer behavioral segmentation
Branch vs digital channel usage
Operational impacts of external events (weather, holidays, pandemic, sports)

The data follows a relational schema with fact and dimension tables similar to a real banking system.

🧱 Entity Relationship Structure
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
👤 1. CUSTOMERS (Dimension Table)

Represents individual bank clients.

Primary Key
customer_id
Fields
Column	Type	Description
customer_id	INT	Unique customer identifier
first_name	STRING	Synthetic first name
last_name	STRING	Synthetic last name
date_of_birth	DATE	Used to derive age
age	INT	Customer age
occupation	STRING	Employment category
income_band	STRING	Low / Mid / High
city	STRING	Vancouver region
province	STRING	BC
postal_code	STRING	Canadian postal code
country	STRING	Canada
customer_since	DATE	Account opening date
home_branch_id	INT	FK → BRANCHES
high_value_client	BOOLEAN	Net worth > $500,000
digital_adoption_score	FLOAT	(0–100) target variable
💳 2. ACCOUNTS (Dimension Table)

Represents bank accounts held by customers.

Primary Key
account_id
Foreign Keys
customer_id → CUSTOMERS
transit_number → BRANCHES
Fields
Column	Type	Description
account_id	INT	Unique account ID
customer_id	INT	Account owner
account_type	STRING	Chequing, Savings, Credit, etc.
opened_date	DATE	Account creation date
transit_number	STRING	Branch identifier
account_number	STRING	Synthetic account number
current_balance	FLOAT	Simulated balance
currency	STRING	CAD / USD
status	STRING	Active / Dormant
🏢 3. BRANCHES (Reference Table)

Represents physical bank locations.

Primary Key
branch_id
Fields
Column	Type	Description
branch_id	INT	Unique branch ID
transit_number	STRING	Branch routing number
branch_name	STRING	Branch name
address	STRING	Physical address
city	STRING	Vancouver
province	STRING	BC
foot_traffic_level	STRING	Low / Medium / High
is_flagship	BOOLEAN	Flagship branch indicator
💰 4. TRANSACTIONS (Fact Table)

Core behavioral dataset capturing all banking activity.

Primary Key
transaction_id
Foreign Keys
customer_id → CUSTOMERS
account_id → ACCOUNTS
branch_id → BRANCHES
Fields
Column	Type	Description
transaction_id	INT	Unique transaction
transaction_datetime	DATETIME	Timestamp
customer_id	INT	Customer reference
account_id	INT	Account reference
branch_id	INT	Branch (if applicable)
channel	STRING	Online / ATM / Branch / Phone
transaction_type	STRING	Action type
transaction_category	STRING	Financial / Service
amount	FLOAT	Monetary value (nullable)
account_type_used	STRING	If applicable
success_flag	BOOLEAN	Transaction success
duration_minutes	FLOAT	Interaction duration
is_holiday	BOOLEAN	Holiday indicator
weather_event	STRING	Weather condition
sports_event	STRING	Sports/game impact
pandemic_phase	STRING	Time period classification
Transaction Types
Financial
cash_in
cash_out
bill_payment
credit_card_payment
loan_payment
draft_purchase
transfer
Service / Administrative
password_reset
address_change
debit_card_replacement
cheque_order
statement_request
direct_deposit_setup
appointment_booking
🧠 5. CUSTOMER BEHAVIOR PROFILE (Simulation Layer)

Used only for synthetic data generation (not for ML training leakage).

Primary Key
customer_id
Fields
Column	Type	Description
customer_id	INT	Customer reference
behavioral_segment	STRING	Customer archetype
digital_confidence	FLOAT	0–100
branch_preference_score	FLOAT	0–100
atm_preference_score	FLOAT	0–100
mobile_app_usage_probability	FLOAT	0–1
financial_literacy_score	FLOAT	0–100
accessibility_needs_flag	BOOLEAN	Support requirement
🌍 6. EXTERNAL EVENTS (Time-Based Context Table)

Used to model real-world influences on banking behavior.

Primary Key
event_date
Fields
Column	Type	Description
event_date	DATE	Calendar date
is_holiday	BOOLEAN	Public holiday
holiday_name	STRING	Holiday label
weather_event	STRING	Snow, rainstorm, windstorm
weather_severity	INT	Scale 1–5
sports_event	STRING	NHL / concert / none
pandemic_phase	STRING	Pre / lockdown / recovery / post
Pandemic Phases
Period	Label
2019	pre_pandemic
2020	lockdown_transition
2021	hybrid_recovery
2022–2024	post_pandemic_normalization
🔗 Relationships Summary
One-to-Many
Customers → Accounts
Customers → Transactions
Accounts → Transactions
Branches → Transactions
Time-Based Joins
Transactions ↔ External Events (via date/time)
📊 Design Intent

This schema is designed to support:

Behavioral modeling of digital banking adoption
Branch vs digital channel analysis
Customer segmentation
Time-series analysis (2019–2024)
External event impact modeling
Explainable machine learning (XAI-ready structure)
⚙️ Notes on Data Generation
Customer behavior is driven by hidden synthetic profiles
External events modify probabilities of transaction types
Pandemic phases shift channel preferences over time
Seasonality (holidays, weather, sports) affects transaction volume and type
