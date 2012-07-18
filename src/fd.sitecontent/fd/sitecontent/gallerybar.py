from five import grok
from Acquisition import aq_inner
from zope.interface import Interface
from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

from plone.app.layout.viewlets.interfaces import IPortalFooter

from plone.app.blob.interfaces import IATBlobImage


class GalleryBarViewlet(grok.Viewlet):
    grok.name('fd.sitecontent.GalleryBarViewlet')
    grok.context(Interface)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter)

    def update(self):
        pstate = getMultiAdapter((self.context, self.request),
                                 name="plone_portal_state")
        self.portal_url = pstate.portal_url()
        self.has_images = len(self.images()) > 0

    def images(self):
        items = []
        data = self._gallery_data()
        if data:
            for item in data:
                info = {}
                info['title'] = item.Title
                info['id'] = item.getId
                info['url'] = item.getURL()
                info['image_tag'] = self.getImageTag(item.getObject())
                items.append(info)
        return items

    def _gallery_data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        gallery = self._mediafolder()
        if gallery:
            results = catalog(
                        object_provides=IATBlobImage.__identifier__,
                        path=dict(query='/'.join(gallery.getPhysicalPath()),
                                  depth=1))
            return results

    def _mediafolder(self):
        pstate = getMultiAdapter((self.context, self.request),
                                 name="plone_portal_state")
        portal = pstate.portal()
        try:
            gallery = portal['gallery']
            return gallery
        except:
            return None

    def getImageTag(self, item):
        obj = item
        scales = getMultiAdapter((obj, self.request), name='images')
        scale = scales.scale('image', width=260, height=260)
        imageTag = None
        if scale is not None:
            imageTag = scale.tag()
        return imageTag
