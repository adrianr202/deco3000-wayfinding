# Database to determine purpose

# Differentiate Study, Class and Lecture
purpose_database = {
    "Study": {
        "descriptions": ["Quiet, individual study in a dedicated space.", "A peaceful environment for focused learning."],
        "keywords": ["study", "revise", "quiet", "individual"]
    },
    "Class": {
        "descriptions": ["Structured classroom activities.", "Engage with your peers in a learning environment."],
        "keywords": ["class", "learning", "peer", "studio"]
    },
    "Lecture": {
        "descriptions": ["Attend a lecture or seminar.", "Listen to a guest speaker on a specific topic."],
        "keywords": ["lecture", "seminar", "guest speaker"]
    },
    "Gallery Visit": {
        "descriptions": ["Space for art, paintings and sculptures open for viewing from Architecture and Design students."],
        "keywords": ["musuem", "artworks", "gallery"]
    },
    "Unknown Purpose": {
        "descriptions": ["I'm not sure about your specific purpose in Wilkinson Building."],
        "keywords": []
    },
}

room_database = {
    # Tin Sheds Gallery 
    "gallery": {
        "name": "Tin Sheds Gallery",
        "capacity": 50,
        "description": "Gallery in Wilkinson Building offering art works featured in Architecture and Design."
    },
    # Lecture
    "270": {
        "name": "Lecture Room 270",
        "capacity": 150,
        "description": "A lecture room for educational presentations with seating, audio-visual equipment and suitable lighting."
    },
    # Class
    "241": {
        "name": "Seminar Room 241",
        "capacity": 30,
        "description": "A studio room for small, interactive group discussions and collaborative learning."
    },
    # Study
    "homebase": {
        "name": "Masters Homebase",
        "capacity": 50,
        "description": "A room with equiped with computers and spots for model making. Great area for quite study."
    },
}


