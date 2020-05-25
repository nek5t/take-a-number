import graphene

import ticket.schema

class Query(ticket.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)