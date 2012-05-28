from Acquisition import aq_inner
from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from Products.CMFCore.utils import getToolByName

from plone.app.contentlisting.interfaces import IContentListing
from fd.blog.blogentry import IBlogEntry

from fd.blog import MessageFactory as _


# Interface class; used to define content-type schema.

class IBlog(form.Schema, IImageScaleTraversable):
    """
    A fcontainer for blog entries
    """


class Blog(dexterity.Container):
    grok.implements(IBlog)


class View(grok.View):
    grok.context(IBlog)
    grok.require('zope2.View')
    grok.name('view')

    def update(self):
        self.has_entries = len(self.blog_entries()) > 0

    def blog_entries(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IBlogEntry.__identifier__,
                          path=dict(query='/'.join(context.getPhysicalPath()),
                                    depth=1),
                          review_state='published',
                          sort_on='effective')
        resultlist = IContentListing(results)
        return resultlist
