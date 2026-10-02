def calculate_taxed_total(amount: float, tax_rate: float = 0.05) -> float:
    total: float = amount * (1 + tax_rate)
    return round(total, 2)

standard_bill = calculate_taxed_total(100.0)
custom_bill = calculate_taxed_total(amount=100.0, tax_rate=0.15)

print(standard_bill)
print(custom_bill)
