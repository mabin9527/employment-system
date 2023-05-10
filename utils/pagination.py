class Pagination(object):
    """
    Build reusable pagination class
    """

    def __init__(self, request, queryset, page_size=10, page_param='page', plus=5):
        """
        :param request: The requested object
        :param page_size: The amount of data displayed per page
        :param page_param: The page parameters
        :param plus: The number of pages is moved back or moved forward from current page
        """

        page = request.GET.get(page_param, '1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page