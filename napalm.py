from napalm import get_network_driver

hosts = [['10.10.10.2','candidate2'],['10.10.10.3','candidate3'],['10.10.10.4','candidate4'],['10.10.10.5','candidate5'],['10.10.10.6','candidate6'],['10.10.10.7','candidate7'],['10.10.10.8','candidate8'],['10.10.10.9','candidate9']]

for host in hosts:
        driver = get_network_driver("ios")
        others = {
                        "secret" : "proposal123",
                        "dest_file_system" : "nvram:",
                        'inline_transfer' : True
                        }
        device = driver(hostname=host[0], username='laras', password='proposal123',optional_args=others)
        device.open()
        print ("Login Sukses di {0}".format(host[0]))

        device.load_merge_candidate(filename=host[1])
        print ("Load Success {0}".format(host[1]))
        device.commit_config()
        print ("Done")

device.close()
