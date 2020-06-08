from django.test.testcases import TestCase
from .schema import Query
import graphene

# Create your tests here.
class ApiSchemaTest(TestCase):

    def test_empty_response(self):
        query = """
            query {
                allTickets {
                    id
                    title
                }
            }
        """

        schema = graphene.Schema(query=Query)
        result = schema.execute(query)

        self.assertIsNone(result.errors)