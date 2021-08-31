__author__ = "N3g4t1v3"
__discord__ = "N3g4t1v3#4103"

# Importing modules
try:
    import sys
    import time
    from stem import Signal
    from stem.control import Controller
    import random
    import requests
    import socket
    import re
    import threading
    import os
    import subprocess
except ModuleNotFoundError:
    exit("You need to install the right modules")


class color:
    if os.name == 'nt':
        @staticmethod
        def black(text):
            return text

        @staticmethod
        def red(text):
            return text

        @staticmethod
        def pastel_red(text):
            return text

        @staticmethod
        def yellow(text):
            return text

        @staticmethod
        def blue(text):
            return text

        @staticmethod
        def green(text):
            return text

        @staticmethod
        def white(text):
            return text

        @staticmethod
        def magenta(text):
            return text

    else:
        @staticmethod
        def black(text):
            text = f"\u001b[30m{text}\u001b[39m"
            return text

        @staticmethod
        def red(text):
            text = f"\u001b[31m{text}\u001b[39m"
            return text

        @staticmethod
        def pastel_red(text):
            text = f"\u001b[91m{text}\u001b[39m"
            return text

        @staticmethod
        def yellow(text):
            text = f"\u001b[33m{text}\u001b[39m"
            return text

        @staticmethod
        def blue(text):
            text = f"\u001b[36m{text}\u001b[39m"
            return text

        @staticmethod
        def green(text):
            text = f"\u001b[92m{text}\u001b[39m"
            return text

        @staticmethod
        def white(text):
            text = f"\u001b[97m{text}\u001b[39m"
            return text

        @staticmethod
        def magenta(text):
            text = f"\u001b[95m{text}\u001b[39m"
            return text


class exceptions:

    class CommandParameterError(Exception):
        pass

    class ParameterError(Exception):
        pass

    class UndifinedError(Exception):
        pass

    class ManagementError(Exception):
        pass

    class AccessError(Exception):
        pass

class SubScanError:

    @staticmethod
    def AdminError():
        raise exceptions.AccessError(color.pastel_red("\nPlease use this command in admin mode\n"))

    @staticmethod
    def MethodError():
        try:
            subprocess.run('sudo service tor stop', shell=True)
        except:
            pass
        raise exceptions.CommandParameterError(color.pastel_red("\nMethod Error\n"))

    @staticmethod
    def TorError():
        try:
            subprocess.run('sudo service tor stop', shell=True)
        except:
            pass
        raise exceptions.ParameterError(color.pastel_red("\nTor Error\n"))

    @staticmethod
    def error():
        try:
            subprocess.run('sudo service tor stop', shell=True)
        except:
            pass
        raise exceptions.UndifinedError(color.red("\nError !\n"))

    @staticmethod
    def invalid_argumentError():
        raise exceptions.CommandParameterError(color.red("Arguments invalids"))

    @staticmethod
    def keyboard_exit():
        try:
            subprocess.run('sudo service tor stop', shell=True)
        except:
            pass
        exit()

    @staticmethod
    def UrlError():
        raise exceptions.CommandParameterError(color.pastel_red("Url Error"))

    @staticmethod
    def WindowsError():
        raise exceptions.ManagementError(color.pastel_red("Windows does not support Tor"))


