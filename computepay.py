def computepay(hours, rate):
    """
    Compute gross pay based on hours worked and hourly rate.
    Normal rate for hours up to 40, time-and-a-half for hours over 40.
    
    Args:
        hours: Number of hours worked
        rate: Hourly rate
    
    Returns:
        Gross pay amount
    """
    if hours <= 40:
        pay = hours * rate
    else:
        # Regular pay for first 40 hours + overtime pay for hours over 40
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    
    return pay


# Main program
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
    
    pay = computepay(hours, rate)
    print(f"Pay: {pay}")
    
except ValueError:
    print("Error, please enter numeric input")
