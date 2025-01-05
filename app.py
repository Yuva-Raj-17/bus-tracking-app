# app.py

def get_bus_details(bus_id):
    bus_info = {
        "101": {"route": "Main Street", "location": "Downtown", "status": "On time"},
        "102": {"route": "Baker Street", "location": "Central Station", "status": "Delayed"},
    }

    return bus_info.get(bus_id, "Bus ID not found.")

if __name__ == "__main__":
    bus_id = input("Enter Bus ID: ")
    details = get_bus_details(bus_id)
    print(f"Bus {bus_id} Details: {details}")
