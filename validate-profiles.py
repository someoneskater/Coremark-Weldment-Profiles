#!/usr/bin/env python3
"""
Validate that all profile JSON files conform to the required schema.
Each profile must have: size, thickness, price, cost_per_lb, weight_per_ft, sku
"""

import json
import sys
from pathlib import Path

REQUIRED_PROPERTIES = ['size', 'thickness', 'price', 'cost_per_lb', 'weight_per_ft', 'sku']

def validate_profile(profile, filename):
    """Validate a single profile object."""
    missing = [prop for prop in REQUIRED_PROPERTIES if prop not in profile]
    if missing:
        return False, f"Missing properties: {', '.join(missing)}"
    
    # Validate data types
    if not isinstance(profile['size'], str):
        return False, "Property 'size' must be a string"
    if not isinstance(profile['thickness'], str):
        return False, "Property 'thickness' must be a string"
    if not isinstance(profile['sku'], str):
        return False, "Property 'sku' must be a string"
    
    # Validate numeric types
    for prop in ['price', 'cost_per_lb', 'weight_per_ft']:
        if not isinstance(profile[prop], (int, float)):
            return False, f"Property '{prop}' must be a number"
        if profile[prop] < 0:
            return False, f"Property '{prop}' must be non-negative"
    
    return True, "Valid"

def validate_file(filepath):
    """Validate a profile JSON file."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if 'profiles' not in data:
            return False, "File must contain a 'profiles' array"
        
        profiles = data['profiles']
        if not isinstance(profiles, list):
            return False, "'profiles' must be an array"
        
        if len(profiles) == 0:
            return False, "File contains no profiles"
        
        # Validate each profile
        for i, profile in enumerate(profiles):
            valid, message = validate_profile(profile, filepath)
            if not valid:
                return False, f"Profile #{i+1}: {message}"
        
        return True, f"Valid - {len(profiles)} profile(s)"
    
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Main validation function."""
    profiles_dir = Path('profiles')
    
    if not profiles_dir.exists():
        print("Error: 'profiles' directory not found")
        sys.exit(1)
    
    # Find all JSON files in profiles directory
    json_files = list(profiles_dir.glob('**/*.json'))
    
    if not json_files:
        print("Warning: No JSON files found in profiles directory")
        return
    
    print(f"Validating {len(json_files)} profile file(s)...\n")
    
    all_valid = True
    for json_file in sorted(json_files):
        valid, message = validate_file(json_file)
        status = "✓" if valid else "✗"
        print(f"{status} {json_file.relative_to(profiles_dir)}: {message}")
        if not valid:
            all_valid = False
    
    print()
    if all_valid:
        print("All profile files are valid!")
        sys.exit(0)
    else:
        print("Some profile files have validation errors.")
        sys.exit(1)

if __name__ == '__main__':
    main()
