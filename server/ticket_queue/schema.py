import graphene

from graphene_django.types import DjangoObjectType
from .models import Ticket

class TicketType(DjangoObjectType):
    class Meta:
        model = Ticket

class Query(object):
    all_tickets = graphene.List(TicketType)

    def resolve_all_tickets(self, info, **kwargs):
        return Ticket.objects.all()