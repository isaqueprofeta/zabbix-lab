import sys
import logging
from time import sleep
from importlib import import_module

# Logging setting for docker containers
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('zabbix-provisioning')

# Install pyzabbix with pip module
try:
    import_module('pyzabbix')
except ImportError:
    import pip
    pip.main(['install', 'pyzabbix'])
finally:
    globals()['pyzabbix'] = import_module('pyzabbix')

# Zabbix default credentials
user = "Admin"
password = "zabbix"
server = "http://zabbix-frontend:8080/"
zapi = pyzabbix.ZabbixAPI(server)
zapi.session.verify = False

# Wait for zabbix-frontend container to be available
frontend_available = False
while frontend_available is False:
    try:
        logger.info('Trying to connect to zabbix-frontend')

        zapi.login(user, password)
        frontend_available = True

        logger.info('Connected to zabbix-frontend')
    except Exception:
        logger.info('Waiting 5 secs for zabbix-frontend to be available')
        sleep(5)

# Update the Zabbix server to connect to zabbix-agent container
logger.info('Searching for "Zabbix server" host to update')
host = zapi.host.get(
    output=['hostid'],
    filter={
        'host': 'Zabbix server'
    },
    selectInterfaces=['interfaceid']
)
logger.info('Ok, got the host information, rolling the interface update')
host_update = zapi.hostinterface.update(
    interfaceid=host[0]['interfaces'][0]['interfaceid'],
    ip='',
    dns='zabbix-agent',
    useip=0
)
logger.info(f'Updated interface: {host_update}')

# Integration with mailhog container to test e-mail media type
logger.info('Searching for "Email" Media Type to update')
mediatype = zapi.mediatype.get(
    output=['mediatypeid'],
    filter={
        'name': 'Email'
    },
)
logger.info('Ok, got the Media Type information, rolling the update')
mediatype_update = zapi.mediatype.update(
    mediatypeid=mediatype[0]['mediatypeid'],
    smtp_port=1025,
    smtp_server="mailhog",
    smtp_helo="zabbixlab.local",
    smtp_email="zabbix@zabbixlab.local"
)
logger.info(f'Updated: {mediatype_update}')

# Integration with mailhog container to test e-mail media type
logger.info('Updating Admin Media with random mail')
user = zapi.user.get(
    output=['userid'],
    filter={
        'alias': 'Admin'
    }
)
logger.info('Ok, got the Admin information, rolling the media update')
media_update = zapi.user.update(
    userid=user[0]['userid'],
    user_medias=[{
        'mediatypeid': 1,
        'sendto': ['admin@zabbixlab.local'],
        'active': 0,
        'severity': 63,
        'period': '1-7,00:00-24:00'
    }]
)
logger.info(f'Updated: {media_update}')

# Update the global problem action to enable
logger.info('Searching for "Report problems to Zabbix administrators" action')
action = zapi.action.get(
    output=['actionid'],
    filter={
        'name': 'Report problems to Zabbix administrators'
    }
)
logger.info('Ok, got the action information, rolling the status update')
action_update = zapi.action.update(
    actionid=action[0]['actionid'],
    status=0
)
logger.info(f'Updated action: {action_update}')
