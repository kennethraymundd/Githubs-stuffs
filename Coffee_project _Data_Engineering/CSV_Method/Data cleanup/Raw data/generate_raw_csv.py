import csv
import random
from datetime import datetime, timedelta

OUTPUT_FILE = r"C:\Users\kenne\Documents\Business Stuffs\Github\Coffee_project _Data_Engineering\Raw data file\raw_coffee_data.csv"
ROW_COUNT = 1000

payment_methods = ["cash", " CASH ", "card", " CARD ", "c@sh", "gcash", None]
stores = ["s001", "S001", " s002", "S002 ", "s003", None]
date_formats = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y"]

def random_date():
    base = datetime(2024, 1, 1)
    delta = timedelta(days=random.randint(0, 10))
    d = base + delta
    fmt = random.choice(date_formats)
    return d.strftime(fmt)

def random_amount():
    choices = [
        str(random.randint(50, 500)),     # valid
        f" {random.randint(50, 500)} ",   # extra spaces
        "-50",                             # invalid business logic
        "100.5",                           # wrong type
        "one_hundred",                     # wrong type
        "",                                # null
    ]
    return random.choice(choices)

rows = []

# header with extra spaces
rows.append([
    "order_id ",
    " customer_id  ",
    " order_date ",
    " amount ",
    " payment_method ",
    " store_id"
])

for i in range(1, ROW_COUNT + 1):
    order_id = i

    # create duplicates
    if random.random() < 0.05:
        order_id = random.randint(1, i)

    customer_id = random.choice([
        f" {str(random.randint(1, 300)).zfill(3)} ",
        "",
        None
    ])

    row = [
        f"{order_id} ",
        customer_id,
        random_date(),
        random_amount(),
        random.choice(payment_methods),
        random.choice(stores)
    ]

    rows.append(row)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Generated {ROW_COUNT} messy rows in {OUTPUT_FILE}")
