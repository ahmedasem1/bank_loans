from rest_framework import serializers
from loan.models import Provider, Bank_personnel, Customer, Loan, User
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "type")

    #   validate the password correction
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    # create a user object
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], type=validated_data["type"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class RegisterProvider(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("user", "name", "total_budget", "bank_personnel")

        # create a Provider object

        def create(self, validated_data):
            provider = Provider.objects.create(
                user=validated_data["user"],
                email=validated_data["email"],
                bank_personnel=validated_data["bank_personnel"],
                total_budget=validated_data["total_budget"],
            )
            provider.save()

            return provider


class RegisterPersonnel(serializers.ModelSerializer):
    class Meta:
        model = Bank_personnel
        fields = ("user", "name")

        # create a Provider object

        def create(self, validated_data):
            bank_personnel = Bank_personnel.objects.create(
                user=validated_data["user"], type=validated_data["name"]
            )
            bank_personnel.save()

            return bank_personnel


class RegisterCustomer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("user", "name", "id", "age", "job")

        def create(self, validated_data):
            customer = Customer.objects.create(
                user=validated_data["user"],
                name=validated_data["name"],
                id=validated_data["id"],
                age=validated_data["age"],
                job=validated_data["job"],
            )
            customer.save()

            return customer


class LoanDetail(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = (
            "min_amount",
            "max_amount",
            "max_duration",
            "interest_rate",
            "bank_personnel",
            "provider",
            "coustmer",
        )

        def create(self, validated_data):
            loan = Loan.objects.create(
                bank_personnel=validated_data["bank_personnel"],
                provider=validated_data["provider"],
                min_amount=validated_data["min_amount"],
                max_amount=validated_data["max_amount"],
                max_duration=validated_data["max_duration"],
                interest_rate=validated_data["interest_rate"],
                coustmer=validated_data["coustmer"],
            )
            loan.save()
            return loan


class loansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.total_amount = validated_data.get(
            "total_amount", instance.total_amount
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.id = self.context["id"]

        print(instance.start_date)
        instance.save()
        return instance


class loansCoustmerSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = "__all__"

    def get_status(self, obj):
        max_amount = self.context.get("max_amount")

        if max_amount is not None:
            return obj.status == "Pending"
        else:
            return obj.status == "viewed"
