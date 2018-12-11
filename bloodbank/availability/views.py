from django.shortcuts import render,get_object_or_404
from .models import BloodAvailability
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import BloodAvailabilitySerializer

# Create your views here.

def index(request):
    quantity = BloodAvailability.objects.all()
    context = {
        'quantity': quantity
    }
    return render(request, 'availability/index.html', context)


class BloodAvailabilityList(APIView):

    def get(self, request):
        blood = BloodAvailability.objects.all()
        serializer = BloodAvailabilitySerializer(blood, many=True)
        return Response(serializer.data)

    def post(self):
        pass