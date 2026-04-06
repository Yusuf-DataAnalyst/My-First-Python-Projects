months = 0
current_savings = 0

print("\n🚀 ****** Welcome To Asset Goal Calculator ****** 🚀\n")
salary = int(input("💰 Enter your monthly salary: EGP "))
rate = float(input("📈 Enter the percentage you wish to invest (e.g., 0.30 for 30%): "))
target = int(input("🏠 Enter your goal price (Apartment, Gold, Business, etc.): EGP "))
annual_return = float(input("📊 Enter the expected annual return rate (e.g., 0.20 for 20%): "))
inflation_rate = float(input("💸 Enter the percentage increase in the asset's price (e.g., 0.15 for 15%): "))

monthly_contribution = salary * rate

while current_savings < target:
    months += 1
    current_savings += monthly_contribution
    
    if months % 12 == 0:
        # وقت الأرباح ووقت غلاء الأسعار
        current_savings += current_savings * annual_return
        target = target + (target * inflation_rate)
        
years = months // 12
remaining_months = months % 12

# عرض النتائج بشكل منظم وجذاب
print("\n" + "—" * 45)
print(f"⏳ Total Time Needed: {years} Years and {remaining_months} Months")
print(f"✅ Total Saving Reached: {current_savings:,.2f} EGP")
print(f"🎯 Final Target Price (After Inflation): {target:,.2f} EGP")
print("—" * 45 + "\n")
print("💪 Keep pushing towards your goal!