class User_agent:
    list = ['User_agent.Linux.Firefox', 'User_agent.Linux.Edge', 'User_agent.Linux.Chrome', 'User_agent.Linux.Opera',
            'User_agent.Windows.Firefox', 'User_agent.Windows.Edge', 'User_agent.Windows.Chrome', 'User_agent.Windows.Opera',
            'User_agent.Apple.Mac.Firefox', 'User_agent.Apple.Mac.Edge', 'User_agent.Apple.Mac.Chrome', 'User_agent.Apple.Mac.Opera', 'User_agent.Apple.Mac.Safari',
            'User_agent.Apple.Iphone.Firefox', 'User_agent.Apple.Iphone.Edge', 'User_agent.Apple.Iphone.Chrome', 'User_agent.Apple.Iphone.Opera', 'User_agent.Apple.Iphone.Safari',
            'User_agent.Android.Firefox', 'User_agent.Android.Edge', 'User_agent.Android.Chrome', 'User_agent.Android.Opera',
            'User_agent.Playstation.PS4', 'User_agent.Playstation.PS5',
            'User_agent.Bot.Google', 'User_agent.Bot.Bing', 'User_agent.Bot.Yahoo']

    class Linux:
        start = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) "

        Firefox = str(start + 'Gecko/20100101 Firefox/78.0')
        Edge = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Edge/12.246')
        Chrome = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/605.1.15')
        Opera = str(start + 'AppleWebKit/605.1.15  (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/605.1.15 OPR/77.0.4054.203')

    class Apple:
        class Mac:
            start = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) "

            Chrome = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/605.1.15')
            Safari = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15')
            Firefox = str(start + 'Gecko/20100101 Firefox/42.0')
            Edge = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Edge/12.246')
            Opera = str(start + 'AppleWebKit/605.1.15  (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/605.1.15 OPR/77.0.4054.203')

        class Iphone:
            start = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_0 like Mac OS X) "
            Chrome = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/605.1.15')
            Safari = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15')
            Firefox = str(start + 'Gecko/20100101 Firefox/42.0')
            Edge = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Edge/12.246')
            Opera = str(start + 'AppleWebKit/605.1.15  (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/605.1.15 OPR/77.0.4054.203')

    class Windows:
        start = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        Chrome = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/605.1.15')
        Firefox = str(start + 'Gecko/20100101 Firefox/42.0')
        Edge = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Edge/12.246')
        Opera = str(start + 'AppleWebKit/605.1.15  (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/605.1.15 OPR/77.0.4054.203')

    class Android:
        start = "Mozilla/5.0 (Android; Mobile; rv:18.0) "
        Chrome = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/605.1.15')
        Firefox = str(start + 'Gecko/20100101 Firefox/42.0')
        Edge = str(start + 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Edge/12.246')
        Opera = str(start + 'AppleWebKit/605.1.15  (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/605.1.15 OPR/77.0.4054.203')

    class Playstation:
        PS4 = 'Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/605.1.15 (KHTML, like Gecko)'
        PS5 = 'Mozilla/5.0 (PlayStation 5 3.11) AppleWebKit/605.1.15 (KHTML, like Gecko)'

    class Bot:
        start = 'Mozilla/5.0 (compatible; '
        Google = str(start + 'Googlebot/2.1; +http://www.google.com/bot.html)')
        Bing = str(start + 'bingbot/2.0; +http://www.bing.com/bingbot.htm)')
        Yahoo = str(start + 'Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')


# Creating a new class for the module SubScan
class SubScan_utils:

    @staticmethod
    def shortcut():
        if os.name == "nt":
            with open('SubScan.bat', 'w') as sc:
                sc.write(f'python {__file__}')
            sc.close()
            subprocess.run(f'''powershell "start cmd '-cmd /K move {SubScan_utils.get_path()}SubScan.bat C:\Windows\System32 && exit' -v runAs " ''', shell=False)

        else:
            with open('SubScan', 'w') as sc:
                sc.write(f'#!/bin/bash\npython{sys.version[:3]} {__file__}')
            sc.close()
            subprocess.run('sudo chmod +x SubScan && sudo mv ./SubScan /../bin/', shell=True)

    @staticmethod
    def clear():
        print('\033c')

    @staticmethod
    def get_path():
        path = str()

        if os.name == "nt":
            s = '\\'
        else:
            s = '/'
        for directory in __file__.split(s)[0:-1]:
            path = path + directory + s


        return path

    @staticmethod
    def stop_tor_service():
        try:
            subprocess.run('sudo service tor stop', shell=True)
        except:
            pass

    @staticmethod
    def new_session(*ua):
        if os.name == "nt":
            SubScanError.WindowsError()
        else:
            try:
                subprocess.run('sudo service tor start', shell=True)
                if ua:

                    SubScan_utils.new_ip(0)

                    session = requests.session()
                    session.headers = {'User-Agent': ua[0]}
                    session.proxies = {}
                    session.proxies['http'] = 'socks5h://localhost:9050'
                    session.proxies['https'] = 'socks5h://localhost:9050'

                    return session

                else:

                    SubScan_utils.new_ip(0)

                    session = requests.session()
                    session.proxies = {}
                    session.proxies['http'] = 'socks5h://localhost:9050'
                    session.proxies['https'] = 'socks5h://localhost:9050'

                    return session

            except Exception:
                SubScan_utils.stop_tor_service()
                SubScanError.error()

    @staticmethod
    def new_ip(*p):
        with open("passwd.txt", 'r') as pswd:
            pswd = pswd.read()
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate(password=pswd)
                controller.signal(Signal.NEWNYM)
                proxies = {
                    "http": "socks5h://localhost:9050",
                    "https": "socks5h://localhost:9050",
                }
                reg = "[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}"
                if p:
                    print(
                        f"{color.magenta('[*]')} {color.white('New ip')} {color.blue(re.findall(reg, requests.get('http://httpbin.org/ip', proxies=proxies).text)[0])}")
        except:
            SubScanError.TorError()
    @staticmethod        
    def start_message():
        logo1 = color.white(""" 
                ,▄▄▄▄▄▄▄▄▄▄
             ╔▓███████████████▄▄
            ╨▀▀▀▀████████████████▄
           ,p@╖  ╙╣▀███████▓▀▀▀▀███╗
         ╓██████Ç é█████╣.⌐;p╖╖, '▀▓@
         ▓▀æ╝╨╩▓▀w@████',▄███████▌ ]▓
        [,)╥╓,,,▄▓█████@▀▓▀╨▀▓▓▀███▒╟
       ▄████████████████▄B▄▄,  '╜█▓▒[
      ╫▓▓▓██████████████████████▄▄φ▓[
      ⌐╙▀▀▀▀▐▄▀▀▀▀██▀██████████████▓C
      ▌  &█████r      '╠▓▄▀████████╜
      ]∩  ▀▀▀▀`  ▄   ▀█████▄,▀▀▀▀▀,
       ▓╙N▄▄w, "▀▀▀    ▀▀██▀▀    $'
       ]m\,▀▀▀██████▄▄▄▄,,, ╓² ╓@
        ▓Ç▓▓▓▓▄    '▀▀▀▀▀▀"  ▄▓`
         ▓╣▓▓██   ▓█▓▓▓▓╜ ,▄▀"
          ▓▓▓▓    ▓▓▓▓▓▒▄▓╜
           ╫▓▓   ▐▓▓▓╬▓▀
            ╙╜  ]╢Ñ╜╙
                    """)

        logo2 = color.blue("""
    .▄▄ · ▄• ▄▌▄▄▄▄· .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
    ▐█ ▀. █▪██▌▐█ ▀█▪▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
    ▄▀▀▀█▄█▌▐█▌▐█▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
    ▐█▄▪▐█▐█▄█▌██▄▪▐█▐█▄▪▐█▐███▌▐█▪ ▐▌██▐█▌
     ▀▀▀▀  ▀▀▀ ·▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪


    """)

        logo3 = color.yellow("""
                         ▄▄                                          
     ▄█▀▀▀█▄█           ▄██        ▄█▀▀▀█▄█                          
    ▄██    ▀█            ██       ▄██    ▀█                          
    ▀███▄   ▀███  ▀███   ██▄████▄ ▀███▄    ▄██▀██ ▄█▀██▄ ▀████████▄  
      ▀█████▄ ██    ██   ██    ▀██  ▀█████▄█▀  ████   ██   ██    ██  
    ▄     ▀██ ██    ██   ██     ██▄     ▀███      ▄█████   ██    ██  
    ██     ██ ██    ██   ██▄   ▄████     ███▄    ▄█   ██   ██    ██  
    █▀█████▀  ▀████▀███▄ █▀█████▀ █▀█████▀ █████▀▀████▀██▄████  ████▄
                                                                     

      """)

        logo4 = color.magenta("""
      ██████  █    ██  ▄▄▄▄     ██████   ▄████▄  ▄▄▄      ███▄    █ 
    ▒██    ▒  ██  ▓██▒▓█████▄ ▒██    ▒  ▒██▀ ▀█ ▒████▄    ██ ▀█   █ 
    ░ ▓██▄   ▓██  ▒██░▒██▒ ▄██░ ▓██▄    ▒▓█    ▄▒██  ▀█▄ ▓██  ▀█ ██▒
      ▒   ██▒▓▓█  ░██░▒██░█▀    ▒   ██▒▒▒▓▓▄ ▄██░██▄▄▄▄██▓██▒  ▐▌██▒
    ▒██████▒▒▒▒█████▓ ░▓█  ▀█▓▒██████▒▒░▒ ▓███▀ ▒▓█   ▓██▒██░   ▓██░
    ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░▒▒   ▓▒█░ ▒░   ▒ ▒ 
    ░ ░▒  ░  ░░▒░ ░ ░ ▒░▒   ░ ░ ░▒  ░     ░  ▒  ░ ░   ▒▒ ░ ░░   ░ ▒░
    ░  ░  ░   ░░░ ░ ░  ░    ░ ░  ░  ░   ░         ░   ▒     ░   ░ ░ 
          ░     ░      ░            ░   ░ ░           ░           ░ 

        """)

        logo_list = [logo1, logo2, logo3, logo4]
        logo_rand = random.randint(0, 3)
        print(logo_list[logo_rand])

    @staticmethod 
    def verify_url(url):
        if url.endswith("/"):
            return url
        else:
            url = url + "/"
            return url

    @staticmethod 
    def verify_url_for_get_ip(url):
        regex = "^https://|http://"
        url = re.sub(regex, '', url)
        if url.endswith("/"):
            url = url[:-1]
        return url

    @staticmethod 
    def hash_passwd_file(pswd="default", *m):
        def config(p1, p2, file, p4):
            if re.search(p1, file):
                r = re.sub(p1, p4, file)
            else:
                r = re.sub(p2, p4, file)
            return r

        if os.name == 'nt':
            SubScanError.WindowsError()
        else:
            if os.getuid() != 0:
                SubScanError.AdminError()
            else:
                out = subprocess.check_output(f'tor --hash-password {pswd}', shell=True)
                out = out.decode('utf-8').replace('\n', '')
                out = re.search(r"16[:]{1}[A-Z0-9]{10,}", out).group()
                with open(f'{SubScan_utils.get_path()}passwd.txt', 'w') as wp:
                    wp.write(str(pswd))
                wp.close()
                with open('/../etc/tor/torrc', 'r') as fi:
                    file = fi.read()
                    tor_reg = {
                        'with-#': {
                            'HashedControlPassword': "[#]{1}HashedControlPassword 16:[0-9A-Z]{1,}",
                            'CookieAuthentication': "[#]{1}CookieAuthentication 1",
                            'ControlPort': "[#]{1}ControlPort 9051",
                        },
                        'whithout-#': {
                            'HashedControlPassword': "HashedControlPassword 16:[0-9A-Z]{1,}",
                            'CookieAuthentication': "CookieAuthentication 1",
                            'ControlPort': "ControlPort 9051",
                        }
                    }
                    r = config(tor_reg['with-#']['HashedControlPassword'], tor_reg['whithout-#']['HashedControlPassword'], file, f"HashedControlPassword {out}")
                    r = config(tor_reg['with-#']['CookieAuthentication'], tor_reg['whithout-#']['CookieAuthentication'],
                               r, "CookieAuthentication 1")
                    r = config(tor_reg['with-#']['ControlPort'], tor_reg['whithout-#']['ControlPort'],
                               r, "ControlPort 9051")
                    with open('/../etc/tor/torrc', 'w') as f:
                        f.write(r)
                        f.close()
                    fi.close()

                    if m:
                        exit(color.green("\nFinish\n"))


class Network:

    class discover:
        @staticmethod
        def get_plage(netmask):
            compt = 0
            plage = Network.discover.addrtobin(netmask)
            for n in plage:
                if n == '0':
                    compt += 1

            return str(pow(2, compt)), compt

        @staticmethod
        def addrtobin(ip):
            r = [bin(int(x) + 256)[3:] for x in ip.split('.')]
            result = str()
            for v in r:
                result += v
            return str(result)

        @staticmethod
        def bintoaddr(binary):
            binary = [int(x, 2) for x in binary.split('.')]
            result = str()
            for v in binary:
                result += str(v) + "."
            return result[:-1]

        @staticmethod
        def getBroadcastAddr(ip, netmask):
            plage, compt = Network.discover.get_plage(netmask)
            ip = Network.discover.addrtobin(ip)
            ip = ip[:-compt] + '1' * compt
            compt2 = 0
            binary = str()
            for v in ip:
                if compt2 == 7:
                    compt2 = 0
                    binary += v + "."
                else:
                    compt2 += 1
                    binary += v
            binary = binary[:-1]
            addr = Network.discover.bintoaddr(binary)
            return addr

        @staticmethod
        def get_network_class(ip):
            compt = Network.discover.addrtobin(ip)
            if compt[0] == '0':
                return "A"
            elif compt[0:2] == '10':
                return "B"
            elif compt[0:2] == '11':
                if compt[2] == '1':
                    if compt[3] == '0':
                        return "D"
                    else:
                        return "E"

                else:
                    return "C"
            else:
                return None

    class scan_ports:
            port_compt = 0
            scan_result = str("\n")
            start = False
            finish = False

            @staticmethod
            def start_threads_scan():
                Network.scan_ports.start = True
                Network.scan_ports.finish = False

            @staticmethod
            def New_scan(ip):
                print(f"\nScanning {ip} ...\n")
                Network.scan_ports.port_compt = 0
                Network.scan_ports.scan_result = str("\n")
                Network.scan_ports.start = False

            @staticmethod
            def search_ports(ip, port, timeout,
                             thread=False):
                for p in port:
                    if thread:
                        while not Network.scan_ports.start:
                            pass
                    print(f"\r{color.red('[+]')} {color.blue(Network.scan_ports.port_compt)} {color.white('ports scanned')}", end='', flush=True)
                    Network.scan_ports.port_compt += 1
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    if sock.connect_ex((ip, p)) == 0:
                        try:
                            Network.scan_ports.scan_result += f"\n{color.white('Port :')} {color.yellow(p)} {color.magenta('/')} {color.white('Status :')} {color.blue('Open')} {color.magenta('/')} {color.white('Service :')} {color.green(socket.getservbyport(p))}"
                        except:
                            Network.scan_ports.scan_result += f"\n{color.white('Port :')} {color.yellow(p)} {color.magenta('/')} {color.white('Status :')} {color.blue('Open')} {color.magenta('/')} {color.white('Service :')} {color.green('Unknow')}"
                    sock.close()
                Network.scan_ports.finish = True


            @staticmethod
            def one(ip='127.0.0.1',
                    port='80',
                    timeout=1):
                Network.scan_ports.New_scan(ip)
                Network.scan_ports.search_ports(ip, port, timeout)
                return Network.scan_ports.scan_result

            @staticmethod
            def fast(ip='127.0.0.1',
                     timeout=0.5):
                Network.scan_ports.New_scan(ip)
                l = [20, 21, 22, 23, 25, 80, 110, 137, 135, 139, 143, 389, 443, 445, 993, 995, 1433, 3306, 5357, 5900, 6667]
                Network.scan_ports.search_ports(ip, l, timeout)
                return Network.scan_ports.scan_result

            @staticmethod
            def medium(ip='127.0.0.1',
                       timeout=0.5):
                Network.scan_ports.New_scan(ip)
                ports = range(1500)
                Network.scan_ports.search_ports(ip, ports, timeout)
                return Network.scan_ports.scan_result

            @staticmethod
            def full(ip='127.0.0.1',
                     timeout=0.5):
                Network.scan_ports.New_scan(ip)
                ports = range(8000)
                Network.scan_ports.search_ports(ip, ports, timeout)
                return Network.scan_ports.scan_result

            @staticmethod
            def custom(ip='127.0.0.1',
                       r='1-6500',
                       timeout=0.1):

                Network.scan_ports.New_scan(ip)
                time.sleep(0.5)
                r = r.split('-')
                r = range(int(r[0]), int(r[1]))
                r2 = int(len(r) / 2)
                threading.Thread(target=Network.scan_ports.search_ports, args=(ip, r[:r2], timeout, True)).start()
                threading.Thread(target=Network.scan_ports.search_ports, args=(ip, r[r2:], timeout, True)).start()
                Network.scan_ports.start_threads_scan()
                while not Network.scan_ports.finish:
                    pass
                return Network.scan_ports.scan_result


def linux_search(site=None,
                 file='dl.txt',
                 timeout=None,
                 extension=None,
                 ua=None,
                 method=None):

    try:
        if ua in User_agent.list:
            ua = eval(ua)

        if ua == None:
            session = SubScan_utils.new_session()
        else:
            print(color.blue('[-]'), color.yellow('User-Agent : '), color.white(ua))
            session = SubScan_utils.new_session(ua)

        site = SubScan_utils.verify_url(site)
        compt = 0

        with open(file, 'r') as file:
            if method == "full":
                if extension == None:
                    for line in file:
                        compt += 1
                        if compt % 40 == 0:
                            SubScan_utils.new_ip(0)
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1]
                        r = session.get(url)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                        else:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.pastel_red(url)} {color.white('is invalid ! Statut :')} {color.blue(r.status_code)}")
                else:
                    for line in file:
                        compt += 1
                        if compt % 40 == 0:
                            SubScan_utils.new_ip(0)
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1] + extension
                        r = session.get(url)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                        else:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.pastel_red(url)} {color.white('is invalid ! Statut :')} {color.blue(r.status_code)}")

            elif method == None:
                if extension == None:
                    for line in file:
                        compt += 1
                        if compt % 40 == 0:
                            SubScan_utils.new_ip(0)
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1]
                        r = session.get(url)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                else:
                    for line in file:
                        compt += 1
                        if compt % 40 == 0:
                            SubScan_utils.new_ip(0)
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1] + extension
                        r = session.get(url)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
            else:
                    SubScanError.MethodError()

            SubScan_utils.stop_tor_service()
    except KeyboardInterrupt:
        SubScanError.keyboard_exit()


