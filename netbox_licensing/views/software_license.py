from netbox.views import generic
from netbox_licensing import filtersets, forms, tables
from netbox_licensing.models import SoftwareLicense


class SoftwareLicenseListView(generic.ObjectListView):
    """View for listing all existing SoftwareLicenses."""

    queryset = SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    filterset_form = forms.SoftwareLicenseFilterForm
    table = tables.SoftwareLicenseTable


class SoftwareLicenseView(generic.ObjectView):
    """Display SoftwareLicense details"""

    queryset = SoftwareLicense.objects.all()


class SoftwareLicenseEditView(generic.ObjectEditView):
    """View for editing and creating a SoftwareLicense instance."""

    queryset = SoftwareLicense.objects.all()
    form = forms.SoftwareLicenseForm


class SoftwareLicenseDeleteView(generic.ObjectDeleteView):
    """View for deleting a SoftwareLicense instance"""

    queryset = SoftwareLicense.objects.all()


class SoftwareLicenseBulkImportView(generic.BulkImportView):
    queryset = SoftwareLicense.objects.all()
    model_form = forms.SoftwareLicenseImportForm
    table = tables.SoftwareLicenseTable


class SoftwareLicenseBulkEditView(generic.BulkEditView):
    queryset = SoftwareLicense.objects.all()
    filterset = filtersets.SoftwareLicenseFilterSet
    table = tables.SoftwareLicenseTable
    form = forms.SoftwareLicenseBulkEditForm


class SoftwareLicenseBulkDeleteView(generic.BulkDeleteView):
    queryset = SoftwareLicense.objects.all()
    table = tables.SoftwareLicenseTable
