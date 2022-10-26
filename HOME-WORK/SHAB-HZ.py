from Dez import *
def create_list(*args, **kwargs):
    DiskC=[]
    for zn1,zn2 in enumerate(args):
        DiskC.append(f"Name_{zn1} = {deg_to_gms(zn2)}")
    for zk1,zk2 in kwargs.items():
        DiskC.append(f"{zk1} = {deg_to_gms(zk2)}")
    return DiskC
print(create_list(172.258943,321.123123,12.321321,pole=21.123123,put_1=123123123))