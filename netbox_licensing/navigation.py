from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_licensing:softwareproduct_list",
        link_text="Software Products",
        buttons=(
            PluginMenuButton(
                "plugins:netbox_licensing:softwareproduct_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_licensing.add_softwareproduct"],
            ),
            PluginMenuButton(
                "plugins:netbox_licensing:softwareproduct_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_licensing.add_softwareproduct"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_licensing:softwareproductversion_list",
        link_text="Versions",
        buttons=(
            PluginMenuButton(
                "plugins:netbox_licensing:softwareproductversion_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_licensing.add_softwareproductversion"],
            ),
            PluginMenuButton(
                "plugins:netbox_licensing:softwareproductversion_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_licensing.add_softwareproductversion"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_licensing:softwareproductinstallation_list",
        link_text="Installations",
        buttons=(
            PluginMenuButton(
                "plugins:netbox_licensing:softwareproductinstallation_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_licensing.add_softwareproductinstallation"],
            ),
            PluginMenuButton(
                "plugins:netbox_licensing:softwareproductinstallation_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_licensing.add_softwareproductinstallation"],
            ),
        ),
    ),
    PluginMenuItem(
        link="plugins:netbox_licensing:softwarelicense_list",
        link_text="Licenses",
        buttons=(
            PluginMenuButton(
                "plugins:netbox_licensing:softwarelicense_add",
                "Add",
                "mdi mdi-plus-thick",
                ButtonColorChoices.GREEN,
                permissions=["netbox_licensing.add_softwarelicense"],
            ),
            PluginMenuButton(
                "plugins:netbox_licensing:softwarelicense_import",
                "Import",
                "mdi mdi-upload",
                ButtonColorChoices.CYAN,
                permissions=["netbox_licensing.add_softwarelicense"],
            ),
        ),
    ),
)
