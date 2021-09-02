import sys
from workflow import Workflow, ICON_WEB, web
import socket


def main(wf):
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()

    r = web.get("http://ip-api.com/json")

    r.raise_for_status()
    result = r.json()
    external_ip = result['query']
    country = result['country']
    city = result['city']

    wf.add_item(title="Local IP: {}".format(local_ip),
                arg=local_ip,
                valid=True,
                subtitle="Local",
                copytext=local_ip,
                icon='local-ip.png')
    wf.add_item(title="External IP: {}".format(external_ip),
                arg=external_ip,
                valid=True,
                subtitle="Country: {}, City: {}".format(country, city),
                copytext=external_ip,
                icon='external-ip.png')

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
