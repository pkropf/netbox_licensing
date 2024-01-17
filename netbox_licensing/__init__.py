from extras.plugins import PluginConfig

__version__ = "1.5"


class SLMConfig(PluginConfig):
    name = "netbox_licensing"
    verbose_name = "Software Licensing Management"
    description = "Software Licensing Management Netbox Plugin."
    version = __version__
    author = "ICTU"
    author_email = "pkropf@Pm.me"
    base_url = "licensing"
    required_settings = []
    default_settings = {"version_info": False}


config = LicensingConfig
