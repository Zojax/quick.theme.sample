#
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
#
"""

$Id$
"""
import os.path

from z3c.breadcrumb.interfaces import IBreadcrumb
from z3c.form.interfaces import IForm

from zope.app.component.hooks import getSite
from zope.app.component.interfaces import ISite
from zope.component import getMultiAdapter, getUtility
from zope.traversing.api import getPath
from zope.traversing.browser import absoluteURL

from zojax.content.feeds.feeds import Feeds
from zojax.content.forms.interfaces import IContentWizard
from zojax.content.space.interfaces import IWorkspace
from zojax.content.type.interfaces import IContentType
from zojax.controlpanel.interfaces import IConfiglet
from zojax.layout.pagelet import BrowserPagelet
from zojax.skintool.interfaces import ISkinTool


class LayoutPage(object):

    notRoot = False
    contentId = 'portal-root'
    contentClass = 'portal-root'

    def update(self):
        context = self.context
        request = self.request
        maincontext = self.maincontext
        mainview = self.mainview
        ws = mainview
        view = mainview
        viewclass = mainview.__class__.__bases__[0]
        ct = IContentType(maincontext, None)

        self.portal_url = '%s/' % absoluteURL(context, request)

        self.context_title = getMultiAdapter(
            (maincontext, request), IBreadcrumb).name

        if not ISite.providedBy(maincontext):
            self.notRoot = True
            self.portal_title = getMultiAdapter(
                (getSite(), request), IBreadcrumb).name

        self.url = '%s/' % request.URL
        self.base_url = '%s/' % request.URL[-1]

        # body id

        while not IWorkspace.providedBy(ws):
            ws = ws.__parent__
            if ws is None:
                break

        self.contentClass = 'aero'

        if ws is not None:
            self.contentClass += ' section-workspace-%s' % ws.__name__.replace(
                '.', '-')

        if IConfiglet.providedBy(maincontext):
            self.contentClass += ' section-controlpanel-%s' % maincontext.__name__.replace(
                '.', '-')

        # body class

        if ct is None:
            ctname = maincontext.__name__
        else:
            ctname = ct.name

        if IConfiglet.providedBy(maincontext):
            ctname = maincontext.__name__

        self.contentId = '-'.join(
            ('section', ctname, mainview.__name__)).replace('.', '-').replace('@', '')

        if IForm.providedBy(mainview):
            self.contentClass += ' ' + mainview.mode

        if not viewclass is BrowserPagelet:
            self.contentClass += ' %s.%s' % (
                viewclass.__module__, viewclass.__name__)

        if mainview.template:
            self.contentClass += ' %s' % (
                os.path.split(mainview.template.filename)[1])

        self.contentClass = self.contentClass.replace('.', '-').lower()
        self.sitePath = getPath(getSite())[1:].replace('/', '-')
        self.contentPath = getPath(maincontext)[1:].replace('/', '-')

        while not IContentWizard.providedBy(view):
            view = view.__parent__
            if view is None:
                break

        self.wizard = view is not None

        self.wizard = self.wizard or isinstance(maincontext, Feeds)
        if self.wizard:
            self.contentClass += ' wizard'
