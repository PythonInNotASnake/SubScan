__author__ = "Negative.py"
__discord__ = "</белый_хакер>#4103"

# Importing modules
try:
    import sys
    import time
    from stem import Signal
    from stem.control import Controller
    import colorama
    import random
    import requests
    import socket
    import re
    import stem
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
    def get_path():
        path = str()

        for directory in __file__.split('/')[0:-1]:
            path = path + directory + '/'


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
    def hash_passwd_file(pswd, *m):
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


def linux_search(site, file, timeout, extension, ua, method):
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
            exit()
    except KeyboardInterrupt:
        SubScanError.keyboard_exit()



def windows_search(site, file, timeout, extension, ua, method):
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
            exit()
    except KeyboardInterrupt:
        SubScanError.keyboard_exit()

def windows_search_NP(site, file, timeout, extension, ua):
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


def linux_search_NP(site, file, timeout, extension, ua):
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


def DNS_enum(site, file, timeout, ua, method):
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
            exit()
    except KeyboardInterrupt:
        SubScanError.keyboard_exit()

def get_host_ip(site):
    site = SubScan_utils.verify_url_for_get_ip(site)
    try:
        ip = socket.gethostbyname(site)
        print(f"{color.white(f'The')} {color.green(site)}{color.white(' ip is :')} {color.blue(ip)}")
        exit()
    except:
        SubScanError.Url()

def scan_ports(ip, value, t, thread):
    value = value.split('-')
    thread = int(thread)
    port_list = []
    start_time = time.time()

    def search_ports(ip, port):
        for p in port:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if t != None:
                    sock.settimeout(float(t))
                result = sock.connect_ex((ip, p))
                if result == 0:
                    port_list.append(int(p))
                sock.close()
            except OSError:
                pass

    compt = 0
    for num in range(int(value[0]), int(value[1]) + 1, thread):
        list = []
        compt += 1
        for nums in range(0, thread - 1):
            list.append(num + nums)
        if compt % 350 == 0:
            time.sleep(0.5)
        threading.Thread(target=search_ports, args=(ip, list)).start()
    time.sleep(0.5)
    for p in sorted(port_list):
        try:
            print(
                f"{color.blue('[+]')} {color.white('Port')} {color.yellow(p)} {color.magenta('/')} {color.green(socket.getservbyport(p))} {color.white(': Open')}")
        except OSError:
            print(
                f"{color.blue('[+]')} {color.white('Port')} {color.yellow(p)} {color.magenta('/')} {color.green('unknow')} {color.white(': Open')}")
    if os.name == 'nt':
        print(f"\n{color.black(f'[--(| Time : {round(float(time.time() - start_time), 4)} s |)--]')}\n")
    else:
        print(f"\u001b[107m\n{color.black(f'[--(| Time : {round(float(time.time() - start_time), 4)} s |)--]')}\n")
    exit()


def get_routes(url, ua):

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
        exit()

    except requests.exceptions.RequestException:
        SubScan_utils.stop_tor_service()
        SubScanError.UrlError()
