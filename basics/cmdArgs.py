# command line arguments 
# these are passed when running the python script from terminal
# we can access the command line arguments using sys.argv
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])

# in real world applications, we use argparse python inbuild module
# it gives more information than sys, it also provide help messages 
import argparse

parser = argparse.ArgumentParser(description="Employee Details")
parser.add_argument('--name', help="Employee name")
parser.add_argument('--role', type=str, default='Developer', help="Employee role")

args = parser.parse_args()
print(args.name)
print(args.role)