def windows_search(site=None,
                   file='dl.txt',
                   timeout=None,
                   extension=None,
                   ua=None,
                   method=None):
    try:
        if ua in User_agent.list:
            ua = eval(ua)

        if ua == None:
            headers = None
        else:
            print(color.blue('[-]'), color.yellow('User-Agent : '), color.white(ua))
            headers = {'User-Agent': ua}


        site = SubScan_utils.verify_url(site)
        with open(file, 'r') as file:

            if method == "full":
                if extension == None:
                    for line in file:
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1]
                        r = requests.get(url, headers=headers)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                        else:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.pastel_red(url)} {color.white('is invalid ! Statut :')} {color.blue(r.status_code)}")
                else:
                    for line in file:
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1] + extension
                        r = requests.get(url, headers=headers)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                        else:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.pastel_red(url)} {color.white('is invalid ! Statut :')} {color.blue(r.status_code)}")

            elif method == None:
                if extension == None:
                    for line in file:
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1]
                        r = requests.get(url, headers=headers)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                else:
                    for line in file:
                        if timeout != None:
                            time.sleep(float(timeout))
                        url = site + line[:-1] + extension
                        r = requests.get(url, headers=headers)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
            else:
                SubScanError.MethodError()
    except KeyboardInterrupt:
        SubScanError.keyboard_exit()


