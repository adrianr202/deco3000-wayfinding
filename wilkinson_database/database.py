# Database to determine purpose

# Differentiate Study, Class and Lecture
purpose_database = {
    "Study": {
        "name": ["Masters Homebase"],
        "capacity": 50,
        "description": ["Master Homebase is your place to study or take a break."],
        "keywords": ["study", "revise", "quiet", "break"]
    },
    "Class": {
        "name": ["Seminar Room 241"],
        "description": ["Class for DECO3000 is located in Seminar Room 241"],
        "keywords": ["class", "learning", "peer", "studio"]
    },
    "Lecture": {
        "name": ["Lecture Room 270"],
        "capacity": 150,
        "description": ["Your lecture will be at Lecture Room 270."],
        "keywords": ["lecture", "seminar", "guest speaker"]
    },
    "Gallery Visit": {
        "name": ["Tin Sheds Gallery"],
        "capacity": 50,
        "description": ["Gallery in Wilkinson Building offering art works featured in Architecture and Design"],
        "keywords": ["museum", "artworks", "gallery"]
    },
    "Unknown Purpose": {
        "name": ["Unknown"],
        "descriptions": ["I'm not sure about your specific purpose in Wilkinson Building."],
        "keywords": []
    },
}

room_database = {
    # Tin Sheds Gallery 
    "gallery": {
        "name": "tin sheds gallery",
        "capacity": 50,
        "description": "Gallery in Wilkinson Building offering art works featured in Architecture and Design.",

    },
    # Lecture
    "270": {
        "name": "lecture room 270",
        "capacity": 150,
        "description": "A lecture room for educational presentations with seating, audio-visual equipment and suitable lighting.",

    },
    # Class
    "241": {
        "name": "seminar room 241",
        "capacity": 30,
        "description": "A studio room for small, interactive group discussions and collaborative learning.",

    },
    # Study
    "homebase": {
        "name": "masters homebase",
        "capacity": 50,
        "description": "A room with equiped with computers and spots for model making. Great area for quite study.",

    },
}


