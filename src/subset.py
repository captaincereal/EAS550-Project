import pandas as pd

N_ORDERS = 10000

orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

subset_orders = (
    orders
    .sort_values("order_purchase_timestamp")
    .head(N_ORDERS)
)

subset_orders.to_csv(
    "data/subset/orders_subset.csv",
    index=False
)

print(
    f"Saved {len(subset_orders)} orders."
)