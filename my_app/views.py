from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.generics import RetrieveAPIView

from .forms import EmployeeForm
from .models import Employee, Position, Article
from .serializers import EmployeeSerializer, PositionSerializer, UserSerializer, ArticleSerializer, ConferenceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout


def myView(request):
    username = None
    if request.user:
        username = request.user.username
        print('**********' + request.user.username)
    return HttpResponse('Hello world! ' + username)


class UserView(RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request):
        # If provided 'pk' is "me" then return the current user.
        if request.user:
            return Response(UserSerializer(request.user).data)
        return super(UserView, self).retrieve(request)


# generic get all employees view
class GenericEmployeeAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request):
        return self.list(request)


# class based  get all employee view example
class EmployeeAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(list(employees), many=True)
        return Response(serializer.data)


# function based get all employee view example
@api_view(['GET'])
def employeelist(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


# generic based post employee
class GenericEmployeeAddAPIView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def post(self, request):
        return self.create(request)


# class based post employee
class EmployeeAddAPIView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# function based put employee update
@api_view(['POST'])
def employee_add(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# generic based employee detail view
class GenericEmployeeDetail(generics.GenericAPIView, mixins.ListModelMixin,
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# class based employee detail view
class EmployeeDetail(APIView):
    def get_object(self, id):
        try:
            return Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = self.get_object(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# function based employee detail view
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pkid):
    try:
        employee = Employee.objects.get(pk=pkid)
    except Employee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    print(context)
    return render(request, "my_app/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        # to register employee
        if id == 0:
            form = EmployeeForm()
        else:  # to edit employee
            employee_instance = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee_instance)
        return render(request, "my_app/employee_form.html", {'form': form})
    else:  # post request
        if id == 0:  # to save form
            form = EmployeeForm(request.POST)
        else:  # to save updated form
            employee_instance = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee_instance)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


# delete the employee
def employee_delete(request, id):
    employee_instance = Employee.objects.get(pk=id)
    employee_instance.delete()
    return redirect('/employee/list')


# class based  get all employee view example
class ArticleCreate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConferenceCreate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ConferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericArticleCreate(generics.GenericAPIView, mixins.CreateModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def post(self, request):
        return self.create(request)
