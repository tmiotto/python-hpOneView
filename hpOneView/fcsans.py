# -*- coding: utf-8 -*-

"""
fcsans.py
~~~~~~~~~~~~

This module implements settings HP OneView REST API
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

__title__ = 'fcsans'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2015) Hewlett Packard Enterprise ' \
                ' Development LP'
__license__ = 'MIT'
__status__ = 'Development'

###
# (C) Copyright (2012-2015) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from hpOneView.common import uri, get_members
from hpOneView.activity import activity


class fcsans(object):

    def __init__(self, con):
        self._con = con
        self._activity = activity(con)

    def get_device_managers(self):
        body = self._con.get(uri['device-managers'])
        return body

    def get_managed_sans(self):
        body = self._con.get(uri['managed-sans'])
        return body

    def get_providers(self):
        body = get_members(self._con.get(uri['providers']))
        return body

    def remove_device_manager(self, manager, blocking=True, verbose=False):
        task, body = self._con.delete(manager['uri'])
        if blocking is True:
            task = self._activity.wait4task(task, tout=600, verbose=verbose)
        return task

    def add_device_manager(self, providerUri, connInfo, blocking=True,
                           verbose=False):
        task, body = self._con.post(providerUri, connInfo)
        return body

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
