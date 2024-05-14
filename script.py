print('''************************************************************
Welcome to the script and have fun !''')
push_config = input("if you want ospf press 1 , if you want bgp press 2 and if you want static route press 3 :")
import yaml
from netmiko import ConnectHandler
device = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.88.129',
    'username':'admin',
    'password':'admin',
}
connect=ConnectHandler(**device)
from jinja2 import Environment, FileSystemLoader
with open('inputbgp.yaml') as file:
    data = yaml.full_load(file)

with open('inputospf.yaml') as file1:
    data1 = yaml.full_load(file1)

with open('inputstatic.yaml') as file2:
    data2 = yaml.full_load(file2)

def render_jinja2( jinja_file , jinja_argument):
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template(jinja_file)
    out = temp.render(a=jinja_argument)
    return out


if push_config == '1':
    configuration = render_jinja2('ospf.j2',data1)
    c = configuration.splitlines()
    out=connect.send_config_set(c)
    print(out)
if push_config == '2':
    configuration = render_jinja2('BGP.j2',data)
    c = configuration.splitlines()
    out=connect.send_config_set(c)
    print(out)

if push_config == '3':
    configuration = render_jinja2('static.j2',data2)
    c = configuration.splitlines()
    out=connect.send_config_set(c)
    print(out)
