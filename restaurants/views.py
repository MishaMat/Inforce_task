from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class RestaurantListView(ListAPIView):
    """Represents Restaurant List Class View"""
    queryset = RestaurantModel.objects.all()
    serializer_class = RestaurantListSerializer


class MenuListView(ListAPIView):
    """Represents Menu List Class View"""
    queryset = MenuModel.objects.all()
    serializer_class = MenuListSerializer


class CreateRestaurantView(APIView):
    """
    Class for creating Restaurants
    only staff user can do this
        params for post:
            - name
            - rating
            - contact_no
            - address
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if not request.user.is_staff:
            return Response(data={'message': 'IsStaff should be True.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = RestaurantListSerializer(data=dict(request.data))
        if serializer.is_valid():
            serializer.save()
            response = {
                'message': 'Restaurant Created Succesfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {"message": str(serializer.errors), "data": None}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserManagerView(APIView):
    """
    Class for Creating Managers
        params in post:
                - username
                - first_name
                - last_name
                - email
                - password
    """

    def post(self, request):
        req = dict(request.data)
        req['is_staff'] = True
        serializer = UserSerializer(data=req)
        if serializer.is_valid() and req.get('password', None):
            serializer.save()
            user = User.objects.filter(username=req['username']).first()
            user.set_password(req['password'])
            user.save()
            response = {
                'message': 'Manager Created Succesfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {"message": str(serializer.errors), "data": None}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class ManagerListView(ListAPIView):
    """Represents Manager List Class View"""
    queryset = User.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = UserSerializer


class CreateEmployeeView(APIView):
    """
    Class for creating Employees
    Only staff users have permissions to do this
        params in post:
                - username
                - first_name
                - last_name
                - email
                - password
                - position
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if not request.user.is_staff:
            return Response(data={'message': 'Only manager or superuser could create employee'},
                            status=status.HTTP_403_FORBIDDEN)
        req = dict(request.data)
        req['is_staff'] = False
        user_serializer = UserSerializer(data=req)
        if user_serializer.is_valid() and req.get('position', None):
            user_serializer.save()
            user = User.objects.filter(username=req['username']).first()
            user.set_password(req['password'])
            user.save()
            id = User.objects.filter(username=req['username']).first().id
            employee = EmployeeSerializer(data={'user': id, 'position': req['position']})
            if employee.is_valid():
                employee.save()
                response = {
                    'message': 'Employee Created Succesfully',
                    'data': employee.data
                }
                return Response(data=response, status=status.HTTP_201_CREATED)
            response = {"message": str(employee.errors), "data": None}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        response = {"message": str(user_serializer.errors), "data": None}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class EmployeeListView(ListAPIView):
    """Represents Employee List Class View"""
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class UserLoginView(APIView):
    """
    Class for authentication and login
        params in post:
                - username
                - password
    """

    def post(self, request):

        if type(request.user).__name__ != 'AnonymousUser':
            return Response(data={'message': 'You are already logged in'}, status=status.HTTP_200_OK)
        req = dict(request.data)
        if req.get('username', None) and req.get('password', None):
            try:
                user = authenticate(username=req['username'],
                                    password=req['password'])
                login(request, user)
                response = {"message": f'Succefully logined as {user.username}', }
                return Response(data=response, status=status.HTTP_200_OK)
            except Exception:
                response = {"message": 'wrong username or password', "data": None}
                return Response(data=response, status=status.HTTP_403_FORBIDDEN)
        response = {"message": 'provide username and password', "data": None}
        return Response(data=response, status=status.HTTP_403_FORBIDDEN)


class UserLogoutView(APIView):
    """ class for log out view"""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        logout(request)
        res = {
            "msg": "User logged out successfully",
            "success": True,
            "data": None}
        return Response(data=res, status=status.HTTP_200_OK)


class CurrentDayMenuList(APIView):
    """
    Class for current day menus
    """

    def get(self, request):
        today_date = datetime.date.today()
        qs = MenuModel.objects.filter(date=today_date)
        serializer = MenuListSerializer(qs, many=True)
        res = {"msg": 'success', "data": serializer.data, "success": True}
        return Response(data=res, status=status.HTTP_200_OK)


class VoteView(APIView):
    """
    Class that realises voting system
      only employee could vote and only once per day
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, menu_id):
        emp = EmployeeModel.objects.filter(user=request.user).first()
        if emp:
            menu = MenuModel.objects.filter(id=menu_id).first()
            if menu:
                # checking if this employee has already voted today
                if VoteModel.objects.filter(employee=emp, voted_at=datetime.date.today()).first():
                    return Response(data={"message": "you have already voted today"}, status=status.HTTP_403_FORBIDDEN)
                VoteModel.objects.create(employee=emp,
                                         menu=menu)
                menu.vote += 1
                menu.save()
                return Response(data={"message": f"Successfully voted for {menu_id} menu"}, status=status.HTTP_200_OK)
            return Response(data={"message": f"Menu with this id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": f"Current user is not employee"}, status=status.HTTP_400_BAD_REQUEST)


class ResultsView(APIView):
    """
    Class that displays the most voted menu(s)
    if there are any voting for current day
    """

    def get(self, request):
        today = datetime.date.today()
        votes = MenuModel.objects.filter(date=today).order_by('-vote').first().vote
        res_query = MenuModel.objects.filter(date=today, vote=votes)
        if res_query:
            serializer = MenuListSerializer(res_query, many=True)
            return Response(data={"message": f"This menu(s) has the most votes", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(data={"message": f"Nobody voted for today menus"}, status=status.HTTP_200_OK)


class UploadMenuView(APIView):
    """Class for uploading new menu to existing restaurant"""
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if not request.user.is_staff:
            return Response(data={'message': 'IsStaff should be True.'}, status=status.HTTP_403_FORBIDDEN)
        req = dict(request.data)
        serializer = MenuListSerializer(data=req)
        if serializer.is_valid():
            if MenuModel.objects.filter(restaurant_id=req['restaurant'], date=datetime.date.today()):
                return Response(data={"message": "you have already uploaded menu for this restaurant today"},
                                status=status.HTTP_200_OK)
            serializer.save()
            response = {
                'message': 'Menu Created Succesfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {"message": str(serializer.errors), "data": None}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
