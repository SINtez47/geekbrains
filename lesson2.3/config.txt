Router0
Router#configure terminal
Router(config)#int fa5/0
Router(config-if)#ip addr 172.16.0.1 255.255.0.0
Router(config-if)#no shut
Router(config-if)#ex
Router(config)#int fa4/0
Router(config-if)#ip addr 172.17.0.1 255.255.0.0
Router(config-if)#no shut
Router(config-if)#ex
Router(config-if)#ip route 192.168.3.0 255.255.255.0 172.16.0.2
Router(config-if)#ip route 192.168.2.0 255.255.255.0 172.17.0.2

Router2
Router#configure terminal
Router(config)#int fa5/0
Router(config-if)#ip addr 172.16.0.2 255.255.0.0
Router(config-if)#no shut
Router(config-if)#ex
Router(config)#int fa4/0
Router(config-if)#ip addr 172.18.0.1 255.255.0.0
Router(config-if)#no shut
Router(config-if)#ex
Router(config-if)#ip route 192.168.1.0 255.255.255.0 172.16.0.1
Router(config-if)#ip route 192.168.2.0 255.255.255.0 172.18.0.2

Router1
Router#configure terminal
Router(config)#int fa5/0
Router(config-if)#ip addr 172.18.0.2 255.255.0.0
Router(config-if)#no shut
Router(config-if)#ex
Router(config)#int fa4/0
Router(config-if)#ip addr 172.17.0.2 255.255.0.0
Router(config-if)#no shut
Router(config-if)#ex
Router(config-if)#ip route 192.168.1.0 255.255.255.0 172.17.0.1
Router(config-if)#ip route 192.168.3.0 255.255.255.0 172.18.0.1