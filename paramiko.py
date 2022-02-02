import paramiko
import time
def r1():
    ip_address ="10.10.10.2"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 1.1.1.1 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.10.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.9.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 25\n")
    conn.send("neighbor 192.168.10.2 remote-as 35\n")
    conn.send("network 1.1.1.1 mask 255.255.255.255\n")
    conn.send("network 192.168.10.0 mask 255.255.255.0\n")
    conn.send("network 192.168.9.0 mask 255.255.255.0\n")
    print ("DONE")
    time.sleep(3)
r1()

def r2():
    ip_address ="10.10.10.3"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 2.2.2.2 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.40.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.20.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/0\n")
    conn.send("ip add 192.168.30.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/1\n")
    conn.send("ip add 192.168.10.2 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 35\n")
    conn.send("neighbor 192.168.10.1 remote-as 25\n")
    conn.send("neighbor 192.168.40.2 remote-as 35\n")
    conn.send("neighbor 192.168.20.2 remote-as 35\n")
    conn.send("neighbor 192.168.30.2 remote-as 35\n")
    conn.send("network 2.2.2.2 mask 255.255.255.255\n")
    conn.send("network 192.168.40.0 mask 255.255.255.0\n")
    conn.send("network 192.168.20.0 mask 255.255.255.0\n")
    conn.send("network 192.168.30.0 mask 255.255.255.0\n")
    conn.send("network 192.168.10.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r2()

def r3():
    ip_address ="10.10.10.4"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 3.3.3.3 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.49.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.50.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 55\n")
    conn.send("neighbor 192.168.50.2 remote-as 35\n")
    conn.send("network 3.3.3.3 mask 255.255.255.255\n")
    conn.send("network 192.168.49.0 mask 255.255.255.0\n")
    conn.send("network 192.168.50.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r3()

def r4():
    ip_address ="10.10.10.5"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 4.4.4.4 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.40.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.70.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/1\n")
    conn.send("ip add 192.168.50.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/0\n")
    conn.send("ip add 192.168.60.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 35\n")
    conn.send("neighbor 192.168.50.1 remote-as 55\n")
    conn.send("neighbor 192.168.40.1 remote-as 35\n")
    conn.send("neighbor 192.168.70.2 remote-as 35\n")
    conn.send("neighbor 192.168.60.2 remote-as 35\n")
    conn.send("network 4.4.4.4 mask 255.255.255.255\n")
    conn.send("network 192.168.50.0 mask 255.255.255.0\n")
    conn.send("network 192.168.40.0 mask 255.255.255.0\n")
    conn.send("network 192.168.70.0 mask 255.255.255.0\n")
    conn.send("network 192.168.60.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r4()

def r5():
    ip_address ="10.10.10.6"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 5.5.5.5 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f2/1\n")
    conn.send("ip add 192.168.30.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.60.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/0\n")
    conn.send("ip add 192.168.80.1 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.90.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 35\n")
    conn.send("neighbor 192.168.30.1 remote-as 35\n")
    conn.send("neighbor 192.168.60.1 remote-as 35\n")
    conn.send("neighbor 192.168.80.2 remote-as 35\n")
    conn.send("neighbor 192.168.90.2 remote-as 65\n")
    conn.send("network 5.5.5.5 mask 255.255.255.255\n")
    conn.send("network 192.168.60.0 mask 255.255.255.0\n")
    conn.send("network 192.168.30.0 mask 255.255.255.0\n")
    conn.send("network 192.168.80.0 mask 255.255.255.0\n")
    conn.send("network 192.168.90.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r5()

def r6():
    ip_address ="10.10.10.7"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 6.6.6.6 255.255.255.255\n")
    conn.send("no sh\n")

    conn.send("int f1/1\n")
    conn.send("ip add 192.168.80.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/1\n")
    conn.send("ip add 192.168.70.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f2/0\n")
    conn.send("ip add 192.168.20.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.100.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 35\n")
    conn.send("neighbor 192.168.20.1 remote-as 35\n")
    conn.send("neighbor 192.168.70.1 remote-as 35\n")
    conn.send("neighbor 192.168.80.1 remote-as 35\n")
    conn.send("neighbor 192.168.100.2 remote-as 45\n")
    conn.send("network 6.6.6.6 mask 255.255.255.255\n")
    conn.send("network 192.168.20.0 mask 255.255.255.0\n")
    conn.send("network 192.168.70.0 mask 255.255.255.0\n")
    conn.send("network 192.168.80.0 mask 255.255.255.0\n")
    conn.send("network 192.168.100.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r6()

def r7():
    ip_address ="10.10.10.8"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 7.7.7.7 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.100.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.101.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 45\n")
    conn.send("neighbor 192.168.100.1 remote-as 35\n")
    conn.send("network 7.7.7.7 mask 255.255.255.255\n")
    conn.send("network 192.168.101.0 mask 255.255.255.0\n")
    conn.send("network 192.168.100.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r7()

def r8():
    ip_address ="10.10.10.9"
    username = "laras"
    password = "proposal123"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    print ("Login Sukses di {0}".format(ip_address))
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send("ip add 8.8.8.8 255.255.255.255\n")
    conn.send("no sh\n")
    conn.send("int f1/1\n")
    conn.send("ip add 192.168.90.2 255.255.255.0\n")
    conn.send("no sh\n")
    conn.send("int f1/0\n")
    conn.send("ip add 192.168.89.1 255.255.255.0\n")
    conn.send("no sh\n")
    time.sleep(1)

    conn.send("router bgp 65\n")
    conn.send("neighbor 192.168.90.1 remote-as 35\n")
    conn.send("network 8.8.8.8 mask 255.255.255.255\n")
    conn.send("network 192.168.89.0 mask 255.255.255.0\n")
    conn.send("network 192.168.90.0 mask 255.255.255.0\n")
    print("DONE")
    time.sleep(3)
r8()
