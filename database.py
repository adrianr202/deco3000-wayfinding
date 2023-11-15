router_addresses = [
    'YOUR ROUTER ADDRESS',            # 0
    '48:91:d5:ef:2c:b8:',            # 1 
    '48:91:d5:ee:fd:80:',            # 2 
    '48:91:d5:ee:d7:38:',            # 3 
    '48:91:d5:ee:ba:b0:',            # 4 
    '48:91:d5:ee:fa:18:',            # 5 
    '48:91:d5:ee:ae:b0:',            # 6 
    '48:91:d5:ef:00:10:',            # 7 
    '48:91:d5:ee:b7:2c:',            # 8
    '48:91:d5:ef:2d:50:',            # 9 
    '48:91:d5:ef:25:a8:'             # 10
    ]

location_names = [
    'Entrance Outside',             # Start
    'Entrance Inside',              # 48:91:d5:ef:2c:b8'
    'Hearth Entrance',              # 48:91:d5:ee:fd:80'
    'The Hearth',                   # 48:91:d5:ee:d7:38'
    'Lecture Hall 231',             # 48:91:d5:ee:ba:b0'
    'Computer Lab 212',             # 48:91:d5:ee:fa:18'
    'Homebase Entrance',            # 48:91:d5:ee:ae:b0'
    'Homebase Desks 1',             # 48:91:d5:ef:00:10'
    'Homebase Desks 2',             # 48:91:d5:ee:b7:2c'
    'Homebase Desks 3',             # 48:91:d5:ef:2d:50'
    'Homebase Storage'              # 48:91:d5:ef:25:a8' 
    ]

router_positions = {
    0: (70, 96),
    1: (73, 81),
    2: (54, 77),
    3: (38, 66),
    4: (29, 79),
    5: (23, 49),
    6: (24, 31),
    7: (40, 24),
    8: (42, 46),
    9: (53, 36),
    10: (57, 47),
}

connections = [
    (0, 1), 
    (1, 2), 
    (2, 3), 
    (2, 4),
    (3, 4),
    (3, 5),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 9),
    (7, 8),
    (8, 9),
    (9, 10),
    ]