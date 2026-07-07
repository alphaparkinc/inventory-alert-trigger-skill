"""
example_usage.py -- Demonstrates InventoryAlertTriggerClient
"""
from client import InventoryAlertTriggerClient

def main():
    client = InventoryAlertTriggerClient()
    result = client.check_stock_level(
        current_stock=15,
        daily_sales_velocity=2.5,
        lead_time_days=7
    )
    print("[Inventory Alert Check]")
    print(f"Days Left: {result['days_of_stock_left']}")
    print(f"Reorder Level: {result['reorder_point']}")
    print(f"Alert Status: {result['alert_triggered']} (Severity: {result['severity']})")

if __name__ == "__main__":
    main()
