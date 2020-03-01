This is the million entry parser.

Yes, we are aware it is called Million Tweet Parser. Disregard that. 

To run, pass a commandline argument like the following:

$ docker run -e APP_KEY={YOUR_APP_KEY} -t million_tweet_parser:1.01 python main.py --page_size=1000 --num_pages=4 --output=results.json

Where:
APP_KEY: This is how a user can pass along an APP_KEY for the api in a safe manner. DO NOT COMMIT YOUR (actual) APP KEY to Github! Also, APP_KEY should not be “hardcoded” anywhere in your source code.
--page_size: This command line argument is required. It will ask for how many records to request from the API per call.
--num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.
--output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).


 
