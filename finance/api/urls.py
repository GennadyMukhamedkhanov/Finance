from django.urls import path

from api.views.transaction import CreateListTransactionsView, GetPutDeleteTransactionsView
from api.views.user import CreateListUsersView, GetPutDeleteUserView

urlpatterns = [

    # User
    path('users/', CreateListUsersView.as_view()),
    path('user/<int:id>/', GetPutDeleteUserView.as_view()),

    # Transaction
    path('transactions/', CreateListTransactionsView.as_view()),
    path('transactions/<int:id>/', GetPutDeleteTransactionsView.as_view()),

]
