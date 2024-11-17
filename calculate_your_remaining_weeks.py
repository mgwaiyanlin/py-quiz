
def terrible_life(current_age):
    people_life = 75
    weeks_in_a_year = 52

    remaining_years = people_life - current_age
    remaining_weeks = remaining_years * weeks_in_a_year
    remaining_days = remaining_years * 365

    print(f"You have {remaining_days} days left.")
    print(f"You have {remaining_weeks} weeks left.")
    
terrible_life(22)

