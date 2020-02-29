import argparse
import sys
from getting import func

required = argparse.ArgumentParser()
required.add_argument(
        "--size",
        type=int,
        default=0
        )
required.add_argument(
        "--num",type=int,default=-999)
required.add_argument(
        "--t",
        type=str,
        default=-1
        )
args = required.parse_args()
if __name__ == "__main__":
    func(args.size,args.num,args.t)
