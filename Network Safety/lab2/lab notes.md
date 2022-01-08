# 实验2课件

## 如何用更安全的方式管理网络？

- 访问权限
- 消息认证
- 信息加密

## Access Control List (ACL)

> access control lists are network traffic filters that can control incoming or outgoing traffic, work on a set of rules that define how to foward or block a packet at the router's interface

- filter based on address or protocol
- can clarify which users can access and which operations can be allowed

## 标准ACL

```
(config)# access-list [access-list number 1-99] [permit/deny] [source IP] [ACL mask]
```

允许语句 with the same group number are regarded as ACL 命令

0 refers to check, 1 refers not

```
(config)# access list 1 permit 192.168.1.0 0.0.0.255
(config)# access list 1 permit host 10.0.0.1
(config)# access list 1 deny any
```

to delete

```
(config)# no access list [access list number]
```

## ACL 绑定

```
(config if)# ip access group [access list number] [in/out]

(config if)# no ip accesss-group [access-list number] [in/out]

show access-list
```

## ACL 工作规则

every router interface, every access (in/out) can only have one ACL command, 

![image-20201214103850950](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201214103850950.png)

## ACL 实例1

```
access-list 1 deny 172.30.16.5 0.0.0.0
access-list 1 permit 172.30.16.0 0.0.0.255
```

how will packets from 

- 172.30.16.4
- 172.30.16.5
- 172.30.15.2

be forwarded, and after the adjusting the order of sentences, has teh forwarding situation changed

## ACL 实例2

```
access list 2 deny 172.30.16.5 0.0.0.0
access list 2 permit 172.30.16.0 0.0.0.255
access list 2 permit 192.168.1.0 0.0.0.255
```

are there 冗余 allowable statements 

after adding ```access list 2 deny 192.168.3.1 0.0.0.0``` before the last line, is there any redundancy

## 扩展ACL

```
(config)# access list [access list number 100 199]
[permit/deny] [protocol] [source IP] [ACL mask]
[destination IP] [ACL mask] [protocol]

access list 101 permit ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255

access list 101 deny tcp 192.168.1.0 0.0.0.255 host 192.168.2.100 eq 21 (ftp)

access list 101 permit tcp 192.168.1.0 0.0.0.255 any eq telnet
```

## Context-Based Access Control (CBAC)

>  CBAC feature of the Cisco IOS Firewall Feature Set actively inspects the activity behind a firewall, and specifies what traffic needs to be let in and what traffic needs to be let out by using access lists (in the same way that Cisco IOS uses access lists) However, CBAC access list include ip inspect statements that allow the inspection of the protocol to make sure that it is not tampered with before the protocol goes to the system behind the firewall

support not only network layer and transport layer, but also application layer protocols

```
(config)# ip inspect name [name] [protocol] [protocol option]

(config if)# ip inspect [name] [in/out]
```

## Virtual Private Network

> extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network, often encrypted

safe, easy to manage, ecrypted

## IPSec VPN

### IPSec 架构

data authentication and encryption: AH/ESP

AH: message header verigication protocol, which verifies the data source and data integrity, prevents message replay

ESP: encapsulating security payload, provides AH protocol verification function, also supports the encryption of messages

Key Management: IKE, auto-negotiation and exchange of secret keys, establishment and maintenance of security alliance services

### IPSec工作模式

传输模式 transport mode : insert IPSec header between IP header and higher layer protocol header, application scenario: data protection for communication between host and host

![image-20201214120658921](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Network Safety\lab2\lab notes.assets\image-20201214120658921.png)

隧道模式 tunnel mode : original ip packet is encapsulated into a payload, and the IPSec header and the new IP header are inserted in front of it: application scenario: the private newtowrk and the private network communicate through the publick network to establish a secure VPN channel 

![image-20201214120703674](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Network Safety\lab2\lab notes.assets\image-20201214120703674.png)

## ISAKMP配置

```
(config) # crypto isakmp policy [ isakmp index]
(config-isakmp)# encryption [method: aes /3des/ des]
(config-isakmp)# hash [method: sha / md5]
(config-isakmp)# authentication pre-share
(config-isakmp) # group [method] (1/2/5)
(config)# crypto isakmp key [key value] address [ip]
```

## IPSec 配置

使用 ACL 对流量进行过滤 （filter traffic）

``` 
(config)# access list [group 100 199] [permit/deny] [protocol][source ip ] [acl mask] [destination ip ] [acl mask] [protocol option]
```

transform set 

```
(config)# crypto ipsec transform-set [name] [esp/ah method] 
```

map 映射

```
(config) # crypto map [name] [map index] ipsec-isakmp
(config-crypto-map) # set peer [ip]
(config-crypto-map) # match address [acl group]
(config-crypto-map) # set transform-set [name]
```

端口绑定

```
(config) # int fX/X 
(config) # crypto map [name]
```

1. show crypto isakmp sa
   查看 isakmp 配置状态
2. show crypto isakmp policy
   查看 isakmp 策略配置集
3. show crypto ipsec sa
   查看 ipsec 配置状态
4. show crypto ipsec transform set
   查看 ipsec 传输模式



