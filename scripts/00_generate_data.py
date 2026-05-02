import yaml
import pandas as pd
import json
from faker import Faker
import random
import os

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

fake = Faker()
seed = config["generation"]["random_seed"]
Faker.seed(seed)
random.seed(seed)

data_dir = config["data_dir"]
os.makedirs(data_dir, exist_ok=True)

# --- generate claims (Parquet) ---
num_claims = config["generation"]["num_claims"]
num_providers = config["generation"]["num_providers"]
claims = []
for _ in range(num_claims):
    claims.append({
        "claim_id": fake.unique.random_int(min=100000, max=9999999),   # unique per claim
        "patient_id": random.randint(1000, 500000),                    # NOT unique – patient can have many claims
        "provider_id": f"P{random.randint(1, num_providers):03d}",
        "claim_amount": round(random.uniform(200, 5000), 2),
        "paid_amount": round(random.uniform(0, 4500), 2),
        "claim_date": fake.date_between(start_date="-2y", end_date="today").isoformat(),
        "payment_status": random.choices(["paid", "pending", "denied"], weights=[0.8, 0.15, 0.05])[0]
    })
df_claims = pd.DataFrame(claims)
claims_path = os.path.join(data_dir, "claims.parquet")
df_claims.to_parquet(claims_path, index=False)

# --- generate providers (nested JSON) ---
providers = []
for i in range(1, num_providers + 1):
    providers.append({
        "provider_id": f"P{i:03d}",
        "name": fake.name(),
        "specialty": random.choice(["Cardiology", "Dermatology", "Orthopedics", "Neurology", "Pediatrics"]),
        "npi": fake.unique.random_number(digits=10),
        "location": {
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip": fake.zipcode()
        },
        "contract_network": random.choice(["PPO", "HMO", "EPO"])
    })
providers_path = os.path.join(data_dir, "providers.json")
with open(providers_path, "w") as f:
    json.dump(providers, f, indent=2)

print(f"Generated {num_claims} claims -> {claims_path}")
print(f"Generated {num_providers} providers -> {providers_path}")

# Reset unique after generation (optional)
fake.unique.clear()
