from rest_framework import serializers
from loan.models import User,Provider,Bank_personnel,Customer,Loan 
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render, redirect




#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  username = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'type')
    

#   validate the password correction  
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  
# create a user object
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
        type=validated_data['type']     
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
  
class RegisterProvider(serializers.ModelSerializer):

  class Meta:
    model= Provider
    fields = ('user','name', 'total_budget','bank_personnel')

# create a Provider object

    def create(self,validated_data):
        provider = Provider.objects.create(
        user=validated_data['user'] ,
        email=validated_data['email'],
        bank_personnel=validated_data['bank_personnel'],

        total_budget=validated_data['total_budget']     
        )
        provider.save()
        
        return provider
    

class RegisterPersonnel(serializers.ModelSerializer):

  class Meta:
    model= Bank_personnel
    fields = ('user','name')

# create a Provider object

    def create(self,validated_data):
        bank_personnel = Bank_personnel.objects.create(
        user=validated_data['user'] ,
        type=validated_data['name']     
        )
        bank_personnel.save()
        
        return bank_personnel    
    

class RegisterCustomer(serializers.ModelSerializer):

  class Meta:
    model= Customer
    fields = ('user','name','id','age','job')

# create a Provider object
    def get_queryset(self, *args, **kwargs):
      user = User.objects.filter(uuid=self.kwargs["uuid"]).first()
    
      return user  
    def create(self,validated_data):
        customer = Customer.objects.create(
        user=validated_data['user'] ,
        name=validated_data['name'],
        id=validated_data['id'],     
        age=validated_data['age'],     
        job=validated_data['job'], 
        )
        customer.save()
        
        return customer        
    
class LoanDetail(serializers.ModelSerializer):
  # bank_personnel = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(uuid=request.user.uuid).first())

  class Meta:
    model=Loan
    fields = ('min_amount','max_amount','max_duration','interest_rate')

# create a Provider object
    # def get_queryset(self, obj):
    #     author = self.context["author"]
    def create(self,validated_data,):
        # print(self.context[''])
        loan = Loan.objects.create(
        bank_personnel=self.context['user'],
        min_amount=validated_data['min_amount'],
        max_amount=validated_data['max_amount'],     
        max_duration=validated_data['max_duration'],     
        interest_rate=validated_data['interest_rate'], 
        )
        loan.save()
        
        
        return loan            