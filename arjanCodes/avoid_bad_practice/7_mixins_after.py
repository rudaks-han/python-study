from dataclasses import dataclass
from typing import Callable


@dataclass
class Order:
    customer_email: str
    product_id: int
    quantity: int


def log(message: str) -> None:
    print(f"LOG: {message}")


def save() -> None:
    print("Data saved")


type SaveFn = Callable[[], None]
type LogFn = Callable[[str], None]


def process_order(order: Order, saver: SaveFn, logger: LogFn) -> None:
    logger(f"Processing order {order}")
    saver()


def cancel_order(order: Order, saver: SaveFn, logger: LogFn) -> None:
    logger(f"Cancelling order {order}")
    saver()


def main() -> None:
    order = Order(customer_email="test@test.com", product_id=123, quantity=2)
    process_order(order, save, log)
    cancel_order(order, save, log)


if __name__ == "__main__":
    main()