def windows_search_NP(site=None,
                      file='dl.txt',
                      timeout=None,
                      extension=None,
                      ua=None):
    try:
        if ua in User_agent.list:
            ua = eval(ua)

        if ua == None:
            headers = None
        else:
            print(color.blue('[-]'), color.yellow('User-Agent : '), color.white(ua))
            headers = {'User-Agent': ua}

        site = SubScan_utils.verify_url(site)
        list = []
        with open(file, 'r') as file:
            if extension == None:
                for line in file:
                    if timeout != None:
                        time.sleep(float(timeout))
                    url = site + line[:-1]
                    r = requests.get(url, headers=headers)
                    if r.status_code == 200:
                        list.append(f"{url} : valid")
                return list
            else:
                for line in file:
                    if timeout != None:
                        time.sleep(float(timeout))
                    url = site + line[:-1] + extension
                    r = requests.get(url, headers=headers)
                    if r.status_code == 200:
                        list.append(f"{url} : valid")
                return list
    except KeyboardInterrupt:
        return list
        SubScanError.keyboard_exit()


def linux_search_NP(site=None,
                    file='dl.txt',
                    timeout=None,
                    extension=None,
                    ua=None):
    try:
        if ua in User_agent.list:
            ua = eval(ua)

        if ua == None:
            session = SubScan_utils.new_session()
        else:
            print(color.blue('[-]'), color.yellow('User-Agent : '), color.white(ua))
            session = SubScan_utils.new_session(ua)

        site = SubScan_utils.verify_url(site)
        list = []
        compt = 0

        with open(file, 'r') as file:
            if extension == None:
                for line in file:
                    compt += 1
                    if compt % 40 == 0:
                        SubScan_utils.new_ip()
                    if timeout != None:
                        time.sleep(float(timeout))
                    url = site + line[:-1]
                    r = session.get(url)
                    if r.status_code == 200:
                        list.append(url)
                return list
            else:
                for line in file:
                    compt += 1
                    if compt % 40 == 0:
                        SubScan_utils.new_ip()
                    if timeout != None:
                        time.sleep(float(timeout))
                    url = site + line[:-1]
                    r = session.get(url)
                    if r.status_code == 200:
                        list.append(url)
                return list
            SubScan_utils.stop_tor_service()
    except KeyboardInterrupt:
        return list
        SubScanError.keyboard_exit()


