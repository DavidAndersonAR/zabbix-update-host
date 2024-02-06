import csv
from pyzabbix import ZabbixAPI

# Configurações do Zabbix
ZABBIX_SERVER = 'http://localhost/zabbix'
ZABBIX_USERNAME = 'Usuario'
ZABBIX_PASSWORD = 'senha'

# Função para conectar ao Zabbix API
def connect_zabbix_api():
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login(ZABBIX_USERNAME, ZABBIX_PASSWORD)
    return zapi

# Função para ler o arquivo CSV e adicionar hosts ao Zabbix
def add_hosts_from_csv(arquivo_csv):
    zapi = connect_zabbix_api()
    
    with open(arquivo_csv, newline='') as csvfile:
        entradaRead = csv.reader(csvfile, delimiter=';')
        for row in entradaRead:
            host_name = row[0]
            ip_address = row[1]
            group_name = row[2]
            print(group_name)
            template_name = row[3]
            
            # Obtém o ID do grupo
            group_id = zapi.hostgroup.get(filter={'name': group_name}) [0]['groupid']
            print(group_id)
            
            # Obtém o ID do template
            template_id = zapi.template.get(filter={'host': template_name}) [0]['templateid']
            
            # Adiciona o host
            zapi.host.create(
                host=host_name,
                interfaces=[{'type': 2, 'main': 1,"useip":1, 'ip': ip_address, 'dns': '', 'port': 161,"details":{ "version":2, "community":"{$SNMP_COMMUNITY}"}}],
                groups=[{'groupid': group_id}],
                templates=[{'templateid': template_id}]
            )
            print(f"Host '{host_name}' adicionado com sucesso!")

# Arquivo CSV com os dados dos hosts
arquivo_csv = 'add_host.csv'

# Chamada da função para adicionar hosts a partir do arquivo CSV
add_hosts_from_csv(arquivo_csv)
