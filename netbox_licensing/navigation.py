from django.conf import settings
from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

# compatibility with netbox v3.3 that does not have PluginMenu
try:
    from extras.plugins import PluginMenu
    HAVE_MENU = True
except ImportError:
    HAVE_MENU = False
    PluginMenu = PluginMenuItem


menu_buttons = (
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

# can't use utils.get_plugin_setting() here, get value manually
if (HAVE_MENU and settings.PLUGINS_CONFIG['netbox_licensing']['top_level_menu']):
    # add a top level entry
    menu = PluginMenu(
        label=f'Licensing',
        groups=(
            ('Licensing Management', menu_buttons),
        ),
        icon_class='mdi mdi-clipboard-text-multiple-outline'
    )
else:
    # display under plugins
    menu_items = menu_buttons
