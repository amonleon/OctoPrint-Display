
from __future__ import absolute_import

import octoprint.plugin
from octoprint.util import RepeatedTimer


class DisplayPlugin(octoprint.plugin.StartupPlugin,):
    def on_after_startup(self):
        self._logger.info("Hello World")

__plugin_name__ = "Display"
__plugin_version__ = "0.0.1"
__plugin_description__= "A test plugin to use the display on WB2"
__plugin_implementation__=DisplayPlugin()