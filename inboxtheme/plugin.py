"""
Plugin definition for the inboxtheme OPAL plugin
"""
from opal.core import plugins

from inboxtheme.urls import urlpatterns

class InboxthemePlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.inboxtheme': [
            # 'js/inboxtheme/app.js',
            # 'js/inboxtheme/controllers/larry.js',
            # 'js/inboxtheme/services/larry.js',
        ]
    }
    stylesheets = [
        'css/inbox.css'
    ]

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}
