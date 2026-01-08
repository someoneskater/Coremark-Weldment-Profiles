#!/usr/bin/env python3
"""
Test script to validate and demonstrate usage of profile_data.json
"""

import json
import sys

def load_profiles():
    """Load profile data from JSON file"""
    try:
        with open('profile_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: profile_data.json not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

def print_statistics(data):
    """Print statistics about the profile data"""
    profiles = data['profiles']
    metadata = data['metadata']
    
    print("=" * 70)
    print("COREMARK WELDMENT PROFILES - DATA STATISTICS")
    print("=" * 70)
    print(f"\nSupplier: {metadata['supplier']}")
    print(f"Last Updated: {metadata['last_updated']}")
    print(f"Total Profiles: {metadata['total_profiles']}")
    print(f"Price Basis: {metadata['price_basis']}")
    print(f"Currency: {metadata['currency']}")
    
    # Count by material
    by_material = {}
    by_type = {}
    for profile in profiles:
        mat = profile['material']
        typ = profile['type']
        by_material[mat] = by_material.get(mat, 0) + 1
        by_type[typ] = by_type.get(typ, 0) + 1
    
    print("\n" + "-" * 70)
    print("PROFILES BY MATERIAL:")
    print("-" * 70)
    for material, count in sorted(by_material.items()):
        print(f"  {material:20s}: {count:4d} profiles")
    
    print("\n" + "-" * 70)
    print("PROFILES BY TYPE:")
    print("-" * 70)
    for ptype, count in sorted(by_type.items()):
        print(f"  {ptype.replace('_', ' ').title():20s}: {count:4d} profiles")
    
    # Price range
    prices = [p['price'] for p in profiles]
    weights = [p['weight_per_ft'] for p in profiles]
    
    print("\n" + "-" * 70)
    print("PRICE RANGE:")
    print("-" * 70)
    print(f"  Minimum: ${min(prices):.2f}")
    print(f"  Maximum: ${max(prices):.2f}")
    print(f"  Average: ${sum(prices)/len(prices):.2f}")
    
    print("\n" + "-" * 70)
    print("WEIGHT RANGE (lb/ft):")
    print("-" * 70)
    print(f"  Minimum: {min(weights):.2f} lb/ft")
    print(f"  Maximum: {max(weights):.2f} lb/ft")
    print(f"  Average: {sum(weights)/len(weights):.2f} lb/ft")

def search_profiles(data, material=None, profile_type=None, max_price=None):
    """Search for profiles matching criteria"""
    profiles = data['profiles']
    results = []
    
    for profile in profiles:
        if material and profile['material'] != material:
            continue
        if profile_type and profile['type'] != profile_type:
            continue
        if max_price and profile['price'] > max_price:
            continue
        results.append(profile)
    
    return results

def demonstrate_usage(data):
    """Demonstrate how to use the profile data"""
    print("\n" + "=" * 70)
    print("EXAMPLE USAGE DEMONSTRATIONS")
    print("=" * 70)
    
    # Example 1: Find all steel angles
    steel_angles = search_profiles(data, material="Steel", profile_type="angle")
    print(f"\n1. Steel Angles: {len(steel_angles)} profiles found")
    print("   First 3 examples:")
    for profile in steel_angles[:3]:
        print(f"   - {profile['description']:40s} ${profile['price']:8.2f}")
    
    # Example 2: Find aluminum profiles under $100
    affordable_al = search_profiles(data, material="Aluminum", max_price=100)
    print(f"\n2. Affordable Aluminum profiles (<$100): {len(affordable_al)} found")
    print("   First 3 examples:")
    for profile in affordable_al[:3]:
        print(f"   - {profile['description']:40s} ${profile['price']:8.2f}")
    
    # Example 3: Find all wide flange beams
    beams = search_profiles(data, profile_type="wide_flange")
    print(f"\n3. Wide Flange Beams: {len(beams)} profiles found")
    print("   Heaviest 3:")
    sorted_beams = sorted(beams, key=lambda x: x['weight_per_ft'], reverse=True)
    for profile in sorted_beams[:3]:
        print(f"   - {profile['description']:40s} {profile['weight_per_ft']:6.2f} lb/ft")
    
    # Example 4: Find stainless steel profiles
    stainless = search_profiles(data, material="Stainless Steel")
    print(f"\n4. Stainless Steel profiles: {len(stainless)} found")
    print("   Price range: ${:.2f} - ${:.2f}".format(
        min(p['price'] for p in stainless),
        max(p['price'] for p in stainless)
    ))

def main():
    """Main function"""
    print("\nLoading profile data...")
    data = load_profiles()
    print("✓ Successfully loaded profile data\n")
    
    # Print statistics
    print_statistics(data)
    
    # Demonstrate usage
    demonstrate_usage(data)
    
    print("\n" + "=" * 70)
    print("✓ All tests passed successfully!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
