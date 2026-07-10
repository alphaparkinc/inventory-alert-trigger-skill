# genpark-inventory-alert-trigger-skill

> **GenPark AI Agent Skill** -- Inventory velocity and stockout predictor.

## Quick Start

```python
from client import InventoryAlertTriggerClient
client = InventoryAlertTriggerClient()
res = client.check_stock_level(100, 5.0, 10)
print(res["alert_triggered"])
```
