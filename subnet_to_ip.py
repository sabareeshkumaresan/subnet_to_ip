import ipaddress

def subnet_to_ips(subnet):
    try:
        # Clear host bits to ensure we're working with a proper network address
        network = ipaddress.ip_network(subnet.strip(), strict=False)
        return [str(ip) for ip in network.hosts()]  # Exclude network and broadcast addresses
    except ValueError as e:
        print(f"Error converting subnet {subnet}: {e}")
        return []

# Read subnets from file
with open('subnets.txt', 'r') as file:
    subnets = file.readlines()

# Prepare output list of IPs
ips_output = []

for subnet in subnets:
    ips_output.extend(subnet_to_ips(subnet))

# Save IPs to the output file
with open('ips_output.txt', 'w') as file:
    for ip in ips_output:
        file.write(ip + '\n')

print("IP address conversion complete. Check ips_output.txt for results.")
