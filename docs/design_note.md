# Design Note

## Dataset

The project uses the following datasets:

- Orders
- Customers
- Order Items
- Products
- Sellers

A reproducible subset of the earliest 10,000 orders was selected.

## Functional Dependencies

- customer_id -> customer attributes
- seller_id -> seller attributes
- product_id -> product attributes
- order_id -> order attributes
- (order_id, order_item_id) -> product_id, seller_id, shipping_limit_date, price, freight_value

## Normalization

The schema satisfies Third Normal Form (3NF):

- Each table represents a single entity.
- Every non-key attribute depends on the key.
- No transitive dependencies exist.
- Many-to-many relationships are resolved through order_items.