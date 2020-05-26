import graphene

import ticket_queue.schema

class Query(ticket_queue.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)