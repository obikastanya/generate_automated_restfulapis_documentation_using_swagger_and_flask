from flask_restx import Api as Api_

class Api(Api_):

    def add_namespace(self, ns, path=None):
        """
        This method registers resources from namespace for current instance of api.
        You can use argument path for definition custom prefix url for namespace.

        :param Namespace ns: the namespace
        :param path: registration prefix of namespace
        """
        if ns not in self.namespaces:
            self.namespaces.append(ns)

            self.sort_namespace() # add this line

            if self not in ns.apis:
                ns.apis.append(self)
            # Associate ns with prefix-path
            if path is not None:
                self.ns_paths[ns] = path
        # Register resources
        for r in ns.resources:
            urls = self.ns_urls(ns, r.urls)
            self.register_resource(ns, r.resource, *urls, **r.kwargs)
        # Register models
        for name, definition in ns.models.items():
            self.models[name] = definition
        if not self.blueprint and self.app is not None:
            self._configure_namespace_logger(self.app, ns)

    # add this method
    def sort_namespace(self):
        """Sort swagger UI sections based on namespace name."""
        self.namespaces = sorted(self.namespaces, key=lambda ns: ns.name)
