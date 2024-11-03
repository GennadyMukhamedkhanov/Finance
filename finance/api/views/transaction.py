from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

from api.docs.transaction import (TRANSACTION_LIST_VIEW, TRANSACTION_CREATE_VIEW,
                                  TRANSACTION_GET_VIEW, TRANSACTION_PUT_VIEW, TRANSACTION_DELETE_VIEW)
from api.serializers.transaction.list import TransactionSerializer
from api.services.transaction.create import CreateTransactionService
from api.services.transaction.delete import DeleteTransactionService
from api.services.transaction.get import GetTransactionService
from api.services.transaction.list import ListTransactionsService
from api.services.transaction.put import PutTransactionService


class CreateListTransactionsView(APIView):
    @swagger_auto_schema(**TRANSACTION_LIST_VIEW)
    def get(self, request):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)

        page_size = request.query_params.get('page_size')
        pagination = PageNumberPagination()
        if page_size and int(page_size) > 0:
            pagination.page_size = page_size
        outcome = ListTransactionsService.execute({})
        paginate_queryset = pagination.paginate_queryset(outcome.result, request)
        return Response(TransactionSerializer(paginate_queryset, many=True).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**TRANSACTION_CREATE_VIEW)
    def post(self, request):
        CreateTransactionService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)


class GetPutDeleteTransactionsView(APIView):
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(**TRANSACTION_GET_VIEW)
    def get(self, request, **kwargs):
        outcome = GetTransactionService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
            }
        )
        return Response(TransactionSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**TRANSACTION_PUT_VIEW)
    def put(self, request, **kwargs):
        outcome = PutTransactionService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
                'user': request.data.get('user'),
                'amount': request.data.get('amount'),
                'date': request.data.get('date'),
                'type': request.data.get('type'),
                'category': request.data.get('category'),
            }
        )
        return Response(TransactionSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**TRANSACTION_DELETE_VIEW)
    def delete(self, request, **kwargs):
        DeleteTransactionService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
            }
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
