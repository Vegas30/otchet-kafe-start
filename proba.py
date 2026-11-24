from app.services.calculator import grade_bounds
from app.utils.formatter import format_kopeks, format_title
from typing import reveal_type

bounds = grade_bounds([5, 3, 4])
reveal_type(bounds)

title = format_title("40")
price = format_kopeks(1250)