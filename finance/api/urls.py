from django.urls import path

from api.views.transaction import CreateListTransactionsView, GetPutDeleteTransactionsView
from api.views.user import CreateListUsersView, GetPutDeleteUserView

urlpatterns = [

    # User
    path('users/', CreateListUsersView.as_view(), name='create_list_users'),
    path('user/<int:id>/', GetPutDeleteUserView.as_view()),

    # Transaction
    path('transactions/', CreateListTransactionsView.as_view()),
    path('transaction/<int:id>/', GetPutDeleteTransactionsView.as_view()),


]
