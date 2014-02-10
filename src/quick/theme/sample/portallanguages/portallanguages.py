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
from zope.component import getUtility
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.app.component.hooks import getSite, setSite
from zope.app.component.interfaces import ISite
from zope.traversing.api import getRoot, getPath
import re
from interfaces import IPortalLanguagesConfiglet
import zojax.language
from zojax.language.interfaces import ISiteLanguage

class PortalLanguages(object):
    ''' Show Portal Languages '''

    def __init__(self, context, request, view, manager=None):
        super(PortalLanguages, self).__init__(context, request, view, manager)

    def getLanguages(self):
        tool = getUtility(IPortalLanguagesConfiglet)
        if not tool.isVisible:
            return []
        patern = re.compile(r"(.*)_(.*)$")
        site_name = patern.split(getSite().__name__)

        def normalise_site_name(site_name):
            return len(site_name)>1 and site_name[1:] or site_name + ['gb']
        site_name = normalise_site_name(site_name)
        root = getRoot(self.context)
        sites = []
        current_site = getSite()
        for site in [(i,normalise_site_name(patern.split(i[0]))) for i in root.items() if ISite.providedBy(i[1])]:
            setSite(site[0][1])
            if getUtility(IPortalLanguagesConfiglet).isVisible:
                sites.append(site)
        setSite(current_site)

        def link_by_path(path,site):
            if len(path)==0:
                return site
            parent = site
            item = path[0]
            for item in path:
                if item in [i for i in parent.keys()]:
                    parent = parent[item]
                else:
                    break
            return parent

        langs = []
        for site in sites:
            if site[1][0]==site_name[0]:
                setSite(site[0][1])
                langs.append({
                            'code':site[1][1],
                            'link':absoluteURL(link_by_path(getPath(self.context).split('/')[2:],site[0][1]),self.request),
                            'title':re.sub(r'(\/.*)? ?\[.*?\]$','',[i[1].title for i in zojax.language.vocabulary.terms if i[1].value == getUtility(ISiteLanguage).language][0])
                            })
                setSite(current_site)

        return langs
