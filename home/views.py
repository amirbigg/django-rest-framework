from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


class Home(APIView):
	def get(self, request):
		persons = Person.objects.get(name='amir')
		ser_data = PersonSerializer(instance=persons)
		return Response(data=ser_data.data)

