import sys
from workflow import Workflow, ICON_WEB, web
import socket


def main(wf):
    #  url = 'https://api.pinboard.in/v1/posts/recent'
    #  params = dict(auth_token=API_KEY, count=20, format='json')
    #  r = web.get(url, params)

    #  # throw an error if request failed
    #  # Workflow will catch this and show it to the user
    #  r.raise_for_status()

    #  # Parse the JSON returned by pinboard and extract the posts
    #  result = r.json()
    #  posts = result['posts']

    #  # Loop through the returned posts and add an item for each to
    #  # the list of results for Alfred
    #  for post in posts:
    #  wf.add_item(title=post['description'],
    #              subtitle=post['href'],
    #              icon=ICON_WEB)

    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()

    r = web.get("https://api.myip.com")

    r.raise_for_status()
    result = r.json()
    external_ip = result['ip']

    wf.add_item(title="Local IP: {}".format(local_ip),
                arg=local_ip,
                valid=True,
                subtitle=local_ip,
                copytext=local_ip,
                icon=ICON_WEB)
    wf.add_item(title="External IP: {}".format(external_ip),
                arg=external_ip,
                valid=True,
                subtitle=external_ip,
                copytext=external_ip,
                icon=ICON_WEB)

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
