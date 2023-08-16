from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    RegisterSerializer,
    RegisterProvider,
    RegisterPersonnel,
    RegisterCustomer,
    LoanDetail,
    loansSerializer,
    loansCoustmerSerializer,
    Paymentserializer,
    LoginSerializer,
)
from loan.models import User, Loan, Bank_personnel, Provider, Customer
from django.contrib.auth import login
from loan.permissions import IsPersonnel, IsProvider, IsCustomer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout


# view function to Register User
class RegisterUserAPIView(generics.CreateAPIView):
    """
    Post a User
    """

    permission_classes = (AllowAny,)

    serializer_class = RegisterSerializer


# view function to login User
class LoginView(views.APIView):
    """
    login User
    """

    # This view should be accessible also for unauthenticated users.
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request, format=None):
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            user.backend = "django.contrib.auth.backends.ModelBackend"

            login(
                request,
                user,
            )

            print(request.user.uuid)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class UserLogout(APIView):
    """
    logout a user
    """

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


# view function to Register Provider
class RegisterProviderAPIView(generics.CreateAPIView):
    """
    Post a Provider
    """

    permission_classes = (IsProvider,)
    serializer_class = RegisterProvider

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# view function to Register Customer


class RegisterCustomerAPIView(generics.CreateAPIView):
    """
    Post a Customer
    """

    permission_classes = (IsCustomer,)
    serializer_class = RegisterCustomer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# view function to Register Bank Personnel
class RegisterPersonnelAPIView(generics.CreateAPIView):
    """
    Post a Bank Personnel data
    """

    permission_classes = (IsPersonnel,)
    lookup_field = "uuid"
    serializer_class = RegisterPersonnel

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# view function to Register each loan rules by the bank provider
@api_view(["POST"])
@permission_classes(
    [
        IsPersonnel,
    ]
)
def loan_Personeldetail(request):
    """
    Post Bank Personnel loan detail.
    """
    user = User.objects.filter(uuid=request.user.uuid).first()
    user = Bank_personnel.objects.get(user=user)
    if request.method == "POST":
        serializer = LoanDetail(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view function to view and delete all the loans provided a loan provider
@api_view(["GET", "DELETE"])
@permission_classes(
    [
        IsProvider,
    ]
)
def viewloanAPIView(request):
    """
    get or delete a Loan provider.
    """
    try:
        print(request.user)
        user = User.objects.get(uuid=request.user.uuid)
        provider = Provider.objects.get(user=user)

        loans = Loan.objects.filter(provider=provider)

    except provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = loansSerializer(loans, many=True)
        print()

        return Response(serializer.data)


# view function to view all the loans of a coustmer
@api_view(["GET"])
@permission_classes(
    [
        IsCustomer,
    ]
)
def viewCoustmerAPIView(request):
    """
    get loans of a Customer
    """
    try:
        coustmer = None

        user = User.objects.get(uuid=request.user.uuid)

        coustmer = Customer.objects.get(user=user)
        loans = Loan.objects.filter(coustmer=coustmer)
    except coustmer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = loansCoustmerSerializer(loans, many=True)
        return Response(serializer.data)


# view function to Register each loan rules
@api_view(["GET", "PATCH"])
@permission_classes(
    [
        IsCustomer,
    ]
)
def loan_Coustmedetail(request, id):
    """
    get and patch loan by coustmer
    """

    loans = Loan.objects.get(id=id)

    if request.method == "PATCH":
        instance = loans
        data = {
            "start_date": request.POST.get("start_date"),
            "total_amount": request.POST.get("total_amount"),
            "duration": request.POST.get("duration"),
        }
        serializer = loansSerializer(
            instance=instance, data=request.data, partial=True, context={"id": id}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = loansSerializer(loans)
        return Response(serializer.data)


@api_view(["POST"])
@permission_classes(
    [
        IsCustomer,
    ]
)
def PaymentApi(request, id):
    """
    Post a Payment
    """
    loans = Loan.objects.get(id=id)

    if request.method == "POST":
        serializer = Paymentserializer(loans, data=request.data, context={"id": id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
