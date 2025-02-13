from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from netbox_licensing.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation, SoftwareLicense


class SoftwareProductSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_licensing-api:softwareproduct-detail")

    class Meta:
        model = SoftwareProduct
        fields = [
            "id",
            "display",
            "url",
            "name",
            "tags",
            "custom_field_data",
            "created",
            "last_updated",
        ]

    def get_display(self, obj):
        return f"{obj.manufacturer} - {obj}"


class SoftwareProductVersionSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_licensing-api:softwareproductversion-detail")

    class Meta:
        model = SoftwareProductVersion
        fields = [
            "id",
            "display",
            "url",
            "name",
            "software_product",
            "tags",
            "custom_field_data",
            "created",
            "last_updated",
        ]

    def get_display(self, obj):
        return f"{obj}"


class SoftwareProductInstallationSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_licensing-api:softwareproductinstallation-detail"
    )

    class Meta:
        model = SoftwareProductInstallation
        fields = [
            "id",
            "display",
            "url",
            "device",
            "virtualmachine",
            "cluster",
            "software_product",
            "version",
            "tags",
            "custom_field_data",
            "created",
            "last_updated",
        ]

    def get_display(self, obj):
        return f"{obj}"


class SoftwareLicenseSerializer(NetBoxModelSerializer):
    display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:netbox_licensing-api:softwarelicense-detail")

    class Meta:
        model = SoftwareLicense
        fields = [
            "id",
            "display",
            "url",
            "name",
            "description",
            "type",
            "stored_location",
            "start_date",
            "expiration_date",
            "software_product",
            "version",
            "installation",
            "tags",
            "custom_field_data",
            "created",
            "last_updated",
        ]

    def get_display(self, obj):
        return f"{obj}"
