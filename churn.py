customers = [
    {"age": 25, "monthly_bill": 500, "months_active": 3, "churned": 1},
    {"age": 40, "monthly_bill": 1200, "months_active": 36, "churned": 0},
    {"age": 32, "monthly_bill": 800, "months_active": 12, "churned": 1},
    {"age": 50, "monthly_bill": 1500, "months_active": 60, "churned": 0}
]

def calculate_churn(customers):
    if not customers:
        return 0, 0.0
    churned_count = 0
    customer_count = len(customers)
    for customer in customers:
        if customer["churned"] == 1:
            churned_count += 1
    churned_rate =round((churned_count / customer_count) *100.0, 2)
    return churned_count, churned_rate
    


count, rate = calculate_churn(customers)
print(count)
print(rate)

