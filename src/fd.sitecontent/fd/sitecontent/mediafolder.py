from five import grok
from Acquisition import aq_inner
from plone.directives import dexterity, form

from Products.CMFCore.utils import getToolByName

from plone.app.contentlisting.interfaces import IContentListing


class IMediaFolder(form.Schema):
    """
    A media folder that allows multi uploads of reusable files and images
    """


class MediaFolder(dexterity.Container):
    grok.implements(IMediaFolder)


class View(grok.View):
    grok.context(IMediaFolder)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        self.has_media = len(self.contained_files()) > 0

    def contained_files(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(portal_type=['Image', 'File'],
                          path=dict(query='/'.join(context.getPhysicalPath()),
                                    depth=1))
        resultlist = IContentListing(results)
        return resultlist