def DNS_enum(site=None,
             file='dl.txt',
             timeout=None,
             ua=None,
             method=None):

    try:
        regex = "^(https://)"
        regex2 = "^(http://)"
        if re.match(regex, site):
            site = site.replace('https://', '')
            r1 = 'https://'
        elif re.match(regex2, site):
            site = site.replace('http://', '')
            r1 = 'http://'
        else:
            site = site.replace('https://', '')
            r1 = 'https://'

        if ua in User_agent.list:
            ua = eval(ua)

        if ua == None:
            session = SubScan_utils.new_session()
        else:
            print(color.blue('[-]'), color.yellow('User-Agent : '), color.white(ua))
            session = SubScan_utils.new_session(ua)

        site = SubScan_utils.verify_url(site)
        compt = 0

        with open(file, 'r') as file:
            if method == "full":
                for line in file:
                    compt += 1
                    if compt % 40 == 0:
                        SubScan_utils.new_ip(0)
                    if timeout != None:
                        time.sleep(float(timeout))
                    url = f"{r1}{line[:-1]}.{site}"
                    try:
                        r = session.get(url)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                        else:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.pastel_red(url)} {color.white('is invalid ! Statut :')} {color.blue(r.status_code)}")
                    except:
                        print(
                            f"{color.blue('[+]')} {color.yellow('Url :')} {color.magenta(url)} {color.white('is invalid ! Statut :')} {color.blue('Nonexistent')}")
                        pass


            elif method == None:
                for line in file:
                    compt += 1
                    if compt % 40 == 0:
                        SubScan_utils.new_ip(0)
                    if timeout != None:
                        time.sleep(float(timeout))
                    url = f"{r1}{line[:-1]}.{site}"
                    try:
                        r = session.get(url)
                        if r.status_code == 200:
                            print(
                                f"{color.blue('[+]')} {color.yellow('Url :')} {color.green(url)} {color.white('is valid ! Statut :')} {color.blue(r.status_code)}")
                    except:
                        pass
            else:
                SubScanError.MethodError()

            SubScan_utils.stop_tor_service()

    except KeyboardInterrupt:
        SubScanError.keyboard_exit()


