# noqa: D100


def format_kopeks(kopeks: int) -> str: 
    """Форматирует сумму в копейках в строку с разделителями тысяч и десятичной запятой.
    
    Args:
        kopeks: Сумма в копейках.
    
    Returns:
        Отформатированная строка с суммой в рублях и копейках.
    """
    return f"{kopeks / 100:,.2f} ₽".replace(",", " ").replace(".", ",")


def format_title(text: str, width: int = 40) -> str:
    """Форматирует заголовок, центрируя его и обрамляя знаками '='.

    Args:
        text: Текст заголовка.
        width: Общая ширина строки.

    Returns:
        Отформатированный заголовок.
    """
    return text.center(width, "=")
