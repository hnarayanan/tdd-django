import random

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL= 'git@github.com:hnarayanan/tdd-django.git'


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv'):
        run('mkdir -p %s/%s' % (site_folder, sub_folder))

def _get_latest_source(site_folder):
    if exists(site_folder + '/.git'):
        run('cd %s && git fetch' % (site_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, site_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (site_folder, current_commit))

def deploy():
    site_folder = '/home/web/tdd-django'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(site_folder)
    _update_settings(site_folder, env.host)
    _update_virtualenv(site_folder)
    _update_static_files(site_folder)
    _update_database(site_folder)

