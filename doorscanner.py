from socket import *
from struct import pack
import argparse
import time


def scan(target, port, timeout=1):
    client = socket(AF_INET, SOCK_STREAM)
    client.setsockopt(SOL_SOCKET, SO_LINGER, pack('ii', 1, 0))
    client.settimeout(timeout)
    try:
        client.connect((target, port))
        client.close()
        print(port, 'open')
    except:
        pass


parser = argparse.ArgumentParser(prog='DoorScanner', description='Simple port scanner')
parser.add_argument('-t', '--target')
parser.add_argument('-p', '--port')
parser.add_argument('-T', '--timeout')
args = parser.parse_args()
start_time = time.time()

print(f'''    ___                 __                                 
   /   \___   ___  _ __/ _\ ___ __ _ _ __  _ __   ___ _ __ 
  / /\ / _ \ / _ \| '__\ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 / /_// (_) | (_) | |  _\ \ (_| (_| | | | | | | |  __/ |   
/___,' \___/ \___/|_|  \__/\___\__,_|_| |_|_| |_|\___|_|   
                                                           
starting DoorScanner at {time.localtime().tm_hour}:{time.localtime().tm_min}''')

try:
    args.timeout = float(args.timeout)
except:
    args.timeout = 1

if args.port:
    try:
        args.port = int(args.port)
        scan(args.target, args.port, float(args.timeout))
    except:
        if '-' in args.port:
            try:
                first_port = int(args.port.split('-')[0])
                final_port = int(args.port.split('-')[1])
            except:
                quit()
            if first_port > final_port:
                temp_port = final_port
                final_port = first_port
                first_port = temp_port
            for port in range(first_port, final_port+1):
                scan(args.target, port, float(args.timeout))
        elif ',' in args.port:
            ports = args.port.split(',')
            for port in ports:
                scan(args.target, int(port), float(args.timeout))

print(f'{args.target} scanned in {(time.time() - start_time):.2f} seconds')
