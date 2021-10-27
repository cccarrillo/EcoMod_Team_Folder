import datetime

# First test: Implement now() and then implement date_to_string(...).

def now():
    return datetime.datetime.now()

def date_to_string(d):
    return d.strftime('%m/%d/%Y')

# Second test: Implement x_squared(...) and then implement def num_to_string(...).

def x_squared(x):
    return x*x

def num_to_string(x):
    return "{}".format(x)

# Run two tests.

if __name__ == '__main__':
    print("Today's date == " + date_to_string(now()))
    print("4 squared == " + num_to_string(x_squared(4)))