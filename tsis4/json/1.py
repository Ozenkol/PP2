import json

with open("sample_data.json", "r") as read_file:
    data = json.load(read_file);

print("""Interface Status
================================================================================""")
print("""DN                                             Description          Speed                      MTU """)

for j in range(len(data["imdata"])):
    for i, k in data["imdata"][j]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                          ")
        if i == "speed":
            print(k, end="                                         ")
        if i == "mtu":
            print(k, end="                   ")
    print()
