from django.urls import path
from .views import  *

urlpatterns = [
    path('movies/', MovieList.as_view(), name='MovieList'),
    path('collection/', ColectionView.as_view(), name='ColectionView'),
    path('collection/<int:id>/', ColectionUpdateView.as_view(), name='ColectionView'),
    path('request-count/', CounterView.as_view(), name='ColectionView'),
    path('registration/', UserRegistrationView.as_view(), name='UserRegistrationView'),
    # path('token/', TokenView.as_view(), name='UserRegistrationView'),
    
    
    # path('file_upload/', FileUploadView.as_view(), name='function_based_view_and_query_param'),
]