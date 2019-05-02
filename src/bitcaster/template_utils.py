import os

from markupsafe import Markup

from bitcaster.app import app


@app.template_filter()
def checkmark(on_off):
    """Convert a string to all caps."""
    if on_off:
        value = '<i class="fas fa-check green mr-2"></i>'
    else:
        value = ''
    return Markup(value)


@app.context_processor
def globals():
    return dict(GOOGLE_ANALYTICS_CODE=os.environ.get('GOOGLE_ANALYTICS_CODE', None),
                )
