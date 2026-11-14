from sqlalchemy import create_engine
from sqlalchemy import text

from config import DB_CONFIG

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

engine = create_engine(DATABASE_URL)

def transactional_reload():

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                TRUNCATE TABLE
                    order_items,
                    orders,
                    products,
                    sellers,
                    customers
                CASCADE;
                """
            )
        )

        print("Tables truncated")

        # Load data here

if __name__ == "__main__":
    transactional_reload()