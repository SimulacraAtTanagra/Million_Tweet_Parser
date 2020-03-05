This is the million entry parser.

Yes, we are aware it is called Million Tweet Parser. Disregard that. 

To run, first clone repository, then, after navigating in, build using the following command:



'''

    $ docker build -t million_tweet_parser:1.02 .

'''



Then, pass a commandline argument like the following to run:



'''

    $ docker run -e APP_KEY={YOUR_APP_KEY} -t million_tweet_parser:1.02 python main.py --page_size=1000 --num_pages=4 --output=results.json

'''


Where:

APP_KEY: This is how a user can pass along an APP_KEY for the api in a safe manner. 

--page_size: This command line argument is required. It will ask for how many records to request from the API per call.

--num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.

--output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).

None of the arguments or variables above need to be encapsulated in quotes to denote string. 
 
