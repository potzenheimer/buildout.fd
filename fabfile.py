from fabric.api import task
from fabric.api import env

from ade25.fabfiles import project

env.use_ssh_config = True
env.forward_agent = True
env.port = '22222'
env.user = 'root'
env.hosts = ['zope8']
env.webserver = '/opt/webserver/buildout.webserver'
env.code_root = '/opt/sites/fleckendeckend/buildout.fleckendeckend'
env.local_root = '/Users/cb/dev/fd/buildout.fd'
env.sitename = 'fleckendeckend'
env.code_user = 'root'
env.prod_user = 'www'


@task
def deploy():
    """ Deploy current master to production server """
    project.site.update()
    project.site.restart()


@task
def deploy_full():
    """ Deploy current master to production and run buildout """
    project.site.update()
    project.site.build()
    project.site.restart()


@task
def rebuild():
    """ Deploy current master and run full buildout """
    project.site.update()
    project.site.build_full()
    project.site.restart()


@task
def get_data():
    """ Copy live database for local development """
    project.db.download_data()
