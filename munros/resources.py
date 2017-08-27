from tastypie.resources import ModelResource
from munros.models import Mountain
# from tastypie.authorization import ReadOnlyAuthorization


class MountainResource(ModelResource):
  class Meta:
    queryset= Mountain.objects.all()
    resource_name = 'mountain'
    # authorization = ReadOnlyAuthorization()
