from tastypie.resources import ModelResource
from munros.models import Mountain
from munros.models import Images

# from tastypie.authorization import ReadOnlyAuthorization


class MountainResource(ModelResource):
  class Meta:
    queryset= Mountain.objects.all()
    resource_name = 'mountain'
    # authorization = ReadOnlyAuthorization()

class ImagesResource(ModelResource):
  class Meta:
     queryset= Images.objects.all()
     resource_name = 'image'