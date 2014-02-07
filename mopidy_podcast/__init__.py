from __future__ import unicode_literals

from mopidy import config, ext

__version__ = '0.2.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Podcast'
    ext_name = 'podcast'
    version = __version__

    def get_default_config(self):
        import os
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['feed_urls'] = config.List()
        schema['browse_label'] = config.String()
        schema['update_interval'] = config.Integer(minimum=0)
        schema['sort_order'] = config.String(choices=['asc', 'desc'])
        schema['preload'] = config.Deprecated()  # FIXME: remove
        return schema

    def setup(self, registry):
        from .backend import PodcastBackend
        registry.add('backend', PodcastBackend)
