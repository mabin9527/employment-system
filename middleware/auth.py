from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    """
    Validate user login. If user does not pass the validation of login. All the opreations
    inside the system are not permitted. Then the user will be redirected to login page
    """

    def process_request(self, request):

        if request.path_info == '/login/':
            return

        info_dict = request.session.get('info')
        if info_dict:
            return
        
        return redirect('/login/')
