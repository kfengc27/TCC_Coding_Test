from django.test import TestCase

# Create your tests here.

from .views import sendEmail

class EmailTest(TestCase):
    pass 
    # def test_send_email(self):
    #     subject = "Test Email"
    #     message = "Tcc Interview Task"
    #     email_to = ["chengbin.feng@outlook.com",]
    #     sendEmail(subject,message,email_to)

    #     # Test that one message has been sent.
    #     self.assertEqual(len(sendEmail.outbox), 1)

    #     # Verify that the subject of the first message is correct.
    #     self.assertEqual(sendEmail.outbox[0].subject, 'Test Email')