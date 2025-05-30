from api.docs.user import USER_CREATE_VIEW, USER_DELETE_VIEW, USER_GET_VIEW, USER_LIST_VIEW, USER_PUT_VIEW
from api.serializers.user.list import UserSerializer
from api.services.user.create import CreateUsersService
from api.services.user.delete import DeleteUserService
from api.services.user.get import GetUserService
from api.services.user.list import ListUsersService
from api.services.user.put import PutUserService
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateListUsersView(APIView):
    @swagger_auto_schema(**USER_LIST_VIEW)
    def get(self, request):
        self.permission_classes = [
            IsAuthenticated,
        ]
        self.check_permissions(request)

        page_size = request.query_params.get("page_size")
        pagination = PageNumberPagination()
        if page_size and int(page_size) > 0:
            pagination.page_size = page_size
        outcome = ListUsersService.execute({})
        paginate_queryset = pagination.paginate_queryset(outcome.result, request)
        return Response(UserSerializer(paginate_queryset, many=True).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**USER_CREATE_VIEW)
    def post(self, request):
        CreateUsersService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)


class GetPutDeleteUserView(APIView):
    @swagger_auto_schema(**USER_GET_VIEW)
    def get(self, request, **kwargs):
        self.permission_classes = [
            IsAuthenticated,
        ]
        self.check_permissions(request)
        outcome = GetUserService.execute(
            {
                "id": kwargs.get("id"),
                "user_id": request.user.id,
            }
        )
        return Response(UserSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**USER_PUT_VIEW)
    def put(self, request, **kwargs):
        self.permission_classes = [
            IsAuthenticated,
        ]
        self.check_permissions(request)
        outcome = PutUserService.execute(
            {
                "id": kwargs.get("id"),
                "user_id": request.user.id,
                "email": request.data.get("email"),
                "first_name": request.data.get("first_name"),
                "last_name": request.data.get("last_name"),
                "username": request.data.get("username"),
                "password": request.data.get("password"),
            }
        )
        return Response(UserSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**USER_DELETE_VIEW)
    def delete(self, request, **kwargs):
        self.permission_classes = [
            IsAuthenticated,
        ]
        self.check_permissions(request)
        DeleteUserService.execute(
            {
                "id": kwargs.get("id"),
                "user_id": request.user.id,
            }
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
