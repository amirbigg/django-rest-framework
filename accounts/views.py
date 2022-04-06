from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer


class UserRegister(APIView):
	def post(self, request):
		ser_data = UserRegisterSerializer(data=request.POST)
		if ser_data.is_valid():
			ser_data.create(ser_data.validated_data)
			return Response(ser_data.data)
		return Response(ser_data.errors)
