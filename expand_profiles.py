"""
Expand profile data to include more comprehensive coverage of Coremark Metals catalog.

This utility script generates additional profile sizes and variations to expand
the profiles_data.csv to include more comprehensive coverage approaching the 558
profiles mentioned in the Coremark catalog.
"""

import csv

def generate_expanded_profiles():
    """Generate expanded profile data."""
    
    profiles = []
    
    # Helper to add profile
    def add_profile(material, shape, size, **kwargs):
        profile = {
            'Material': material,
            'Shape': shape,
            'Size': size,
            'Width': kwargs.get('Width', ''),
            'Height': kwargs.get('Height', ''),
            'Thickness': kwargs.get('Thickness', ''),
            'Wall_Thickness': kwargs.get('Wall_Thickness', ''),
            'Outer_Diameter': kwargs.get('Outer_Diameter', ''),
            'Inner_Diameter': kwargs.get('Inner_Diameter', ''),
            'Web_Thickness': kwargs.get('Web_Thickness', ''),
            'Flange_Width': kwargs.get('Flange_Width', ''),
            'Flange_Thickness': kwargs.get('Flange_Thickness', ''),
            'Weight_Per_Foot': kwargs.get('Weight_Per_Foot', ''),
            'Price_Per_Foot': kwargs.get('Price_Per_Foot', ''),
        }
        profiles.append(profile)
    
    # Expand Steel Angles - Many more sizes
    steel_angle_sizes = [
        (0.5, 0.5, 0.0625, 0.15, 0.23),
        (0.75, 0.75, 0.125, 0.59, 0.89),
        (1.0, 1.0, 0.125, 0.80, 1.20),
        (1.0, 1.0, 0.1875, 1.16, 1.75),
        (1.25, 1.25, 0.125, 1.01, 1.52),
        (1.5, 1.5, 0.125, 1.23, 1.85),
        (1.5, 1.5, 0.1875, 1.80, 2.70),
        (2.0, 2.0, 0.125, 1.65, 2.48),
        (2.0, 2.0, 0.1875, 2.44, 3.66),
        (2.0, 2.0, 0.25, 3.19, 4.79),
        (2.5, 2.5, 0.1875, 3.07, 4.61),
        (2.5, 2.5, 0.25, 4.01, 6.02),
        (2.5, 2.5, 0.375, 5.90, 8.85),
        (3.0, 3.0, 0.1875, 3.71, 5.57),
        (3.0, 3.0, 0.25, 4.90, 7.35),
        (3.0, 3.0, 0.375, 7.20, 10.80),
        (3.0, 3.0, 0.5, 9.40, 14.10),
        (3.5, 3.5, 0.25, 5.80, 8.70),
        (3.5, 3.5, 0.375, 8.50, 12.75),
        (4.0, 4.0, 0.25, 6.60, 9.90),
        (4.0, 4.0, 0.375, 9.80, 14.70),
        (4.0, 4.0, 0.5, 12.80, 19.20),
        (5.0, 5.0, 0.375, 12.30, 18.45),
        (5.0, 5.0, 0.5, 16.20, 24.30),
        (6.0, 6.0, 0.375, 14.90, 22.35),
        (6.0, 6.0, 0.5, 19.60, 29.40),
        # Unequal leg angles
        (2.0, 1.5, 0.1875, 2.12, 3.18),
        (2.5, 2.0, 0.25, 3.62, 5.43),
        (3.0, 2.0, 0.25, 4.10, 6.15),
        (3.5, 2.5, 0.25, 4.90, 7.35),
        (4.0, 3.0, 0.25, 5.80, 8.70),
        (4.0, 3.0, 0.375, 8.50, 12.75),
        (5.0, 3.5, 0.375, 10.40, 15.60),
        (6.0, 4.0, 0.375, 12.30, 18.45),
        (6.0, 4.0, 0.5, 16.20, 24.30),
        (8.0, 6.0, 0.5, 21.90, 32.85),
    ]
    
    for w, h, t, wt, price in steel_angle_sizes:
        add_profile('Steel', 'Angle', f'{w}x{h}x{t}',
                   Width=w, Height=h, Thickness=t,
                   Weight_Per_Foot=wt, Price_Per_Foot=price)
    
    # Expand Steel Square Tubes
    steel_sq_sizes = [
        (0.75, 0.75, 0.065, 1.04, 1.56),
        (1.0, 1.0, 0.065, 1.40, 2.10),
        (1.0, 1.0, 0.125, 2.00, 3.00),
        (1.0, 1.0, 0.1875, 2.86, 4.29),
        (1.25, 1.25, 0.065, 1.77, 2.66),
        (1.5, 1.5, 0.065, 2.14, 3.21),
        (1.5, 1.5, 0.125, 3.07, 4.61),
        (1.5, 1.5, 0.1875, 4.40, 6.60),
        (2.0, 2.0, 0.065, 2.88, 4.32),
        (2.0, 2.0, 0.125, 4.32, 6.48),
        (2.0, 2.0, 0.1875, 6.32, 9.48),
        (2.0, 2.0, 0.25, 8.15, 12.23),
        (2.5, 2.5, 0.125, 5.59, 8.39),
        (2.5, 2.5, 0.1875, 8.22, 12.33),
        (2.5, 2.5, 0.25, 10.70, 16.05),
        (3.0, 3.0, 0.125, 6.87, 10.31),
        (3.0, 3.0, 0.1875, 10.10, 15.15),
        (3.0, 3.0, 0.25, 13.10, 19.65),
        (3.0, 3.0, 0.375, 19.02, 28.53),
        (3.5, 3.5, 0.125, 8.15, 12.23),
        (4.0, 4.0, 0.125, 9.42, 14.13),
        (4.0, 4.0, 0.1875, 13.87, 20.81),
        (4.0, 4.0, 0.25, 18.04, 27.06),
        (4.0, 4.0, 0.375, 25.82, 38.73),
        (5.0, 5.0, 0.125, 11.97, 17.96),
        (5.0, 5.0, 0.1875, 17.67, 26.51),
        (5.0, 5.0, 0.188, 21.63, 32.45),
        (5.0, 5.0, 0.25, 23.04, 34.56),
        (5.0, 5.0, 0.375, 33.13, 49.70),
        (6.0, 6.0, 0.125, 14.53, 21.80),
        (6.0, 6.0, 0.188, 21.63, 32.45),
        (6.0, 6.0, 0.25, 28.43, 42.65),
        (6.0, 6.0, 0.375, 41.11, 61.67),
        (8.0, 8.0, 0.188, 29.23, 43.85),
        (8.0, 8.0, 0.25, 38.50, 57.75),
        (8.0, 8.0, 0.375, 55.66, 83.49),
    ]
    
    for w, h, wt, weight, price in steel_sq_sizes:
        add_profile('Steel', 'Square Tube', f'{w}x{h}x{wt}',
                   Width=w, Height=h, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Expand Steel Rectangular Tubes
    steel_rect_sizes = [
        (2.0, 1.0, 0.065, 2.25, 3.38),
        (2.0, 1.0, 0.125, 3.20, 4.80),
        (2.0, 1.0, 0.1875, 4.60, 6.90),
        (3.0, 1.5, 0.120, 5.59, 8.39),
        (3.0, 2.0, 0.065, 3.62, 5.43),
        (3.0, 2.0, 0.125, 5.60, 8.40),
        (3.0, 2.0, 0.1875, 8.20, 12.30),
        (4.0, 2.0, 0.065, 4.37, 6.56),
        (4.0, 2.0, 0.125, 7.11, 10.67),
        (4.0, 2.0, 0.1875, 10.48, 15.72),
        (4.0, 2.0, 0.25, 13.60, 20.40),
        (5.0, 3.0, 0.125, 9.70, 14.55),
        (5.0, 3.0, 0.1875, 14.32, 21.48),
        (5.0, 3.0, 0.188, 14.53, 21.80),
        (5.0, 3.0, 0.25, 18.71, 28.07),
        (6.0, 2.0, 0.125, 9.42, 14.13),
        (6.0, 3.0, 0.125, 10.70, 16.05),
        (6.0, 3.0, 0.1875, 15.83, 23.75),
        (6.0, 3.0, 0.188, 16.32, 24.48),
        (6.0, 4.0, 0.125, 11.97, 17.96),
        (6.0, 4.0, 0.1875, 17.67, 26.51),
        (6.0, 4.0, 0.25, 23.04, 34.56),
        (8.0, 4.0, 0.125, 14.53, 21.80),
        (8.0, 4.0, 0.188, 21.21, 31.82),
        (8.0, 4.0, 0.25, 27.59, 41.39),
        (8.0, 6.0, 0.188, 25.82, 38.73),
        (8.0, 6.0, 0.250, 33.54, 50.31),
        (10.0, 6.0, 0.25, 38.86, 58.29),
    ]
    
    for w, h, wt, weight, price in steel_rect_sizes:
        add_profile('Steel', 'Rectangular Tube', f'{w}x{h}x{wt}',
                   Width=w, Height=h, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Expand Steel Round Tubes
    steel_round_sizes = [
        (0.5, 0.049, 0.402, 0.24, 0.36),
        (0.5, 0.065, 0.370, 0.31, 0.47),
        (0.625, 0.049, 0.527, 0.31, 0.47),
        (0.75, 0.049, 0.652, 0.38, 0.57),
        (0.75, 0.065, 0.620, 0.50, 0.75),
        (1.0, 0.049, 0.902, 0.52, 0.78),
        (1.0, 0.065, 0.870, 0.69, 1.04),
        (1.0, 0.083, 0.834, 0.87, 1.31),
        (1.0, 0.120, 0.760, 1.20, 1.80),
        (1.25, 0.049, 1.152, 0.66, 0.99),
        (1.25, 0.065, 1.120, 0.87, 1.31),
        (1.25, 0.083, 1.084, 1.10, 1.65),
        (1.5, 0.049, 1.402, 0.79, 1.19),
        (1.5, 0.065, 1.370, 1.05, 1.58),
        (1.5, 0.083, 1.334, 1.33, 2.00),
        (1.5, 0.120, 1.260, 1.88, 2.82),
        (2.0, 0.049, 1.902, 1.06, 1.59),
        (2.0, 0.065, 1.870, 1.41, 2.12),
        (2.0, 0.083, 1.834, 1.79, 2.69),
        (2.0, 0.120, 1.760, 2.54, 3.81),
        (2.5, 0.083, 2.334, 2.24, 3.36),
        (2.5, 0.120, 2.260, 3.20, 4.80),
        (2.5, 0.188, 2.124, 4.87, 7.31),
        (3.0, 0.083, 2.834, 2.70, 4.05),
        (3.0, 0.120, 2.760, 3.85, 5.78),
        (3.0, 0.188, 2.624, 5.88, 8.82),
        (3.5, 0.120, 3.260, 4.51, 6.77),
        (4.0, 0.120, 3.760, 5.17, 7.76),
        (4.0, 0.188, 3.624, 7.95, 11.93),
    ]
    
    for od, wt, id_val, weight, price in steel_round_sizes:
        add_profile('Steel', 'Round Tube', f'{od}x{wt}',
                   Outer_Diameter=od, Inner_Diameter=id_val, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Expand Steel Channels
    steel_channel_sizes = [
        (2.0, 1.22, 0.17, 1.22, 0.17, 1.70, 2.55),
        (3.0, 1.41, 0.17, 1.41, 0.17, 3.50, 5.25),
        (4.0, 1.58, 0.18, 1.58, 0.18, 5.40, 8.10),
        (5.0, 1.75, 0.19, 1.75, 0.19, 6.70, 10.05),
        (6.0, 1.92, 0.20, 1.92, 0.20, 8.20, 12.30),
        (7.0, 2.09, 0.21, 2.09, 0.21, 9.80, 14.70),
        (8.0, 2.26, 0.22, 2.26, 0.22, 11.50, 17.25),
        (9.0, 2.43, 0.23, 2.43, 0.23, 13.40, 20.10),
        (10.0, 2.60, 0.24, 2.60, 0.24, 15.30, 22.95),
        (12.0, 3.05, 0.28, 3.05, 0.28, 20.70, 31.05),
    ]
    
    for h, w, wt, fw, ft, weight, price in steel_channel_sizes:
        add_profile('Steel', 'Channel', f'{h}x{w}x{wt}',
                   Height=h, Width=w, Web_Thickness=wt, 
                   Flange_Width=fw, Flange_Thickness=ft,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Now add Aluminum profiles (similar structure, different pricing)
    # Aluminum Angles
    aluminum_angle_sizes = [
        (0.5, 0.5, 0.0625, 0.05, 0.15),
        (0.75, 0.75, 0.125, 0.22, 0.66),
        (1.0, 1.0, 0.125, 0.29, 0.87),
        (1.0, 1.0, 0.1875, 0.42, 1.26),
        (1.0, 1.0, 0.25, 0.54, 1.62),
        (1.5, 1.5, 0.125, 0.44, 1.32),
        (1.5, 1.5, 0.1875, 0.64, 1.92),
        (1.5, 1.5, 0.25, 0.83, 2.49),
        (2.0, 2.0, 0.125, 0.59, 1.77),
        (2.0, 2.0, 0.1875, 0.86, 2.58),
        (2.0, 2.0, 0.25, 1.15, 3.45),
        (2.0, 2.0, 0.375, 1.68, 5.04),
        (2.5, 2.5, 0.25, 1.47, 4.41),
        (3.0, 3.0, 0.1875, 1.31, 3.93),
        (3.0, 3.0, 0.25, 1.76, 5.28),
        (3.0, 3.0, 0.375, 2.59, 7.77),
        (4.0, 4.0, 0.25, 2.37, 7.11),
        (4.0, 4.0, 0.375, 3.50, 10.50),
        (5.0, 5.0, 0.375, 4.42, 13.26),
        (6.0, 6.0, 0.375, 5.35, 16.05),
        # Unequal leg
        (1.5, 1.0, 0.125, 0.37, 1.11),
        (2.0, 1.0, 0.125, 0.44, 1.32),
        (2.0, 1.5, 0.125, 0.52, 1.56),
        (3.0, 2.0, 0.1875, 1.08, 3.24),
        (4.0, 3.0, 0.25, 2.06, 6.18),
    ]
    
    for w, h, t, wt, price in aluminum_angle_sizes:
        add_profile('Aluminum', 'Angle', f'{w}x{h}x{t}',
                   Width=w, Height=h, Thickness=t,
                   Weight_Per_Foot=wt, Price_Per_Foot=price)
    
    # Aluminum Square Tubes
    aluminum_sq_sizes = [
        (0.5, 0.5, 0.049, 0.21, 0.63),
        (0.75, 0.75, 0.062, 0.34, 1.02),
        (1.0, 1.0, 0.062, 0.47, 1.41),
        (1.0, 1.0, 0.125, 0.87, 2.61),
        (1.5, 1.5, 0.062, 0.72, 2.16),
        (1.5, 1.5, 0.125, 1.35, 4.05),
        (2.0, 2.0, 0.062, 0.97, 2.91),
        (2.0, 2.0, 0.125, 1.84, 5.52),
        (2.0, 2.0, 0.188, 2.66, 7.98),
        (2.5, 2.5, 0.125, 2.33, 6.99),
        (3.0, 3.0, 0.125, 2.81, 8.43),
        (3.0, 3.0, 0.188, 4.11, 12.33),
        (4.0, 4.0, 0.125, 3.79, 11.37),
        (4.0, 4.0, 0.188, 5.57, 16.71),
        (5.0, 5.0, 0.188, 7.03, 21.09),
        (6.0, 6.0, 0.188, 8.49, 25.47),
    ]
    
    for w, h, wt, weight, price in aluminum_sq_sizes:
        add_profile('Aluminum', 'Square Tube', f'{w}x{h}x{wt}',
                   Width=w, Height=h, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Aluminum Rectangular Tubes
    aluminum_rect_sizes = [
        (2.0, 1.0, 0.062, 0.60, 1.80),
        (2.0, 1.0, 0.125, 1.13, 3.39),
        (3.0, 1.0, 0.062, 0.72, 2.16),
        (3.0, 2.0, 0.062, 0.85, 2.55),
        (3.0, 2.0, 0.125, 1.62, 4.86),
        (4.0, 2.0, 0.125, 2.11, 6.33),
        (4.0, 3.0, 0.125, 2.60, 7.80),
        (5.0, 3.0, 0.125, 3.08, 9.24),
        (6.0, 2.0, 0.125, 2.81, 8.43),
        (6.0, 3.0, 0.125, 3.30, 9.90),
        (6.0, 4.0, 0.125, 3.57, 10.71),
        (8.0, 4.0, 0.188, 6.76, 20.28),
        (8.0, 6.0, 0.188, 8.22, 24.66),
    ]
    
    for w, h, wt, weight, price in aluminum_rect_sizes:
        add_profile('Aluminum', 'Rectangular Tube', f'{w}x{h}x{wt}',
                   Width=w, Height=h, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Aluminum Round Tubes
    aluminum_round_sizes = [
        (0.375, 0.035, 0.305, 0.09, 0.27),
        (0.5, 0.049, 0.402, 0.14, 0.42),
        (0.625, 0.049, 0.527, 0.18, 0.54),
        (0.75, 0.049, 0.652, 0.22, 0.66),
        (1.0, 0.049, 0.902, 0.29, 0.87),
        (1.0, 0.065, 0.870, 0.39, 1.17),
        (1.0, 0.083, 0.834, 0.48, 1.44),
        (1.25, 0.049, 1.152, 0.37, 1.11),
        (1.25, 0.065, 1.120, 0.48, 1.44),
        (1.5, 0.049, 1.402, 0.44, 1.32),
        (1.5, 0.065, 1.370, 0.59, 1.77),
        (1.5, 0.083, 1.334, 0.74, 2.22),
        (2.0, 0.049, 1.902, 0.59, 1.77),
        (2.0, 0.065, 1.870, 0.78, 2.34),
        (2.0, 0.083, 1.834, 1.00, 3.00),
        (2.5, 0.065, 2.370, 0.98, 2.94),
        (2.5, 0.083, 2.334, 1.26, 3.78),
        (3.0, 0.065, 2.870, 1.18, 3.54),
        (3.0, 0.083, 2.834, 1.51, 4.53),
        (4.0, 0.083, 3.834, 2.03, 6.09),
    ]
    
    for od, wt, id_val, weight, price in aluminum_round_sizes:
        add_profile('Aluminum', 'Round Tube', f'{od}x{wt}',
                   Outer_Diameter=od, Inner_Diameter=id_val, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Aluminum Channels
    aluminum_channel_sizes = [
        (1.5, 0.75, 0.125, 0.75, 0.125, 0.45, 1.35),
        (2.0, 1.0, 0.13, 1.0, 0.13, 0.61, 1.83),
        (3.0, 1.5, 0.13, 1.5, 0.13, 1.03, 3.09),
        (4.0, 2.0, 0.15, 2.0, 0.15, 1.53, 4.59),
        (5.0, 2.0, 0.19, 2.0, 0.19, 2.02, 6.06),
        (6.0, 2.5, 0.19, 2.5, 0.19, 2.59, 7.77),
    ]
    
    for h, w, wt, fw, ft, weight, price in aluminum_channel_sizes:
        add_profile('Aluminum', 'Channel', f'{h}x{w}x{wt}',
                   Height=h, Width=w, Web_Thickness=wt,
                   Flange_Width=fw, Flange_Thickness=ft,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Stainless Steel profiles (higher pricing multiplier ~3.5x steel)
    # Stainless Angles
    stainless_angle_sizes = [
        (0.5, 0.5, 0.0625, 0.15, 0.53),
        (0.75, 0.75, 0.125, 0.59, 2.07),
        (1.0, 1.0, 0.125, 0.80, 2.80),
        (1.0, 1.0, 0.1875, 1.16, 4.06),
        (1.5, 1.5, 0.125, 1.23, 4.31),
        (1.5, 1.5, 0.1875, 1.80, 6.30),
        (2.0, 2.0, 0.125, 1.65, 5.78),
        (2.0, 2.0, 0.1875, 2.44, 8.54),
        (2.0, 2.0, 0.25, 3.19, 11.17),
        (2.5, 2.5, 0.25, 4.01, 14.04),
        (3.0, 3.0, 0.1875, 3.71, 12.99),
        (3.0, 3.0, 0.25, 4.90, 17.15),
        (3.0, 3.0, 0.375, 7.20, 25.20),
        (4.0, 4.0, 0.25, 6.60, 23.10),
        (4.0, 4.0, 0.375, 9.80, 34.30),
        (5.0, 5.0, 0.375, 12.30, 43.05),
        (6.0, 6.0, 0.375, 14.90, 52.15),
        # Unequal leg
        (2.0, 1.5, 0.1875, 2.12, 7.42),
        (3.0, 2.0, 0.25, 4.10, 14.35),
        (4.0, 3.0, 0.25, 5.80, 20.30),
    ]
    
    for w, h, t, wt, price in stainless_angle_sizes:
        add_profile('Stainless', 'Angle', f'{w}x{h}x{t}',
                   Width=w, Height=h, Thickness=t,
                   Weight_Per_Foot=wt, Price_Per_Foot=price)
    
    # Stainless Square Tubes
    stainless_sq_sizes = [
        (0.75, 0.75, 0.065, 0.72, 2.52),
        (1.0, 1.0, 0.065, 0.86, 3.01),
        (1.0, 1.0, 0.120, 1.54, 5.39),
        (1.5, 1.5, 0.065, 1.32, 4.62),
        (1.5, 1.5, 0.120, 2.37, 8.30),
        (2.0, 2.0, 0.065, 1.79, 6.27),
        (2.0, 2.0, 0.120, 3.23, 11.31),
        (2.0, 2.0, 0.188, 4.88, 17.08),
        (2.5, 2.5, 0.120, 4.09, 14.32),
        (3.0, 3.0, 0.120, 4.94, 17.29),
        (3.0, 3.0, 0.188, 7.49, 26.22),
        (4.0, 4.0, 0.120, 6.66, 23.31),
        (4.0, 4.0, 0.188, 10.11, 35.39),
        (5.0, 5.0, 0.188, 12.73, 44.56),
        (6.0, 6.0, 0.188, 15.35, 53.73),
    ]
    
    for w, h, wt, weight, price in stainless_sq_sizes:
        add_profile('Stainless', 'Square Tube', f'{w}x{h}x{wt}',
                   Width=w, Height=h, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Stainless Rectangular Tubes
    stainless_rect_sizes = [
        (2.0, 1.0, 0.065, 1.05, 3.68),
        (2.0, 1.0, 0.120, 1.91, 6.69),
        (3.0, 2.0, 0.120, 3.09, 10.82),
        (4.0, 2.0, 0.120, 3.94, 13.79),
        (4.0, 3.0, 0.120, 4.56, 15.96),
        (5.0, 3.0, 0.120, 5.38, 18.83),
        (6.0, 2.0, 0.120, 4.80, 16.80),
        (6.0, 3.0, 0.120, 5.55, 19.43),
        (6.0, 4.0, 0.120, 6.37, 22.30),
        (8.0, 4.0, 0.120, 7.84, 27.44),
    ]
    
    for w, h, wt, weight, price in stainless_rect_sizes:
        add_profile('Stainless', 'Rectangular Tube', f'{w}x{h}x{wt}',
                   Width=w, Height=h, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Stainless Round Tubes
    stainless_round_sizes = [
        (0.375, 0.035, 0.305, 0.09, 0.32),
        (0.5, 0.049, 0.402, 0.14, 0.49),
        (0.625, 0.049, 0.527, 0.18, 0.63),
        (0.75, 0.049, 0.652, 0.22, 0.77),
        (1.0, 0.049, 0.902, 0.29, 1.02),
        (1.0, 0.065, 0.870, 0.38, 1.33),
        (1.0, 0.083, 0.834, 0.48, 1.68),
        (1.25, 0.049, 1.152, 0.37, 1.30),
        (1.25, 0.065, 1.120, 0.48, 1.68),
        (1.5, 0.049, 1.402, 0.44, 1.54),
        (1.5, 0.065, 1.370, 0.59, 2.07),
        (1.5, 0.083, 1.334, 0.74, 2.59),
        (2.0, 0.049, 1.902, 0.59, 2.07),
        (2.0, 0.065, 1.870, 0.79, 2.77),
        (2.0, 0.083, 1.834, 1.00, 3.50),
        (2.5, 0.065, 2.370, 0.99, 3.47),
        (2.5, 0.083, 2.334, 1.26, 4.41),
        (3.0, 0.065, 2.870, 1.19, 4.17),
        (3.0, 0.083, 2.834, 1.51, 5.29),
        (4.0, 0.083, 3.834, 2.03, 7.11),
    ]
    
    for od, wt, id_val, weight, price in stainless_round_sizes:
        add_profile('Stainless', 'Round Tube', f'{od}x{wt}',
                   Outer_Diameter=od, Inner_Diameter=id_val, Wall_Thickness=wt,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    # Stainless Channels
    stainless_channel_sizes = [
        (2.0, 1.22, 0.17, 1.22, 0.17, 1.70, 5.95),
        (3.0, 1.41, 0.17, 1.41, 0.17, 3.50, 12.25),
        (4.0, 1.58, 0.18, 1.58, 0.18, 5.40, 18.90),
        (5.0, 1.75, 0.19, 1.75, 0.19, 6.70, 23.45),
        (6.0, 1.92, 0.20, 1.92, 0.20, 8.20, 28.70),
    ]
    
    for h, w, wt, fw, ft, weight, price in stainless_channel_sizes:
        add_profile('Stainless', 'Channel', f'{h}x{w}x{wt}',
                   Height=h, Width=w, Web_Thickness=wt,
                   Flange_Width=fw, Flange_Thickness=ft,
                   Weight_Per_Foot=weight, Price_Per_Foot=price)
    
    return profiles


if __name__ == "__main__":
    print("Generating expanded profile data...")
    profiles = generate_expanded_profiles()
    
    print(f"Generated {len(profiles)} profiles")
    
    # Count by material and shape
    by_material = {}
    by_shape = {}
    for p in profiles:
        mat = p['Material']
        shape = p['Shape']
        by_material[mat] = by_material.get(mat, 0) + 1
        by_shape[shape] = by_shape.get(shape, 0) + 1
    
    print("\nBy Material:")
    for mat, count in sorted(by_material.items()):
        print(f"  {mat}: {count}")
    
    print("\nBy Shape:")
    for shape, count in sorted(by_shape.items()):
        print(f"  {shape}: {count}")
    
    # Write to CSV
    output_file = "profiles_data.csv"
    fieldnames = ['Material', 'Shape', 'Size', 'Width', 'Height', 'Thickness',
                  'Wall_Thickness', 'Outer_Diameter', 'Inner_Diameter',
                  'Web_Thickness', 'Flange_Width', 'Flange_Thickness',
                  'Weight_Per_Foot', 'Price_Per_Foot']
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(profiles)
    
    print(f"\nWrote {len(profiles)} profiles to {output_file}")
