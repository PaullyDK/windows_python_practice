# BROKEN CODE - FIX THIS
company_tax_rate = 0.15

def update_tax_rate(new_rate):
    # Hint: A keyword is missing right here!
    global company_tax_rate
    company_tax_rate = new_rate
    print(f"Inside function, tax rate set to: {company_tax_rate}")

update_tax_rate(0.18)
print(f"Global tax rate is now: {company_tax_rate}") 
# Expected Output should show 0.18 for both prints!

def calculate_payout(base_salary, *args,performance_score='B'):
    total_salary = 0.0
    for arg in args:
        total_salary += arg
    total_salary += base_salary
    if performance_score == "A":
        total_salary *= 1.1
    return total_salary

scores = [45, 88, 92, 61, 55, 78, 99, 30]
l = list(filter(lambda x:x >= 75, scores))
print(l)