from pyzabbix import ZabbixAPI

def upadate_host():
    try:
        zapi = ZabbixAPI("seu_servidor_zabbix")
        zapi.login("usuario", "senha")
        print(f"Login efetuado com sucesso! {zapi.api_version()}")
    except Exception as erro:
        print(erro)
    
    # Passando o id do host em uma variavel
    host_para_alterar = 0101

    # Fazendo a chamado do host pela API do zabbix
    hosts = zapi.host.get(output = ["name" , "hostid"], hostids = host_para_alterar)

    for host in hosts:
        host_name = host["name"]
        host_id = host["hostid"]

        update_info = {
            "hostid" : host_id,
            "status" : 0,
            "templates" : [
                {
                    "templateid" : 0202
                },
                {
                    "templateid" : 0303
                }
            ]
        }


        try:
            result = zapi.host.update(update_info)
            print("Host atualizado com sucesso")
        except Exception as erro:
            print("Erro ao tenta atualizar o host", erro)

    zapi.logout

upadate_host()