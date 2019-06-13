

class TemplateRenderer(object):
    """
    Mock class for some real template engine. Jinja, mako you name it.
    """
    def render(self, template: str, **kwargs):
        return template.format(**kwargs)