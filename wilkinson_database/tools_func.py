from wilkinson_database.database import purpose_database, room_database  # Import purpose and landmarks

def search_purpose_database(input_text):
    input_text = input_text.lower()  # Convert user input to lowercase for case-insensitive search
    for purpose, data in purpose_database.items():
        descriptions = data["descriptions"]
        keywords = data["keywords"]
        for keyword in keywords:
            if keyword in input_text:
                return f"You seem to be here for {purpose} ({', '.join(descriptions)})."
    return "I'm not sure about your purpose here."

# Tool for room details
def room_finder(room_number):
    room_info = room_database.get(room_number)
    if room_info:
        return f"Room {room_number} - {room_info['name']}\nCapacity: {room_info['capacity']} people\nDescription: {room_info['description']}"
    else:
        return f"Room {room_number} not found in the building."




