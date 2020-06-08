from django.test import TestCase
from .models import Ticket

# Create your tests here.
class TicketModelTest(TestCase):
    def setUp(self):
        Ticket.objects.create(title="New Task", description="No I haven't tried turning it on and off again.")
    
    def test_ticket_as_string(self):
        ticket = Ticket.objects.get(id=1)
        self.assertEqual(ticket.title, str(ticket))