def get_host_ip(site):
    site = SubScan_utils.verify_url_for_get_ip(site)
    try:
        ip = socket.gethostbyname(site)
        print(f"{color.white(f'The')} {color.green(site)}{color.white(' ip is :')} {color.blue(ip)}")
    except:
        SubScanError.UrlError()



def get_routes(url,
               ua=None):

    if ua in User_agent.list:
        ua = eval(ua)

    if ua == None:
        session = SubScan_utils.new_session()
    else:
        print(color.blue('[-]'), color.yellow('User-Agent : '), color.white(ua))
        session = SubScan_utils.new_session(ua)

    try:
        r = session.get(url)
        r = r.history
        time.sleep(1)
        if len(r) == 0:
            print(color.pastel_red("[!]"), color.blue("There is no redirection on this page"))
            SubScan_utils.stop_tor_service()
        else:
            for urls in range(len(r)):
                u = r[urls].url
                try:
                    ip = socket.gethostbyname(str(u.split('/')[2]))
                    print(
                        f"{color.yellow('[')}{color.blue(urls)}{color.yellow(']')} {color.white('Url :')} {color.green(r[urls].url)} {color.white('| Server IP : ')}{color.magenta(ip)}")
                except socket.gaierror:
                    print(
                        f"{color.yellow('[')}{color.blue(urls)}{color.yellow(']')} {color.white('Url :')} {color.green(r[urls].url)}")
            SubScan_utils.stop_tor_service()

    except requests.exceptions.RequestException:
        SubScan_utils.stop_tor_service()
        SubScanError.UrlError()

