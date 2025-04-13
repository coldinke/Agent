import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int,
                    help="increase output verbosity")
parser.add_argument("-c", "--cot", type=bool,
                    help="With chain-of-thought reasoning.")
args = parser.parse_args()
answer = args.square**2
if args.cot:
    print("the cot is True")
else:
    print("the cot is False")
if args.verbosity == 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(f"{answer}")
