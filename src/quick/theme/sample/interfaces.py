##############################################################################
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
##############################################################################
"""

$Id$
"""
from zope import interface
from zope.i18nmessageid import MessageFactory

from zojax.extensions.interfaces import IExtensible
from zojax.pageelement.interfaces import IPageElement
from zojax.theme.default.interfaces import ICommonSkinLayer

_ = MessageFactory('quick.theme.sample')



class ISkinLayer(interface.Interface):
    """ Quick sample skin layer """


class IQuickSampleSkin(ISkinLayer, ICommonSkinLayer):
    """ Quick sample skin """


class IPortalHeader(IPageElement):
    """portal header"""


class IPortletable(IExtensible):
    pass