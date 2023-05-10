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

        # Calcualte the first and the last data on current page

        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size

        # Obtain the total page by using total number of data divided by the amount of data
        # displayed per page.  If there is a remainder, then total page +1 for showing all 
        # data to user. 

        self.page_queryset = queryset[self.start:self.end]
        total_count = queryset.count()
        total_page_count, remainder = divmod(total_count, page_size)
        if remainder:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):

        # Get the first 5 pages and the last 5 pages of current page

        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
            
