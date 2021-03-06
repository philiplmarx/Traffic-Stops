from selectable.base import ModelLookup
from selectable.registry import registry

from nc.models import Agency


class AgencyLookup(ModelLookup):
    model = Agency
    search_fields = (
        'name__icontains',
    )

registry.register(AgencyLookup)
