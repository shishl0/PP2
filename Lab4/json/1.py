import json

with open("./sample-data.json", "r") as file:
    data = json.load(file)

def print_header():
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
    print("-" * 80)

def print_interfaces(data):
    for item in data.get("imdata", []):
        attributes = item.get("l1PhysIf", {}).get("attributes", {})
        dn = attributes.get("dn", "")
        description = attributes.get("descr", "")
        speed = attributes.get("speed", "inherit")
        mtu = attributes.get("mtu", "")
        print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<5}")

if __name__ == "__main__":
    print_header()
    print_interfaces(data)
