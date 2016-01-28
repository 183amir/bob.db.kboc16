#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks at the KBOC16 database.
"""

import os, sys
import unittest
from .query import Database

class KBOC16DatabaseTest(unittest.TestCase):

    def test_clients(self):
      db = Database()
      assert len(db.groups()) == 1
      assert len(db.clients()) == 300
      assert len(db.clients(groups='eval')) ==300
      assert len(db.models()) == 300
      assert len(db.models(groups='eval')) == 300


    def test_objects(self):
      db = Database()
      assert len(db.objects()) == 7200
      # A
      assert len(db.objects(protocol='A')) == 7200
      assert len(db.objects(protocol='A', groups='eval')) == 7200
      assert len(db.objects(protocol='A', groups='eval', purposes='enrol')) == 1200
      assert len(db.objects(protocol='A', groups='eval', purposes='probe')) == 6000
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', classes='client')) == 6000
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1])) == 20
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1], classes='client')) == 20
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2])) == 40
      assert len(db.objects(protocol='A', groups='eval', purposes='probe', model_ids=[1,2], classes='client')) == 40


    def test_driver_api(self):

      from bob.db.base.script.dbmanage import main
      assert main('KBOC16 dumplist --self-test'.split()) == 0
      assert main('KBOC16 checkfiles --self-test'.split()) == 0
      assert main('KBOC16 reverse T001_01 --self-test'.split()) == 0
      assert main('KBOC16 path 37 --self-test'.split()) == 0"""
