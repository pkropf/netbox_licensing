from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet
from netbox_licensing.api.serializers import (
    SoftwareProductSerializer,
    SoftwareProductVersionSerializer,
    SoftwareProductInstallationSerializer,
    SoftwareLicenseSerializer,
)
from netbox_licensing.filtersets import (
    SoftwareProductFilterSet,
    SoftwareProductVersionFilterSet,
    SoftwareProductInstallationFilterSet,
    SoftwareLicenseFilterSet,
)
from netbox_licensing.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense


class NetboxLicensingRootView(APIRootView):
    """
    NetboxLicensing API root view
    """

    def get_view_name(self):
        return "NetboxLicensing"


class SoftwareProductViewSet(NetBoxModelViewSet):
    queryset = SoftwareProduct.objects.all()
    serializer_class = SoftwareProductSerializer
    filterset_class = SoftwareProductFilterSet


class SoftwareProductVersionViewSet(NetBoxModelViewSet):
    queryset = SoftwareProductVersion.objects.all()
    serializer_class = SoftwareProductVersionSerializer
    filterset_class = SoftwareProductVersionFilterSet


class SoftwareProductInstallationViewSet(NetBoxModelViewSet):
    queryset = SoftwareProductInstallation.objects.all()
    serializer_class = SoftwareProductInstallationSerializer
    filterset_class = SoftwareProductInstallationFilterSet


class SoftwareLicenseViewSet(NetBoxModelViewSet):
    queryset = SoftwareLicense.objects.all()
    serializer_class = SoftwareLicenseSerializer
    filterset_class = SoftwareLicenseFilterSet
