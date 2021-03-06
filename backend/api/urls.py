from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

from api.views.auth import SignUpView
from api.views.auth import SignUpVerificationView
from api.views.auth import SignUpWithFacebookView
from api.views.auth import CurrentUserView
from api.views.auth import CurrentUserAvatarUploadView
from api.views.auth import UpdatePasswordView
from api.views.donors import DonorFrontListView
from api.views.donors import DonorListView
from api.views.donors import DonorDetailView
from api.views.jobs import JobListView
from api.views.jobs import JobDetailView
from api.views.auctions import AccountBidDetailView
from api.views.auctions import AccountBidListView
from api.views.auctions import AuctionDetailView
from api.views.auctions import AuctionFrontListView
from api.views.auctions import AuctionListView
from api.views.auctions import AuctionPlaceBidView
from api.views.blog import PostFrontListView
from api.views.blog import PostListView
from api.views.blog import PostDetailView
from api.views.blog import PostCommentListView
from api.views.settings import CountriesView
from api.views.payment import AccountPaymentView
from api.views.payment import PaymentTestView
# temporary endpoint for testing
from api.views.test import TestView


urlpatterns = [
    url(r'^signin/$', obtain_jwt_token, name='signin'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^verify-signup/$', SignUpVerificationView.as_view(), name='verify-signup'),
    url(r'^signup-with-facebook/$', SignUpWithFacebookView.as_view(), name='signup-with-facebook'),
    url(r'^current-user/$', CurrentUserView.as_view(), name='current-user'),
    url(r'^current-user/avatar/$', CurrentUserAvatarUploadView.as_view(), name='current-user-avatar'),
    url(r'^current-user/update-password/$', UpdatePasswordView.as_view(), name='current-user-update-password'),
    url(r'^test/$', TestView.as_view()),

    url(r'^donors/front/$', DonorFrontListView.as_view(), name='donor-front-list'),
    url(r'^donors/$', DonorListView.as_view(), name='donor-list'),
    url(r'^donors/(?P<pk>[0-9]+)/$', DonorDetailView.as_view(), name='donor-detail'),

    url(r'^jobs/$', JobListView.as_view(), name='job-list'),
    url(r'^jobs/(?P<pk>[0-9]+)/$', JobDetailView.as_view(), name='job-detail'),
    url(r'^auctions/front/$', AuctionFrontListView.as_view(), name='auction-front-list'),
    url(r'^auctions/$', AuctionListView.as_view(), name='auction-list'),
    url(r'^auctions/(?P<pk>[0-9]+)/$', AuctionDetailView.as_view(), name='auction-detail'),
    url(r'^auctions/(?P<pk>[0-9]+)/bid/$', AuctionPlaceBidView.as_view(), name='auction-place-bid'),

    url(r'^posts/front/$', PostFrontListView.as_view(), name='posts-front-list'),
    url(r'^posts/$', PostListView.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^posts/(?P<pk>[0-9]+)/comments/$', PostCommentListView.as_view(), name='post-comments'),

    url(r'^account/bids/$', AccountBidListView.as_view(), name='account-bid-list'),
    url(r'^account/bids/(?P<pk>[0-9]+)/$', AccountBidDetailView.as_view(), name='account-bid-detail'),
    url(r'^account/payment/$', AccountPaymentView.as_view(), name='account-payment'),

    url(r'^payment-test/$', PaymentTestView.as_view(), name='payment-test'),

    url(r'^settings/countries$', CountriesView.as_view(), name='settings-countries'),

    url(r'^admin/', include('api.views.admin.urls', namespace='admin')),
]
