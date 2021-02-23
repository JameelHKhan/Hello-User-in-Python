# Module 1 Assignment - Part 2

print("Enter the date the first assignment is due below:")
day = input("Day (enter 2-digit value): ")
month = input("Month (enter 2-digit value): ")
year = input("Year (enter 4-digit value): ")

print("For the time, enter the 2-digit value for each line below:")
timeHours = input("Enter the hours: ")
timeMinutes = input("Enter the minutes: ")

print(f"Module 1 Assignment is due on {month}/{day}/{year} " +
      f"at {timeHours}:{timeMinutes} EST.")
