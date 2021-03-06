from __future__ import unicode_literals

import logging

from mopidy import backend

import uritools

logger = logging.getLogger(__name__)


class PodcastPlaybackProvider(backend.PlaybackProvider):

    def translate_uri(self, uri):
        parts = uritools.uridefrag(uri)
        try:
            feed = self.backend.feeds[parts.uri]
        except Exception as e:
            logger.error('Error retrieving %s: %s', parts.uri, e)
        else:
            return feed.getstreamuri(parts.getfragment())
