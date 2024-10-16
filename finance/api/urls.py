from django.urls import path

from api.views.user import CreateListUsersView, GetPutDeleteUserView

urlpatterns = [

    # User
    path('users/', CreateListUsersView.as_view()),
    path('user/<int:id>/', GetPutDeleteUserView.as_view()),

]
