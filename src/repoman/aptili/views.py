from django.shortcuts import render
from django.http import HttpResponse

##
import requests
from bs4 import BeautifulSoup

def index(request):
    return HttpResponse("Hello from Aptili")

def get_pardus_dists(request):
    # get the response from the URL
    r = requests.get('http://depo.pardus.org.tr/pardus/dists')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        a_html = soup.findAll('a')
        for i in a_html:
            if i.text != "../":
                print(i.text[:-1])
        return HttpResponse("connected")
    else:
        return HttpResponse("cant connect")

######### MIRROR
def pardus_mirror_create():
    # create & publish
    pass

def pardus_mirror_check():
    #1- kurum yansısı vs pardus (şu güncellemer var)
    #2- pardus vs local reposu (şu güncellemer local reponu ezecek)
    pass

def pardus_mirror_update_switch():
    pass

def pardus_mirror_rsync():
    # ln -s yeterli
    pass

######### LOCAL REPO
def local_repo_create():
    pass
#aptly repo create -distribution="ondokuz" -architectures="amd64,i386,source,arm64" -component="main" -comment="Afad 19 Yerel" afad-ondokuz-yerel
#-distribution -comment -repo_name -kurum_tag

def local_repo_package_add():
    pass
def local_repo_package_remove():
    pass
def local_repo_show_info():
    pass
def local_repo_show_packages_list():
    pass

def local_repo_publish():
    #if varsa repo publish drop et publish
    #aptly publish repo -component=main -architectures="amd64,i386,source" -origin="Pardus" -label="Yirmibir gvfs" -distribution=yirmibir-gvfs gvfs-yirmibir experimental
    #no parametre
    pass

def local_repo_publish_drop():
    pass

def local_repo_rsync():
    # rsync --delete must, link yapma
    pass






