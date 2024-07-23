import os
import logging
import socket
from kubernetes import client, config
from flask import Flask, jsonify

app = Flask(__name__)

# Kubernetes Environment
def get_pod_info():
    # Load k8s config
    config.load_incluster_config()
    # Create k8s api client 
    pod_client = client.CoreV1Api()
    # get pod namespace
    namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()
    # get pod name
    pod_name = os.environ.get("HOSTNAME")
    # get pod instance
    pod = pod_client.read_namespaced_pod(name=pod_name, namespace=namespace)
    # get hostname, ip address
    hostname = pod.metadata.name
    ip_address = pod.status.pod_ip
    return hostname, ip_address

# Local Environment
def get_host_info():
    # get hostname, ip address
    hostname = socket.gethostname()
    # get ip address by socket info
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        soc.connect("8.8.8.8",80)
        ip_address = soc.getsockname()[0]
    except Exception:
        ip_address = "127.0.0.1"
    finally:
        soc.close()
    return hostname, ip_address

@app.route("/", methods=["GET"])
def main():
    # Kubernetes
    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
        hostname, ip_address = get_pod_info()
    # Docker, Local
    else:
        hostname, ip_address = get_host_info()

    return jsonify({
        "hostname": hostname,
        "ip_address": ip_address
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)