price = float(input("Enter item price: "))
gst = float(input("Enter GST %: "))
gst_amount = (price * gst) / 100
final_amount = price + gst_amount
print("Final Price: ₹",final_amount)