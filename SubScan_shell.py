import SubScan
import colorama
import os
import sys

if __name__ == "__main__":
    colorama.init()
    argument = sys.argv
    os.system('clear')
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
                                    SubScan.linux_search(url, file, 0.5, extension, str(user_agent), 'full')
                                else:
                                    SubScan.linux_search(url, file, 0.5, extension, None, 'full')
                            else:
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, 0.5, None, str(user_agent), 'full')
                                else:
                                    SubScan.linux_search(url, file, 0.5, None, None, 'full')
                        else:
                            if '-e' in argument:
                                extension = argument[argument.index("-e") + 1]
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, 0.5, extension, str(user_agent), None)
                                else:
                                    SubScan.linux_search(url, file, 0.5, extension, None, None)
                            else:
                                if '-a' in argument:
                                    user_agent = argument[argument.index("-a") + 1]
                                    SubScan.linux_search(url, file, 0.5, None, str(user_agent), None)
                                else:
                                    SubScan.linux_search(url, file, 0.5, None, None, None)
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
                            SubScan.scan_ports(ip, r, timeout, 12)
                    else:
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, r, 0.25, threads)
                        else:
                            SubScan.scan_ports(ip, r, 0.25, 12)
                else:
                    if '-t' in argument:
                        timeout = argument[argument.index('-t') + 1]
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, '1-9000', timeout, threads)
                        else:
                            SubScan.scan_ports(ip, '1-9000', timeout, 12)
                    else:
                        if '-tn' in argument:
                            threads = argument[argument.index('-tn') + 1]
                            SubScan.scan_ports(ip, '1-9000', 0.25, threads)
                        else:
                            SubScan.scan_ports(ip, '1-9000', 0.25, 12)
            else:
                SubScan.SubScan_utils.invalid_argument()

        elif argument[1] == '-tp':
            if '-p' in argument:
                pswd = argument[argument.index('-p') + 1]
                if '-h' in argument:
                    hpswd = argument[argument.index('-h') + 1]
                    SubScan.SubScan_utils.hash_passwd_file(pswd, hpswd, True)
                else:
                    SubScan.SubScan_utils.invalid_argument()
            else:
                SubScan.SubScan_utils.invalid_argument()

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
                                SubScan.DNS_enum(url, file, 0.5, str(user_agent), 'full')
                            else:
                                SubScan.DNS_enum(url, file, 0.5, str(user_agent), None)        
                        else: 
                            if '-f' in argument:
                                SubScan.DNS_enum(url, file, 0.5, None, 'full')
                            else:
                                SubScan.DNS_enum(url, file, 0.5, None, None)
                else:
                    SubScan.SubScan_utils.invalid_argument()
            else:
                SubScan.SubScan_utils.invalid_argument()

        elif argument[1] == '-route':
            if '-u' in argument:
                url = argument[argument.index('-u') + 1]
                if '-a' in argument:
                    user_agent = argument[argument.index("-a") + 1]
                    SubScan.get_routes(url, str(user_agent))
                else:
                    SubScan.get_routes(url, None)
            else:
                SubScan.SubScan_utils.invalid_argument()

        else:
            SubScan.SubScan_utils.invalid_argument()

    except KeyboardInterrupt:
        SubScan.SubScan_utils.keyboard_exit()

    except IndexError:
        SubScan.SubScan_utils.invalid_argument()