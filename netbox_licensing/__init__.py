from extras.plugins import PluginConfig

__version__ = "0.0"


class LicensingConfig(PluginConfig):
    name = "netbox_licensing"
    verbose_name = "Software Licensing Management"
    description = "Software Licensing Management Netbox Plugin."
    version = __version__
    author = "Peter Kropf"
    author_email = "pkropf@pm.me"
    base_url = "licensing"
    required_settings = []
    default_settings = {"version_info": False}


config = LicensingConfig
