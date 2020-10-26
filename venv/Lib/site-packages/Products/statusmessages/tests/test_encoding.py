# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import unittest


class TestEncoding(unittest.TestCase):

    def test_encoding_msg_with_type(self):
        """Test message encoding:
        """
        from Products.statusmessages.message import Message
        from Products.statusmessages.message import decode
        m = Message('späm', 'eggs')
        self.assertEqual(
            m.encode(),
            b'\x00\xa4sp\xc3\xa4meggs',
        )
        self.assertEqual(decode(m.encode())[0], m)

    def test_encoding_msg_without_type(self):
        from Products.statusmessages.message import Message
        from Products.statusmessages.message import decode
        m = Message('späm')
        self.assertEqual(
            m,
            Message('späm'),
        )
        self.assertEqual(m.encode(), b'\x00\xa0sp\xc3\xa4m')
        self.assertEqual(decode(m.encode())[0], m)

    def test_decoding(self):
        """Test message decoding:
        """
        from Products.statusmessages.message import decode

        # Craft a wrong value:
        m, rem = decode(b'\x01\x84spameggs')
        self.assertEqual(
            m.message,
            'spameggs',
        )
        self.assertEqual(
            m.type,
            '',
        )
        self.assertEqual(rem, b'')

        # Craft another wrong value:
        m, rem = decode(b'\x00\x24spameggs')
        self.assertEqual(
            m.message,
            's',
        )
        self.assertEqual(
            m.type,
            'pame',
        )
        self.assertEqual(rem, b'ggs')

        # And another wrong value:
        m, rem = decode(b'\x00spameggs')
        self.assertEqual(
            m.message,
            'pam',
        )
        self.assertEqual(
            m.type,
            'eggs',
        )
        self.assertEqual(rem, b'')

        # And yet another wrong value:
        m, rem = decode('')

        self.assertIs(m, None)
        self.assertEqual(rem, b'')
