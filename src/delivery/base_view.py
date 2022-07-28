from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class BaseView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
