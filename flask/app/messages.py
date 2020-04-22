from typing import NamedTuple


class MessageCategory:
    INFO = "info"
    DANGER = "danger"
    WARNING = "warning"
    SUCCESS = "success"
    DARK = "dark"


class FlashMessage(NamedTuple):
    text: str = ""
    category: str = MessageCategory.INFO


