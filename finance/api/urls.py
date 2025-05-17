from api.views.csv_export import ExportTransactionsCSV
from api.views.transaction import CreateListTransactionsView, GetPutDeleteTransactionsView
from api.views.user import CreateListUsersView, GetPutDeleteUserView
from django.urls import path

urlpatterns = [
    # User
    path("users/", CreateListUsersView.as_view(), name="create_list_users"),
    path("user/<int:id>/", GetPutDeleteUserView.as_view(), name="get_put_delete_user_id"),
    # Transaction
    path("transactions/", CreateListTransactionsView.as_view(), name="create_list_transactions"),
    path("transaction/<int:id>/", GetPutDeleteTransactionsView.as_view(), name="get_put_delete_transaction_id"),
    # CSV export
    path("export/transactions/csv/", ExportTransactionsCSV.as_view(), name="export_transactions_csv"),
]

# DATABASE_URL=postgres://usersup:198616Gm@database:5432/finance_db при запуске docker-compose в .env
# DATABASE_URL=postgres://UserSup:198616Gm@localhost:5432/finance_db
