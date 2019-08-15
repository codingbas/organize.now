{"filter":false,"title":"tests.py","tooltip":"/dashboard/tests.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":0},"end":{"row":2,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"f729e25bc04704e191d344988d373c6375a0e9b6","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":3,"column":0},"end":{"row":19,"column":55},"action":"insert","lines":["from django.test import TestCase, Client","from accounts.client import Login","","","\"\"\"","Checks the if logged in user can access the dashboard page","\"\"\"","class DashboardViewTests(TestCase):","    ","    # This runs a testing client","    c=Client()","    ","    def test_dashboard_view(self):","        Login.setUp(self)","        page = self.c.get(\"/dashboard/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"dashboard.html\")"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.test import TestCase","","# Create your tests here."],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":5}]]},"timestamp":1565782558930}