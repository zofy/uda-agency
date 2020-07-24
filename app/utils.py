import logging
from typing import Any, List

import flask


def paginate(request: flask.Request, items: List[Any], per_page: int) -> List[Any]:
    """Paginate items for a given page"""
    page = request.args.get('page', 1, type=int)
    start, end = (page - 1) * per_page, page * per_page
    return items[start: end]


def setup_logger(file_path: str, logger: logging.Logger) -> None:
    """Setup file handler for a given logger"""
    fh = logging.FileHandler(file_path)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
