import argparse
import sys
import os
from src.getting import func

print("Initializing application...")

required = argparse.ArgumentParser()
required.add_argument(
        "--page_size",
        type=int,
        required=True
        )
required.add_argument(
        "--num_pages",type=int,default=-999)
required.add_argument(
        "--output",
        default=None
        )
token = os.environ['APP_KEY']
args = required.parse_args()
page_size = args.page_size
num_pages = args.num_pages
output = args.output
database_id = "nc67-uf89"
if output != None:
    with open(output,'w') as f:
        f.write(func(page_size,num_pages,token,database_id))
else:
    try:
        sys.stdout.write(func(page_size,num_pages,token,database_id ))
    except:
        print("Something went wrong here boss")
