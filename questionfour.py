import json

def optimize_energy_distribution(demand_data, source_data):
    results = []
    total_cost = 0
    renewable_energy_used = 0
    total_energy_used = 0

    # Sort sources by cost (Greedy Prioritization)
    sources = sorted(source_data, key=lambda x: x['cost'])

    for hour_data in demand_data:
        hour = hour_data['hour']
        districts = {k: v for k, v in hour_data.items() if k != 'hour'}
        
        allocation = {dist: {'Solar': 0, 'Hydro': 0, 'Diesel': 0, 'total': 0} for dist in districts}
        
        # Track remaining capacity for each source this hour
        current_capacities = {}
        for s in sources:
            # Check if source is available during this specific hour
            start, end = map(int, s['available_hours'].split('-'))
            if start <= hour <= end:
                current_capacities[s['type']] = s['max_capacity']
            else:
                current_capacities[s['type']] = 0

        # Allocate sources greedily (Cheapest First)
        for s in sources:
            s_type = s['type']
            s_cost = s['cost']
            
            for dist, demand in districts.items():
                needed = demand - allocation[dist]['total']
                if needed > 0 and current_capacities[s_type] > 0:
                    drawn = min(needed, current_capacities[s_type])
                    
                    allocation[dist][s_type] = drawn
                    allocation[dist]['total'] += drawn
                    current_capacities[s_type] -= drawn
                    
                    # Statistical tracking
                    cost_inc = drawn * s_cost
                    total_cost += cost_inc
                    total_energy_used += drawn
                    if s_type in ['Solar', 'Hydro']:
                        renewable_energy_used += drawn

        # Prepare results for this hour
        for dist, demand in districts.items():
            fulfilled_pct = (allocation[dist]['total'] / demand) * 100
            results.append({
                "Hour": hour,
                "District": dist,
                "Solar": allocation[dist]['Solar'],
                "Hydro": allocation[dist]['Hydro'],
                "Diesel": allocation[dist]['Diesel'],
                "Total Used": allocation[dist]['total'],
                "Demand": demand,
                "% Met": f"{fulfilled_pct:.1f}%"
            })

    return results, total_cost, (renewable_energy_used / total_energy_used) * 100

def main():
    # Data Modeling (2 Marks) - Based on Tables in Brief
    demand_table = [
        {"hour": 6, "District A": 20, "District B": 15, "District C": 25},
        {"hour": 7, "District A": 22, "District B": 16, "District C": 28}
    ]
    
    source_table = [
        {"id": "S1", "type": "Solar", "max_capacity": 50, "available_hours": "06-18", "cost": 1.0},
        {"id": "S2", "type": "Hydro", "max_capacity": 40, "available_hours": "00-24", "cost": 1.5},
        {"id": "S3", "type": "Diesel", "max_capacity": 60, "available_hours": "17-23", "cost": 3.0}
    ]

    results, total_cost, renewable_pct = optimize_energy_distribution(demand_table, source_table)

    # Output Results (3 Marks)
    print(f"{'Hour':<5} | {'Dist':<10} | {'Solar':<6} | {'Hydro':<6} | {'Diesel':<6} | {'Total':<6} | {'Demand':<6} | {'% Met'}")
    print("-" * 75)
    for r in results:
        print(f"{r['Hour']:<5} | {r['District']:<10} | {r['Solar']:<6} | {r['Hydro']:<6} | {r['Diesel']:<6} | {r['Total Used']:<6} | {r['Demand']:<6} | {r['% Met']}")

    print(f"\nTotal Cost: Rs. {total_cost}")
    print(f"Renewable Energy Usage: {renewable_pct:.2f}%")

if __name__ == "__main__":
    main()