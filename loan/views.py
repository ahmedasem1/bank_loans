from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,RegisterProvider,RegisterPersonnel,RegisterCustomer,LoanDetail
from loan.models import User,Loan,Bank_personnel
from rest_framework.authentication import TokenAuthentication 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model




#view function to Register User

class RegisterUserAPIView(generics.CreateAPIView):
#   control premmision
  permission_classes = (AllowAny,)

  serializer_class = RegisterSerializer

class RegisterProviderAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  lookup_field = "uuid"
  serializer_class = RegisterProvider

  def get_queryset(self, *args, **kwargs):
    user = User.objects.filter(uuid=self.kwargs["uuid"]).first()

    
    return user
  

class RegisterCustomerAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  lookup_field = "uuid"
  serializer_class = RegisterCustomer

  def get_queryset(self, *args, **kwargs):
    user = User.objects.filter(uuid=self.kwargs["uuid"]).first()
    return user  
  
class RegisterPersonnelAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  lookup_field = "uuid"
  serializer_class = RegisterPersonnel

  def get_queryset(self, *args, **kwargs):
    user = User.objects.filter(uuid=self.kwargs["uuid"]).first()
    # serializer.save(user)

    return user    
  
class loan_detail(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  # lookup_field = "uuid"
  serializer_class = LoanDetail
  def post(self, request):
        print("llllllllllllllllllllllllllll")
        print(self.request.user)
        user=User.objects.filter(uuid=self.user.uuid).first()
        print("llllllllllllllllllllllllllll")
        print(user)
        user=Bank_personnel.filter(user=user).first()
        

        serializer = LoanDetail(data=request.data,context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  # def get_queryset(self,request, *args, **kwargs):
  #   # try:
  #   user = User.objects.filter(uuid=request.user.uuid).first()
  #   print("opppppppppppppppppppppppp")
  #   print(user)
  #   LoanDetail(Loan,context={'user': user})

  #   # except user.DoesNotExist:
  #   #   return Response(status=status.HTTP_404_NOT_FOUND)
  #   return user    
  # def create(self, request, *args, **kwargs):
  #   serializer = self.get_serializer(data=request.data)
  #   serializer.is_valid(raise_exception=True)
  #   self.perform_create(serializer)
  #   headers = self.get_success_headers(serializer.data)
  #   return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

# @api_view(['GET','POST'])
# def loan_detail(request, acc_uuid):
#     """
#     Retrieve, update or delete a proudct.
#     """
#     try:
#         user = User.objects.filter(uuid=request.user.uuid).first()
#     except user.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = LoanDetail(Loan)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = LoanDetail(Loan,context={'user': user})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 