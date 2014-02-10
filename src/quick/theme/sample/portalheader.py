##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope.component import queryMultiAdapter
from zope.contentprovider.interfaces import IContentProvider

from zojax.content.feeds.feeds import Feeds
from zojax.controlpanel.interfaces import IConfiglet
from zojax.layoutform.interfaces import IPageletSubform
from zojax.principal.registration.browser.join import RegistrationForm

from interfaces import IPortletable


class PortalHeader(object):

    def update(self):
        context = self.context
        request = self.request

        while context is not None and (not IPortletable.providedBy(context)):
            context = context.__parent__

        self.headerContext = context
        self.hasTopBanner = queryMultiAdapter(
            (context, request, self), IContentProvider, name='banners.top')
        self.hasHeaderInfo = queryMultiAdapter(
            (context, request, self), IContentProvider, name='header.info')
        self.personalBar = not isinstance(self.view, RegistrationForm) \
            and (IConfiglet.providedBy(self.context)
                 or IPageletSubform.providedBy(self.view)
                 or isinstance(self.context, Feeds))

