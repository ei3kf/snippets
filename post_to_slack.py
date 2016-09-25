import urllib2

def post_to_slack(slack_message):
    """
    Function to post a message to a slack channel.
    """
    SLACK_ENDPOINT = "https://hooks.slack.com/services/000000000/000000000/0000000000000000000"
    SLACK_CHANNEL = "my_lovely_slack_channel"
    SLACK_USERNAME = "my_lovely_bot"
    SLACK_TEXT = (str(slack_message))
    SLACK_JSON = {
        'channel': SLACK_CHANNEL,
        'username': SLACK_USERNAME,
        'text': SLACK_TEXT,
        }
    request = urllib2.Request(SLACK_ENDPOINT)
    request.add_header('Content-Type', 'application/json')
    urllib2.urlopen(request, json.dumps(SLACK_JSON))
