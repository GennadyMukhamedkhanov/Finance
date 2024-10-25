from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.transaction.list import TransactionSerializer
from api.services.transaction.create import CreateTransactionService
from api.services.transaction.delete import DeleteTransactionService
from api.services.transaction.get import GetTransactionService
from api.services.transaction.list import ListTransactionsService
from api.services.transaction.put import PutTransactionService


class CreateListTransactionsView(APIView):

    def get(self, request):
        self.permission_classes = [IsAuthenticated, ]
        self.check_permissions(request)
        outcome = ListTransactionsService.execute({})
        return Response(TransactionSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        CreateTransactionService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)


class GetPutDeleteTransactionsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, **kwargs):
        outcome = GetTransactionService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
            }
        )
        return Response(TransactionSerializer(outcome.result).data, status=status.HTTP_200_OK)

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

    def delete(self, request, **kwargs):
        DeleteTransactionService.execute(
            {
                'id': kwargs.get('id'),
                'user_id': request.user.id,
            }
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
