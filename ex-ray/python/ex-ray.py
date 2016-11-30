import os
import json
import sys
import urllib2

# build the API call to the BBC Juicer
def build_api_call(facet):
    bbc_juicer_api_key = os.getenv("BBC_JUICER_API_KEY")
    prefix = "http://juicer.api.bbci.co.uk/articles?"

    # Building Parameters for the juicer
    number_of_results = "&size=5"
    api_key = "&api_key=" + bbc_juicer_api_key
    recent_first = "&recent_first=yes"

    url = prefix + "facets[]=" + facet + number_of_results + recent_first + api_key

    return url


# Call the bbc juicer service and return the result. The result will
# be either the document as json or and empty string if the @url could not be
# processed
def get_json_from_juicer(request_url):
    try:
        req = urllib2.Request(request_url)
        handler = urllib2.urlopen(req)
    except urllib2.HTTPError:
        return ""

    return handler.read()

# Read the url for the entity from the arguments
facet = str(sys.argv[1])
url = build_api_call(facet)
result = get_json_from_juicer(url)
output_file = open("out.json", "w")
output_file.write(result)