class terminal_color:

    theme_list = {
       'Sunlight' : f"{color.yellow('|')}{color.magenta('-')}{color.yellow('>')}  ",
       'Ice And Fire' : f"{color.blue('|')}{color.red('~')}{color.blue('>')}  ",
       'JokR' : f"{color.magenta('$')}{color.green('~')}{color.magenta('>')}  ",
       'Earth' : f"{color.blue('(')}{color.green('~')}{color.blue(')')}{color.magenta('>')}  ",
       'Extra' : '{}{}{}{}{}  '.format(color.pastel_red("┌─["), color.white(" SubScan "), color.pastel_red("""]\n└─"""), color.white("$"), color.pastel_red(">"))
    }

    @staticmethod
    def new_config(color):
        with open('SubScan_color.config', 'w') as file:
            file.write(color)
            file.close

    @staticmethod
    def config():
        with open('SubScan_color.config', 'r') as file:
            r = file.readlines()
            if r == []:
                terminal_color.new_config('Sunlight')
                c = terminal_color.theme_list.get('Sunlight')
                return c
            else:
                c = terminal_color.theme_list.get(r[0])
                return c

    @staticmethod
    def choice():
        presentation = f"\n[0]    {color.red('Exit the color configuration menu')}\n\n"
        for theme in terminal_color.theme_list:
            presentation += f"[{list(terminal_color.theme_list).index(theme) + 1}]    {theme}\n{terminal_color.theme_list.get(theme)}\n\n"
        print(presentation)
        while True:
            print(color.green('?>  '), end='')
            result = input("\b")
            if result == '0':
                break
            else:
                try:
                    terminal_color.new_config(list(terminal_color.theme_list)[int(result) - 1])
                    break
                except:
                    print(color.red("Please Enter a valid number !\n"))


if __name__ == '__main__':
    try:
        c = terminal_color.config()
    except FileNotFoundError:
        terminal_color.new_config('Sunlight')
        c = terminal_color.config()
    SubScan_utils.clear()
    SubScan_utils.start_message()
    while True:
        print(c, end='')
        command = input('\b')
        if command.lower().replace(' ', '') == 'exit':
            break
        elif command.lower().replace(' ', '') == 'shortcut':
            SubScan_utils.shortcut()
        elif command.lower().replace(' ', '') == 'theme':
            terminal_color.choice()
            c = terminal_color.config()
        elif command.lower().replace(' ', '') == 'clear':
            SubScan_utils.clear()
        elif command.lower() == 'ua list':
            for UserAgents in User_agent.list:
                print(color.green(UserAgents), end='\n')
        elif command.lower() == 'help':
            print(color.magenta('Look at https://github.com/Negative-py/SubScan for more informations'))
        else:
            try:
                exec(command)
                print('\n')
            except :
                print(color.red('Please Enter a valid command\n'))
        
    exit()
