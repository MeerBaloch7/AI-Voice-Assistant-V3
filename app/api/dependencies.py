from app.core.container import ServiceContainer


container = ServiceContainer()

container.initialize()


def get_container() -> ServiceContainer:

    return container