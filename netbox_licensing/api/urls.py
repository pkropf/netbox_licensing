from netbox.api.routers import NetBoxRouter
from netbox_licensing.api.views import (
    NetboxLicensingRootView,
    SoftwareProductViewSet,
    SoftwareProductVersionViewSet,
    SoftwareProductInstallationViewSet,
    SoftwareLicenseViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetboxLicensingRootView

router.register("softwareproducts", SoftwareProductViewSet)
router.register("softwareproductversions", SoftwareProductVersionViewSet)
router.register("softwareproductinstallations", SoftwareProductInstallationViewSet)
router.register("softwarelicenses", SoftwareLicenseViewSet)
urlpatterns = router.urls
