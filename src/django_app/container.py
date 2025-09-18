# django_app/container.py

from dependency_injector import containers, providers

class CoreContainer(containers.DeclarativeContainer):
  pass

core_container = CoreContainer()