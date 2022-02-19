from tabulate import tabulate

HEADERS = ("Employee Name", "Hours Worked", "Pay Rate", "Regular Pay",
           "OT Pay", "Gross Pay", "Fed Tax", "State Tax", "FICA", "Net Pay")


def process_input():
    name = input("What is the empoyee's name? ")

    pay_rate = get_float_input("What is the employee's hourly wage? $",
                               "hourly wage")
    hours_worked = get_float_input(
        "How many hours has the employee worked this week? ", "hours worked")

    print(f"{name} worked {hours_worked} hours at ${pay_rate} per hour")
    return (name, hours_worked, pay_rate)


def get_float_input(prompt, field):
    valid_input = False
    while not valid_input:
        value = input(prompt)
        try:
            value = float(value)
            if value < 0:
                print(f"{value} is not a valid input for {field}.")
            else:
                valid_input = True
        except ValueError:
            print(f"{value} is not a valid input for {field}.")
    return value


def calculate(rate, hours):
    if hours > 40:
        regular_pay = 40 * rate
        OT_pay = (hours - 40) * rate * 1.5
    else:
        regular_pay = hours * rate
        OT_pay = 0.0

    gross_pay = regular_pay + OT_pay
    fed_tax = 0.1 * gross_pay
    state_tax = 0.06 * gross_pay
    FICA = 0.03 * gross_pay
    net_pay = gross_pay - fed_tax - state_tax - FICA

    return (regular_pay, OT_pay, gross_pay, fed_tax, state_tax, FICA, net_pay)


if __name__ == "__main__":
    employees = []

    print(
        "When you are done, all employee records will be output in table format"
    )

    done = False
    while not done:
        employee = process_input()
        output = calculate(employee[2], employee[1])
        employees.append(employee + output)
        done = True if input(
            "Press enter to continue or enter 0 if done. ") == '0' else False

    print(tabulate(employees, headers=HEADERS, floatfmt=".2f"))
