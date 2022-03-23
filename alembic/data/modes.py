MODE_INITIAL = """
    INSERT INTO mode(
        id, name, is_tfl_service, is_fare_paying, is_scheduled_service
    ) VALUES
        ('bus', 'bus', True, True, True),
        ('cable-car', 'cable-car', True, True, True),
        ('coach', 'coach', False, True, True),
        ('cycle', 'cycle', False, False, False),
        ('cycle-hire', 'cycle-hire', True, True, False),
        ('dlr', 'dlr', True, True, True),
        ('elizabeth-line', 'elizabeth-line', True, True, True),
        ('interchange-keep-sitting', 'interchange-keep-sitting', False, False, False),
        ('interchange-secure', 'interchange-secure', False, False, False),
        ('national-rail', 'national-rail', False, True, True),
        ('overground', 'overground', True, True, True),
        ('replacement-bus', 'replacement-bus', True, True, True),
        ('river-bus', 'river-bus', True, True, True),
        ('river-tour', 'river-tour', True, True, True),
        ('taxi', 'taxi', False, False, False),
        ('tram', 'tram', True, True, True),
        ('tflrail', 'tflrail', True, True, True),
        ('tube', 'tube', True, True, True),
        ('walking', 'walking', False, False, False);"""

MODE_TRUNCATE = "TRUNCATE mode RESTART IDENTITY CASCADE;"
