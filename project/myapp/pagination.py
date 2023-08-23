from rest_framework import pagination
from rest_framework.response import Response

'''
class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
             },
            'count':self.paginator.count,
            'data':data
     })
'''

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = self.get_page_size(request)
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
             },
            'count':self.page.paginator.count,
            'data':data
        })