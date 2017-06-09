import os

import django

from project.tornado_app import options, run

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

    django.setup()

    if options.port:
        run(port=options.port)
    else:
        run()
