from pyramid.config import Configurator

def main(global_config=None, **settings):
    # Make global_config optional so this factory can be called
    # directly (e.g. by `waitress-serve --call module:main`).
    config = Configurator(settings=settings)

    # Route endpoints
    # Homepage route so visiting `/` shows a friendly message
    config.add_route("home", "/", request_method="GET")
    config.add_route("get_all_mk", "/api/matakuliah", request_method="GET")
    config.add_route("get_mk", "/api/matakuliah/{id}", request_method="GET")
    config.add_route("add_mk", "/api/matakuliah", request_method="POST")
    config.add_route("update_mk", "/api/matakuliah/{id}", request_method="PUT")
    config.add_route("delete_mk", "/api/matakuliah/{id}", request_method="DELETE")

    # Scan for `@view_config` decorated views (e.g. in `app.py`)
    config.scan()

    # Finalize and return the WSGI application
    return config.make_wsgi_app()

