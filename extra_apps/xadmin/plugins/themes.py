#coding:utf-8
from __future__ import print_function
import httplib2
from django.template import loader
from django.core.cache import cache
from django.utils import six
from django.utils.translation import ugettext as _
from xadmin.sites import site
from xadmin.models import UserSettings
from xadmin.views import BaseAdminPlugin, BaseAdminView
from xadmin.util import static, json
import requests

import six
if six.PY2:
    import urllib
else:
    import urllib.parse

THEME_CACHE_KEY = 'xadmin_themes'


class ThemePlugin(BaseAdminPlugin):

    enable_themes = False
    # {'name': 'Blank Theme', 'description': '...', 'css': 'http://...', 'thumbnail': '...'}
    user_themes = None
    use_bootswatch = False
    default_theme = static('xadmin/css/themes/bootstrap-xadmin.css')
    bootstrap2_theme = static('xadmin/css/themes/bootstrap-theme.css')

    def init_request(self, *args, **kwargs):
        return self.enable_themes

    def _get_theme(self):
        if self.user:
            try:
                return UserSettings.objects.get(user=self.user, key="site-theme").value
            except Exception:
                pass
        if '_theme' in self.request.COOKIES:
            if six.PY2:
                func = urllib.unquote
            else:
                func = urllib.parse.unquote
            return func(self.request.COOKIES['_theme'])
        return self.default_theme

    def get_context(self, context):
        context['site_theme'] = self._get_theme()
        return context

    # Media
    def get_media(self, media):
        return media + self.vendor('jquery-ui-effect.js', 'xadmin.plugin.themes.js')

    # Block Views
    def block_top_navmenu(self, context, nodes):

        themes = [
            {'name': _(u"Default"), 'description': _(u"Default bootstrap theme"), 'css': self.default_theme},
            {'name': _(u"Bootstrap2"), 'description': _(u"Bootstrap 2.x theme"), 'css': self.bootstrap2_theme},
            ]
        select_css = context.get('site_theme', self.default_theme)

        if self.user_themes:
            themes.extend(self.user_themes)

        if self.use_bootswatch:
            ex_themes = cache.get(THEME_CACHE_KEY)
            if ex_themes:
                themes.extend(json.loads(ex_themes))
            else:
                ex_themes = []
                try:
                    flag = False  # 假如为True使用原来的代码，假如为Flase，使用requests库来访问
                    if flag:
                        h = httplib2.Http()
                        resp, content = h.request("https://bootswatch.com/api/3.json", 'GET', '',
                            headers={"Accept": "application/json", "User-Agent": self.request.META['HTTP_USER_AGENT']})
                        if six.PY3:
                            content = content.decode()
                        watch_themes = json.loads(content)['themes']
                    else:
                        # content = requests.get("https://bootswatch.com/api/3.json", verify=False)
                        # if six.PY3:
                        #     content = content.text.decode()
                        # watch_themes = json.loads(content.text)['themes']
                        watch_themes = {
                            "themes": [
                                {
                                    "name": "Cerulean",
                                    "description": "A calm blue sky",
                                    "thumbnail": "https://bootswatch.com/3/cerulean/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/cerulean/",
                                    "css": "https://bootswatch.com/3/cerulean/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/cerulean/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/cerulean/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/cerulean/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/cerulean/variables.less",
                                    "scss": "https://bootswatch.com/3/cerulean/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/cerulean/_variables.scss"
                                },
                                {
                                    "name": "Cosmo",
                                    "description": "An ode to Metro",
                                    "thumbnail": "https://bootswatch.com/3/cosmo/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/cosmo/",
                                    "css": "https://bootswatch.com/3/cosmo/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/cosmo/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/cosmo/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/cosmo/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/cosmo/variables.less",
                                    "scss": "https://bootswatch.com/3/cosmo/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/cosmo/_variables.scss"
                                },
                                {
                                    "name": "Cyborg",
                                    "description": "Jet black and electric blue",
                                    "thumbnail": "https://bootswatch.com/3/cyborg/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/cyborg/",
                                    "css": "https://bootswatch.com/3/cyborg/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/cyborg/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/cyborg/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/cyborg/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/cyborg/variables.less",
                                    "scss": "https://bootswatch.com/3/cyborg/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/cyborg/_variables.scss"
                                },
                                {
                                    "name": "Darkly",
                                    "description": "Flatly in night mode",
                                    "thumbnail": "https://bootswatch.com/3/darkly/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/darkly/",
                                    "css": "https://bootswatch.com/3/darkly/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/darkly/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/darkly/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/darkly/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/darkly/variables.less",
                                    "scss": "https://bootswatch.com/3/darkly/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/darkly/_variables.scss"
                                },
                                {
                                    "name": "Flatly",
                                    "description": "Flat and modern",
                                    "thumbnail": "https://bootswatch.com/3/flatly/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/flatly/",
                                    "css": "https://bootswatch.com/3/flatly/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/flatly/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/flatly/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/flatly/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/flatly/variables.less",
                                    "scss": "https://bootswatch.com/3/flatly/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/flatly/_variables.scss"
                                },
                                {
                                    "name": "Journal",
                                    "description": "Crisp like a new sheet of paper",
                                    "thumbnail": "https://bootswatch.com/3/journal/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/journal/",
                                    "css": "https://bootswatch.com/3/journal/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/journal/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/journal/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/journal/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/journal/variables.less",
                                    "scss": "https://bootswatch.com/3/journal/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/journal/_variables.scss"
                                },
                                {
                                    "name": "Lumen",
                                    "description": "Light and shadow",
                                    "thumbnail": "https://bootswatch.com/3/lumen/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/lumen/",
                                    "css": "https://bootswatch.com/3/lumen/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/lumen/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/lumen/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/lumen/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/lumen/variables.less",
                                    "scss": "https://bootswatch.com/3/lumen/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/lumen/_variables.scss"
                                },
                                {
                                    "name": "Paper",
                                    "description": "Material is the metaphor",
                                    "thumbnail": "https://bootswatch.com/3/paper/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/paper/",
                                    "css": "https://bootswatch.com/3/paper/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/paper/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/paper/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/paper/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/paper/variables.less",
                                    "scss": "https://bootswatch.com/3/paper/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/paper/_variables.scss"
                                },
                                {
                                    "name": "Readable",
                                    "description": "Optimized for legibility",
                                    "thumbnail": "https://bootswatch.com/3/readable/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/readable/",
                                    "css": "https://bootswatch.com/3/readable/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/readable/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/readable/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/readable/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/readable/variables.less",
                                    "scss": "https://bootswatch.com/3/readable/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/readable/_variables.scss"
                                },
                                {
                                    "name": "Sandstone",
                                    "description": "A touch of warmth",
                                    "thumbnail": "https://bootswatch.com/3/sandstone/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/sandstone/",
                                    "css": "https://bootswatch.com/3/sandstone/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/sandstone/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/sandstone/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/sandstone/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/sandstone/variables.less",
                                    "scss": "https://bootswatch.com/3/sandstone/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/sandstone/_variables.scss"
                                },
                                {
                                    "name": "Simplex",
                                    "description": "Mini and minimalist",
                                    "thumbnail": "https://bootswatch.com/3/simplex/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/simplex/",
                                    "css": "https://bootswatch.com/3/simplex/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/simplex/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/simplex/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/simplex/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/simplex/variables.less",
                                    "scss": "https://bootswatch.com/3/simplex/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/simplex/_variables.scss"
                                },
                                {
                                    "name": "Slate",
                                    "description": "Shades of gunmetal gray",
                                    "thumbnail": "https://bootswatch.com/3/slate/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/slate/",
                                    "css": "https://bootswatch.com/3/slate/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/slate/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/slate/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/slate/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/slate/variables.less",
                                    "scss": "https://bootswatch.com/3/slate/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/slate/_variables.scss"
                                },
                                {
                                    "name": "Spacelab",
                                    "description": "Silvery and sleek",
                                    "thumbnail": "https://bootswatch.com/3/spacelab/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/spacelab/",
                                    "css": "https://bootswatch.com/3/spacelab/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/spacelab/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/spacelab/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/spacelab/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/spacelab/variables.less",
                                    "scss": "https://bootswatch.com/3/spacelab/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/spacelab/_variables.scss"
                                },
                                {
                                    "name": "Superhero",
                                    "description": "The brave and the blue",
                                    "thumbnail": "https://bootswatch.com/3/superhero/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/superhero/",
                                    "css": "https://bootswatch.com/3/superhero/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/superhero/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/superhero/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/superhero/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/superhero/variables.less",
                                    "scss": "https://bootswatch.com/3/superhero/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/superhero/_variables.scss"
                                },
                                {
                                    "name": "United",
                                    "description": "Ubuntu orange and unique font",
                                    "thumbnail": "https://bootswatch.com/3/united/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/united/",
                                    "css": "https://bootswatch.com/3/united/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/united/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/united/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/united/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/united/variables.less",
                                    "scss": "https://bootswatch.com/3/united/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/united/_variables.scss"
                                },
                                {
                                    "name": "Yeti",
                                    "description": "A friendly foundation",
                                    "thumbnail": "https://bootswatch.com/3/yeti/thumbnail.png",
                                    "preview": "https://bootswatch.com/3/yeti/",
                                    "css": "https://bootswatch.com/3/yeti/bootstrap.css",
                                    "cssMin": "https://bootswatch.com/3/yeti/bootstrap.min.css",
                                    "cssCdn": "https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/yeti/bootstrap.min.css",
                                    "less": "https://bootswatch.com/3/yeti/bootswatch.less",
                                    "lessVariables": "https://bootswatch.com/3/yeti/variables.less",
                                    "scss": "https://bootswatch.com/3/yeti/_bootswatch.scss",
                                    "scssVariables": "https://bootswatch.com/3/yeti/_variables.scss"
                                }
                            ]
                        }['themes']
                    ex_themes.extend([
                        {'name': t['name'], 'description': t['description'],
                            'css': t['cssMin'], 'thumbnail': t['thumbnail']}
                        for t in watch_themes])
                except Exception as e:
                    print(e)

                cache.set(THEME_CACHE_KEY, json.dumps(ex_themes), 24 * 3600)
                themes.extend(ex_themes)

        nodes.append(loader.render_to_string('xadmin/blocks/comm.top.theme.html', {'themes': themes, 'select_css': select_css}))


site.register_plugin(ThemePlugin, BaseAdminView)
