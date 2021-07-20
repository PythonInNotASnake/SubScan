import SubScan
import colorama
import sys
import subprocess

if __name__ == "__main__":
    colorama.init()
    argument = sys.argv
    subprocess.run('clear', shell=True)
    try:
        SubScan.SubScan_utils.start_message()
        if argument[1] == "-find":
            if '-u' in argument:
                url = argument[argument.index('-u') + 1]
                if '-w' in argument:
                    file = argument[argument.index("-w") + 1]
                    if '-t' in argument:
                        timeout = argument[argument.index("-t") + 1]
                        if '-f' in argument:
                            if '-e' in argument:
                                extension = argument[argument.index("-e") + 1]
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, timeout, extension, str(user_agent), 'full')
                                else:
                                    SubScan.linux_search(url, file, timeout, extension, None, 'full')
                            else:
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, timeout, None, str(user_agent), 'full')
                                else:
                                    SubScan.linux_search(url, file, timeout, None, None, 'full')
                        else:
                            if '-e' in argument:
                                extension = argument[argument.index("-e") + 1]
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, timeout, extension, str(user_agent), None)
                                else:
                                    SubScan.linux_search(url, file, timeout, extension, None, None)
                            else:
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, timeout, None, str(user_agent), None)
                                else:
                                    SubScan.linux_search(url, file, timeout, None, None, None)
                    else:
                        if '-f' in argument:
                            if '-e' in argument:
                                extension = argument[argument.index("-e") + 1]
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, None, extension, str(user_agent), 'full')
                                else:
                                    SubScan.linux_search(url, file, None, extension, None, 'full')
                            else:
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, None, None, str(user_agent), 'full')
                                else:
                                    SubScan.linux_search(url, file, None, None, None, 'full')
                        else:
                            if '-e' in argument:
                                extension = argument[argument.index("-e") + 1]
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, None, extension, str(user_agent), None)
                                else:
                                    SubScan.linux_search(url, file, None, extension, None, None)
                            else:
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, None, None, str(user_agent), None)
                                else:
                                    SubScan.linux_search(url, file, None, None, None, None)
                else:
                    SubScan.SubScan_utils.invalid_argument()
            else:
                SubScan.SubScan_utils.invalid_argument()
        elif argument[1] == "-ip":
            if '-u' in argument:
                url = argument[argument.index('-u') + 1]
                SubScan.get_host_ip(url)
            else:
                SubScan.SubScan_utils.invalid_argument()

        elif argument[1] == '-scan':
            if '-i' in argument:
                ip = argument[argument.index('-i') + 1]
                if '-r' in argument:
                    r = argument[argument.index('-r') + 1]
                    if '-t' in argument:
                        timeout = argument[argument.index('-t') + 1]
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, r, timeout, threads)
                        else:
                            SubScan.scan_ports(ip, r, timeout, 2)
                    else:
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, r, 1, threads)
                        else:
                            SubScan.scan_ports(ip, r, 1, 2)
                else:
                    if '-t' in argument:
                        timeout = argument[argument.index('-t') + 1]
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, '1-9000', timeout, threads)
                        else:
                            SubScan.scan_ports(ip, '1-9000', timeout, 2)
                    else:
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, '1-9000', 1, threads)
                        else:
                            SubScan.scan_ports(ip, '1-9000', 1, 2)
            else:
                SubScan.SubScanError.invalid_argumentError()

        elif argument[1] == '-tp':
            if '-p' in argument:
                pswd = argument[argument.index('-p') + 1]
                SubScan.SubScan_utils.hash_passwd_file(pswd, True)
            else:
                SubScan.SubScanError.invalid_argumentError()

        elif argument[1] == '-dns':
            if '-u' in argument:
                url = argument[argument.index('-u') + 1]
                if '-w' in argument:
                    file = argument[argument.index("-w") + 1]
                    if '-t' in argument:
                        timeout = argument[argument.index("-t") + 1]
                        if '-a' in argument:
                            user_agent = argument[argument.index("-a") + 1]
                            if '-f' in argument:
                                SubScan.DNS_enum(url, file, timeout, str(user_agent), 'full')
                            else:
                                SubScan.DNS_enum(url, file, timeout, str(user_agent), None)        
                        else: 
                            if '-f' in argument:
                                SubScan.DNS_enum(url, file, timeout, None, 'full')
                            else:
                                SubScan.DNS_enum(url, file, timeout, None, None)
                    else:
                        if '-a' in argument:
                            user_agent = argument[argument.index("-a") + 1]
                            if '-f' in argument:
                                SubScan.DNS_enum(url, file, None, str(user_agent), 'full')
                            else:
                                SubScan.DNS_enum(url, file, None, str(user_agent), None)
                        else: 
                            if '-f' in argument:
                                SubScan.DNS_enum(url, file, None, None, 'full')
                            else:
                                SubScan.DNS_enum(url, file, None, None, None)
                else:
                    SubScan.SubScanError.invalid_argumentError()
            else:
                SubScan.SubScanError.invalid_argumentError()

        elif argument[1] == '-route':
            if '-u' in argument:
                url = argument[argument.index('-u') + 1]
                if '-a' in argument:
                    user_agent = argument[argument.index("-a") + 1]
                    SubScan.get_routes(url, str(user_agent))
                else:
                    SubScan.get_routes(url, None)
            else:
                SubScan.SubScanError.invalid_argumentError()

        else:
            SubScan.SubScanError.invalid_argumentError()

    except KeyboardInterrupt:
        SubScan.SubScanError.invalid_argumentError()

    except IndexError:
        SubScan.SubScanError.invalid_argumentError()
