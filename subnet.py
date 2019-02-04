class Network():
 def __init__(self,ipaddress):
    self.ipaddress=ipaddress
 def belongsclass(ipaddress):
    if int(ipaddress[0])>= 0 and int(ipaddress[0])<= 127:
      print ("IP address belongs to class A")
    elif int(ipaddress[0])>= 128 and int(ipaddress[0])<=191:
      print ("IP address belongs to class B")
    elif int(ipaddress[0])>=192 and int(ipaddress[0])<=223:
      print("IP address belongs to class C")
    elif int(ipaddress[0])>= 224 and int(ipaddress[0])<=239:
      print("Ipaddress belongs to class D")
n=str(input())
melo=Network.belongsclass(n)
