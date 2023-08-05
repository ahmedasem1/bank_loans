from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,RegisterProvider,RegisterPersonnel,RegisterCustomer,LoanDetail,loansSerializer,loansCoustmerSerializer
from loan.models import User,Loan,Bank_personnel,Provider,Customer
from loan.permissions import IsPersonnelOrReadOnly

from rest_framework.authentication import TokenAuthentication 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status,mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.decorators import  permission_required



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

@api_view(['POST'])
# @permission_required('loan.IsPersonnelOrReadOnly', raise_exception=True)
def loan_Personeldetail(request, uuid):
      user=User.objects.filter(uuid=uuid).first()
      user=Bank_personnel.objects.get(user=user)     
      if request.method == 'POST':

        serializer = LoanDetail(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def viewloanAPIView(request, uuid):
    """
    Retrieve, update or delete a proudct.
    """
    try:
        user = User.objects.get(uuid=uuid)
        provider = Provider.objects.get(user=user)

        loans = Loan.objects.get(provider=provider)



    except provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = loansSerializer(loans)
        return Response(serializer.data)
    
@api_view(['GET'])
def viewCoustmerAPIView(request, uuid):
    try:
        coustmer=None
        
        user = User.objects.get(uuid=uuid)
        print(user)


        coustmer = Customer.objects.get(user=user)
        loans = Loan.objects.filter(coustmer=coustmer)
    except coustmer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = loansCoustmerSerializer(loans,many=True)
        return Response(serializer.data)    
    
# class loan_Coustmedetail(mixins.UpdateModelMixin):
#     queryset = Loan.objects.all()
#     serializer_class = LoanCoustmer
#     http_method_names=["patch"]
@api_view(['GET','PATCH'])
# @permission_required('loan.IsPersonnelOrReadOnly', raise_exception=True)
def loan_Coustmedetail(request,id):
        
      
      loans = Loan.objects.get(id=id)   

      if request.method == 'PATCH':
        instance = loans
        data = {
            "start_date": request.POST.get('start_date'),
            "total_amount": request.POST.get('total_amount'),
            "duration": request.POST.get('duration'),

            }
        serializer = loansSerializer(instance=instance,data=request.data ,partial=True,context={'id': id})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      if request.method == 'GET':

        serializer = loansSerializer(loans)
        return Response(serializer.data)
      