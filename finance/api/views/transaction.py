from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.transaction.list import TransactionSerializer
from api.services.transaction.create import CreateTransactionService
from api.services.transaction.delete import DeleteTransactionService
from api.services.transaction.get import GetTransactionService
from api.services.transaction.list import ListTransactionsService
from api.services.transaction.put import PutTransactionService
from api.services.user.delete import DeleteUserService


class CreateListTransactionsView(APIView):

    def get(self, request):
        outcome = ListTransactionsService.execute({})
        return Response(TransactionSerializer(outcome.result, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        CreateTransactionService.execute(request.data)
        return Response(status=status.HTTP_201_CREATED)


class GetPutDeleteTransactionsView(APIView):

    def get(self, request, **kwargs):
        outcome = GetTransactionService.execute(kwargs)
        return Response(TransactionSerializer(outcome.result).data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        outcome = PutTransactionService.execute(
            {
                'id': kwargs.get('id'),
                'user': request.data.get('user'),
                'amount': request.data.get('amount'),
                'date': request.data.get('date'),
                'type': request.data.get('type'),
                'category': request.data.get('category'),
            }
        )
        return Response(TransactionSerializer(outcome.result).data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        DeleteTransactionService.execute(kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
