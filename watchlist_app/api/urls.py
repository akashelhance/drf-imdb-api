from django.urls import path,include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail


urlpatterns = [

    path('list/',WatchListAV.as_view(),  name="watch_list" ),
    path('<int:pk>', WatchDetailAV.as_view(), name="movie_detail"),
    path('stream/',StreamPlatformAV.as_view(),  name="stream" ),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),  name="stream_detail" ),
    
    
    path('stream/<int:pk>/review',StreamPlatformDetailAV.as_view(), name="review" ),
    path('stream/review/<int:pk>',ReviewDetail.as_view(), name="review-detail" ),
]
