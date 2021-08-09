from django.urls import path, include
from . import views
from rest_framework import routers


#urlpatterns = [
#    path("", views.apiOverview, name="api_overview")
#]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from softdesk import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contributors', views.ContributorViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'comments', views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]