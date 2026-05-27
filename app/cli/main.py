import json
import sys
from packages.core.metrics import calculate_roi, calculate_cr, calculate_profit

def main(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print("--- Ads Metrics Report (Refactored) ---")
    for camp in data["campaigns"]:
        roi = calculate_roi(camp["revenue"], camp["cost"])
        cr = calculate_cr(camp["leads"], camp["clicks"])
        profit = calculate_profit(camp["revenue"], camp["cost"])
        
        print(f"[{camp['network']}] ROI: {roi:.2f}%, CR: {cr:.2f}%, Profit: ${profit:.2f}")

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "tests/fixtures/sample_data.json"
    main(filepath)