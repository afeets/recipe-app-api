"""
Import Patch function from unit test
Simulate availability of db
"""
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            """"Override with mock object"""
            gi.return_value = True
            call_command('wait_for_db')
            """check was called"""
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Waiting for db"""
        with patch('django.db.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            """Should be called on 6th time"""
            call_command('wait_for_db')
            """check"""
            self.assertEqual(gi.call_count, 6)
