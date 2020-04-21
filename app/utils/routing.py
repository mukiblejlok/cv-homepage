from flask import request, url_for


def get_next_page(argument_name: str = "next", default_view: str = "main.index"):
    """
    It returns a path to next page that the view should redirect to after doing it's job.
    :param argument_name: name of argument in request that defines the page to redirect to. (default="next")
    :param default_view: name of default view function that defines the default goto page. (default="main.index)
    :return: path to redirect page.
    """
    next_page = request.args.get(argument_name)
    if next_page is None or not next_page.startswith('/'):
        next_page = url_for(default_view)
    return next_page

