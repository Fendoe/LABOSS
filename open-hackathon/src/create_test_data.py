#!/usr/bin/python
# -*- coding: utf8 -*-

'''not necessary for Production environment'''

from hackathon.database import *
from hackathon.database.models import *
from hackathon.log import *
from hackathon.enum import *

# vm = DockerHostServer(vm_name="localhost", public_dns="localhost", public_docker_api_port=8001, private_ip="10.0.2.15",
# private_docker_api_port=8001, container_count=0, container_max_count=100)
# vm = DockerHostServer(vm_name="osslab-vm-20.chinacloudapp.cn", public_dns="osslab-vm-20.chinacloudapp.cn",
#                       public_docker_api_port=8001, private_ip="10.210.18.47", private_docker_api_port=8001,
#                       container_count=0, container_max_count=100)
# db.session.add(vm)

db_adapter.add_object_kwargs(DockerHostServer,
                             vm_name="OSSLAB-VM-18",
                             public_dns="osslab-vm-18.chinacloudapp.cn",
                             public_docker_api_port=4243,
                             private_ip="10.210.18.47",
                             private_docker_api_port=4243,
                             container_count=0,
                             container_max_count=100)

db_adapter.add_object_kwargs(Announcement, content="欢迎访问开放黑客松平台")

hackathon_name = 'open-xml-sdk'
h = db_adapter.add_object_kwargs(Hackathon, name=hackathon_name, sponsor=1, end_time="2015-03-16 00:00:00")

db_adapter.add_object_kwargs(Register, hackathon=h, register_name="Yifu Huang", email="ifhuang91@gmail.com")
db_adapter.add_object_kwargs(Register, hackathon=h, register_name="xxzhe", email="zhengxx012@gmail.com")
db_adapter.add_object_kwargs(Register, hackathon=h, register_name="Ice", email="v-iceshi@microsoft.com")

# add public templates to database
template_dir = 'hackathon/resources'
if not os.path.isdir(template_dir):
    log.error('template dir %s is not exist' % template_dir)
    sys.exit(1)
template_files = os.listdir(template_dir)
if template_files is None:
    log.error('template dir %s is empty' % template_dir)
    sys.exit(1)
for template_file in template_files:
    if hackathon_name in template_file:
        name = template_file.replace(hackathon_name+'-', '').replace('.js', '')
        template_url = os.getcwd() + os.path.sep + template_dir + os.path.sep + template_file
        provider = VirtualEnvironmentProvider.Docker
        if name == 'windows':
            provider = VirtualEnvironmentProvider.AzureVM
        db_adapter.add_object_kwargs(Template, hackathon=h, name=name, url=template_url, provider=provider)

db_adapter.commit()
