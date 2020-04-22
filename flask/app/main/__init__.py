from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


"""
All variables and functions that should be seen in all templates by default
are defined below.
Although it says @main. in the decorator it works for other blueprints as well.
"""


@main.app_context_processor
def inject_variables():
    _variables_dict = {
        "task2bootstrap": {
            "PENDING": "default",
            "PROGRESS": "primary",
            "SUCCESS": "success",
            "FAILURE": "danger"
        },
        "job2bootstrap": {
            "UNKNOWN": "default",
            "CREATED": "primary",
            "DONE": "success",
            "FAILED": "danger"
        },
        "news2bootstrap": {
            "LOW": "default",
            "NORMAL": "info",
            "HIGH": "primary"
        },
        "default_status_refresh": 2000,
        "default_moment_format": "YYYY-MM-DD HH:mm:ss",
    }
    return _variables_dict


@main.app_context_processor
def inject_methods():
    def format_number(n, fmt=".1f", default="-") -> str:
        try:
            return "{:{fmt}}".format(n, fmt=fmt)
        except (TypeError, ValueError):
            return default

    def build_email_link(to: str = "", subject: str = "", body: str = "") -> str:

        def parse_text(text: str) -> str:
            return text.replace(" ", "%20").replace("\n", "%0D%0A")

        _link = f"mailto:{to}?subject={parse_text(subject)}&body={parse_text(body)}"
        return _link
    return dict(format_number=format_number, build_email_link=build_email_link)
