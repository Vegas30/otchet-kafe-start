from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Загружает заказы из CSV-файла.
    
    Args:
        path: Путь к CSV-файлу с заказами.
    
    Returns:
        Список объектов Order, загруженных из файла.
    """
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Args:
        orders: Список заказов.
        top: Количество лучших официантов для возврата.

    Returns:
        Словарь с суммами выручки по официантам.
    """  # noqa: D205
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """_summary_.
    
    Args:
        orders: _description_
    #
    """
    orders.sort(key=lambda order: -order.kopeks)
