import sys
import json
from packages.core.metrics import calculate_roi, calculate_cr, calculate_profit

def main(filepath=None):
    if filepath is None:
        if len(sys.argv) < 2:
            print("Ошибка: Укажите путь к JSON файлу.")
            print("Использование: ads-calc <путь_к_файлу.json>")
            sys.exit(1)
        filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    print("--- Ads Metrics Report (Refactored) ---")
    for camp in data["campaigns"]:
        roi = calculate_roi(camp["revenue"], camp["cost"])
        cr = calculate_cr(camp["leads"], camp["clicks"])
        profit = calculate_profit(camp["revenue"], camp["cost"])
        
        print(f"[{camp['network']}] ROI: {roi:.2f}%, CR: {cr:.2f}%, Profit: ${profit:.2f}")

if __name__ == "__main__":
    default_path = sys.argv[1] if len(sys.argv) > 1 else "tests/fixtures/sample_data.json"
    main(default_path)