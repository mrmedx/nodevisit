import ipaddress
import sys
import requests
import json

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
IP = ipaddress.IPv4Address

def get_version(url:str):
    try:
        res= requests.get(url+"/json/version", headers={'User-Agent': USER_AGENT},timeout=1)
        js_res = res.json()
        return js_res
    except:
        pass
    return {}

def get_empty_list_res():
    js_res=[]
    js_res.append({"webSocketDebuggerUrl":"At the moment, this target does not open any pages.", "devtoolsFrontendUrl":""})
    return json.dumps(js_res)


def get_list(url:str):
    try:
        res= requests.get(url+"/json/list", headers={'User-Agent': USER_AGENT})
        js_res = res.json()
        return js_res
    except:
        pass
    return get_empty_list_res()


def print_version(version_js):
    if len(version_js)>0:
        print("Target Browser: "+ version_js.get("Browser"),flush=True)
        print("Protocol Version: "+ version_js.get("Protocol-Version"),flush=True)


def print_list_details(list_details):
    if len(list_details)==0:
        list_details=get_empty_list_res()
    try:
        print("webSocketDebuggerUrl: "+list_details[0].get('webSocketDebuggerUrl'),flush=True)
        print('devtoolsFrontendUrl: ' +list_details[0].get('devtoolsFrontendUrl'),flush=True)
    except:
        pass


def exploit(url:str):
    print("exploit "+url+"...\n[",flush=True)
    version_details=get_version(url)
    print_version(version_details)
    list_details=get_list(url)
    print_list_details(list_details)
    print("]",flush=True)


def to_http_link(ip:str, port:str):
    return "http://"+ip+":"+str(port)


def is_vulnerable(curr_ip:str,from_port:int,to_port:int):
    for port in range(from_port-1,to_port+1):
        curr_url = to_http_link(curr_ip, str(port))
        try:
            version = get_version(curr_url)
            if version!={}:
                return {"vuln":True, "link":curr_url}
        except:
            pass
    return {"vuln":False}


def scan(curr_ip:str,from_port:int,to_port:int):
    print("scan "+curr_ip+"...",flush=True)
    status=is_vulnerable(curr_ip,from_port,to_port)
    if status["vuln"]:
        print("*Vulnerable.",flush=True)
        exploit(status["link"])
    else:
        print("Not vulnerable.",flush=True)


def scan_range(from_add:IP, to_add:IP,from_port:int,to_port:int):
    while from_add <= to_add:
        scan(str(from_add),from_port,to_port)
        from_add+=1
 
def print_help_menu():
    print("NodeVisit - find & access Node.js servers configured with the --inspect switch, within a designated range of IP addresses.\nThis tool can also be used to access a Google Chrome instances opened with the --remote-debugging-port.\n",flush=True)
    print("Usage: "+ sys.argv[0]+ " <FROM_IP_ADDRESS> <TO_IP_ADDRESS> <FROM_PORT> <TO_PORT>\n",flush=True)
    print("<FROM_IP_ADDRESS> <TO_IP_ADDRESS>: Specify the IP address range from <FROM_IP_ADDRESS> to <TO_IP_ADDRESS> for scanning and identifying active nodejs servers.\n",flush=True)
    print("<FROM_PORT> <TO_PORT>: (OPTIONAL) verify the presence of an active nodejs server listening on a port within the designated range defined by <FROM_PORT> to <TO_PORT>.",flush=True)

def main():
    if len(sys.argv[1:])<2:
        print_help_menu()
        return
    try:
        from_addr =IP(sys.argv[1])
        to_addr=IP(sys.argv[2])
        from_port=9222
        to_port=9229
        if len(sys.argv[1:])==4:
            from_port=int(sys.argv[3])
            to_port=int(sys.argv[4])
        scan_range(from_addr,to_addr,from_port,to_port)
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    main()



