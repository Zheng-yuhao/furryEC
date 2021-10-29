from rest_framework.pagination import PageNumberPagination


class CoursePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 10