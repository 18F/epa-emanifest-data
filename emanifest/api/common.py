"""
This file are sets of standard data.
"""

CONTAINER_TYPES = (
    ("BA", "Burlap, cloth, paper, or plastic bags"),
    ("CF", "Fiber or plastic boxes, cartons, cases"),
    ("CM", "Metal boxes, cartons, cases (including roll-offs"),
    ("CW", "Wooden boxes, cartons, cases"),
    ("CY", "Cylinders"),
    ("DF", "Fiberboard or plastic drums, barrels, kegs"),
    ("DM", "Metal drums, barrels, kegs"),
    ("DW", "Wooden drums, barrels, kegs"),
    ("HG", "Hopper or gondola cars"),
    ("TC", "Tank cars"),
    ("TP", "Portable tanks"),
    ("TT", "Cargo tanks (tank trucks)."),
)

# COUNTRIES is not a complete list. This is for demo purposes only.
COUNTRIES = (
    ('US', 'United States'),
    ('MX', 'Mexico'),
    ('PR', 'Puerto Rico'),
)

DOT_GROUPS = (
    ("", "None"),
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
)

WASTE_CODE_TYPES = (
    ('Federal', 'Federal'),
    ('State', 'State'),
)

UNITS_OF_MEASURE = (
    ("G", "Gallons (liquids only)"),
    ("N", "Cubic Meters"),
    ("K", "Kilograms P = Pounds"),
    ("L", "Liters (liquids only)"),
    ("T", "Tons (2000 Pounds)"),
    ("M", "Metric Tons (1000 Kilograms)"),
    ("Y", "Cubic Yards"),
)
