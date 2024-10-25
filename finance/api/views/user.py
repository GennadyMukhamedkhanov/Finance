from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.serializers.user.list import UserSerializer
from api.services.user.create import CreateUsersService
from api.services.user.delete import DeleteUserService
from api.services.user.get import GetUserService
from api.services.user.list import ListUsersService
from api.services.user.put import PutUserService


class CreateListUsersView(APIView):

    def get(self, request):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)

        outcome = ListUsersService.execute({})
        return Response(UserSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        CreateUsersService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)


class GetPutDeleteUserView(APIView):

    def get(self, request, **kwargs):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)
        outcome = GetUserService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
            }
        )
        return Response(UserSerializer(outcome.result).data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)
        outcome = PutUserService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
                'email': request.data.get('email'),
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'username': request.data.get('username'),
                'password': request.data.get('password'),
            }
        )
        return Response(UserSerializer(outcome.result).data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)
        DeleteUserService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
            }
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
