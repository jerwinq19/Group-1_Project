from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, views, status
from rest_framework.response import Response

class LogoutView(views.APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({"message": "Please enter a valid token."})
        token = RefreshToken(refresh_token)
        token.blacklist()        
        return Response({"message": "You account has been logout."})