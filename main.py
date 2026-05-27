import json
import sys

def main(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print("--- Ads Metrics Report ---")
    for camp in data["campaigns"]:
        network = camp["network"]
        clicks = camp["clicks"]
        leads = camp["leads"]
        cost = camp["cost"]
        revenue = camp["revenue"]
        
        roi = ((revenue - cost) / cost * 100) if cost > 0 else 0
        cr = (leads / clicks * 100) if clicks > 0 else 0
        profit = revenue - cost
        
        print(f"[{network}] ROI: {roi:.2f}%, CR: {cr:.2f}%, Profit: ${profit:.2f}")

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "tests/fixtures/sample_data.json"
    main(filepath)