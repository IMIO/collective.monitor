from Zope2 import app as App
from zope.component.hooks import setSite
import os


def get_plone_site(connection, container, plone_path=None):
    """ Return plone site """
    if plone_path:
        plone_paths = [path for path in plone_path.split(os.sep) if path]
        for path_name in plone_paths:
            container = container.get(path_name)
        plone_site = container
        if not plone_site:
            msg = "Error, path '{0}' do not exist".format(plone_path)
            connection.write(str(msg))
            return False
        if plone_site.meta_type != "Plone Site":
            msg = "Error, path {0} is not a plone site, it's {1}".format(plone_path, plone_site.meta_type)
            connection.write(str(msg))
            return False
        else:
            return plone_site
    else:
        result = False
        for obj in container.values():
            if obj.meta_type == "Folder": # if plone site come from mount point
                for plone in obj.values():
                    if plone.meta_type == "Plone Site":
                        result = plone
            else:
                if obj.meta_type == "Plone Site" and not result:
                    result = obj
        return result


def get_users(context, obj=True):
    from Products.CMFCore.utils import getToolByName
    portal = getToolByName(context, "portal_url").getPortalObject()
    users = []
    for user in portal.acl_users.searchUsers():
        if user['pluginid'] == 'source_users':
            if obj:
                users.append(portal.portal_membership.getMemberById(user['userid']))
            else:
                users.append(user['userid'])
    return users


def count_users(connection, plone_path=None):
    """the total amount of users in your plone site"""
    app = App()
    # container = app.unrestrictedTraverse('/')
    plone_site = get_plone_site(connection, app, plone_path)
    if plone_site:
        setSite(plone_site)
        users = get_users(plone_site)
        connection.write(str(len(users)))
