def calculated_discount(price, discount_percent = 10):
    savings = price * (discount_percent / 100)
    final_price = price - savings
    return f"ORIGINAL: {price} | FINAL: {final_price}" 

call_1 = calculated_discount(100)
call_2 = calculated_discount(200, 25)

print(call_1)
print(call_2)