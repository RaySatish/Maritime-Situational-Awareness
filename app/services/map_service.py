def plot_contact(contact_info):
    return {
        "latitude": contact_info["coordinates"]["lat"],
        "longitude": contact_info["coordinates"]["lon"],
        "type": contact_info["type"],
        "speed": contact_info["speed"],
        "timestamp": contact_info["timestamp"]
    }
