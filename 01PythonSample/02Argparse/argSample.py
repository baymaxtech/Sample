import argparse

parser = argparse.ArgumentParser()

parser.add_argument("command", help="Enter the command", type=str)  # Sample of positional argument
parser.add_argument("-s", "--square", type=int, help="Enter the number squared")  # Sample of optional argument
parser.add_argument("-v", "--verbose", action="store_true", help="The verbose")  # Sample of true | false argument
# Sample of limited selection
parser.add_argument("-m", "--multiple", type=int, choices=[0, 1, 2], help="Number of multiplier")
# Sample of count
parser.add_argument("-c", "--count", action="count", help="Number of count")
# Sample of two command exclusive
group = parser.add_mutually_exclusive_group()
group.add_argument("-a", "--apple", action="store_true")
group.add_argument("-ss", "--samsung", action="store_true")

# argSample.py square
args = parser.parse_args()
print args.command  # >> square
print args.square**2  # >> 16
if args.verbose:
    print "The square of {} is {}".format(args.square,args.square**2)   # >> The square of 4 is 16
else:
    print args.square

print "The multiplier is {}".format(args.multiple)  # >> The multiplier is 2
print "The count is {}".format(args.count)  # >> The count is 3

