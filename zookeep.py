from kazoo.client import KazooClient
import time


print("Instantiating a KazooClient object")
zk = KazooClient(hosts="127.0.0.1:2181")
print("Connecting to the ZooKeeper Server")
zk.start()
print("client current state = {}".format(zk.state))


path = "/dischm"
if not zk.exists(path):
    zk.create(str ("/") + "dischm", value=bytes("{}", 'utf-8'), ephemeral=True, makepath=True)
    print ("diectory created")

if not zk.exists(path):
    print ("SHOULD NOT SEE THIS")


path = "/dischm2"
if not zk.exists(path):
    zk.create(str ("/") + "dischm2", value=bytes("{}", 'utf-8'), ephemeral=True, makepath=True)
    print ("diectory created")

if not zk.exists(path):
    print ("SHOULD NOT SEE THIS")


path = "/numPubs"
if not zk.exists(path):
    zk.create(str("/") + "numPubs", value=bytes("0", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")

if not zk.exists(path):
    print("SHOULD NOT SEE THIS")


path = "/numSubs"
if not zk.exists(path):
    zk.create(str("/") + "numSubs", value=bytes("0", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")

if not zk.exists(path):
    print("SHOULD NOT SEE THIS")


path = "/curDiscovery"
if not zk.exists(path):
    zk.create(str("/") + "curDiscovery", value=bytes("tcp://localhost:5555", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")

if not zk.exists(path):
    print("SHOULD NOT SEE THIS")

path = "/disclist"
if not zk.exists(path):
    zk.create(str("/") + "disclist", value=bytes("", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")

if not zk.exists(path):
    print("SHOULD NOT SEE THIS")


path = "/curpubset"
if not zk.exists(path):
    zk.create(str("/") + "curpubset", value=bytes("{}", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")

if not zk.exists(path):
    print("SHOULD NOT SEE THIS")


path = "/curbroker"
if not zk.exists(path):
    zk.create(str("/") + "curbroker", value=bytes("localhost 5570", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")


path = "/brokerlist"
if not zk.exists(path):
    zk.create(str("/") + "brokerlist", value=bytes("", 'utf-8'), ephemeral=True, makepath=True)
    print("diectory created")



print ("Finished creating directories")


while (True):
    time.sleep(5)

