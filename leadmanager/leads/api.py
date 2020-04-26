from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset(viewset allows to create full CRUD api)
class LeadViewset(viewsets.ModelViewSet):
  permission_classes = [
      permissions.IsAuthenticated
  ]
  serializer_class = LeadSerializer

  def get_queryset(self):
    self.request.user.leads.all()

  def perform_create(self, serializer):
    # serializer is positinal argument
    serializer.save(owner=self.request.user)
