import kfp
from kfp import compiler
from utils.authentication import get_istio_auth_session


class KubeflowManager:
    def __init__(self, endpoint: str, username: str, password: str, namespace: str):
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.namespace = namespace
        self.auth_session = self._get_istio_auth_session()
        self.kfp_client = self._create_kfp_client()

    def _get_istio_auth_session(self):
        return get_istio_auth_session(url=self.endpoint, username=self.username, password=self.password)

    def _create_kfp_client(self):
        client = kfp.Client(
            host=f"{self.endpoint}/pipeline",
            namespace=self.namespace,
            cookies=self.auth_session.session_cookie,
        )
        # client = kfp.Client(
        #     host=f"{self.endpoint}/pipeline"
        # )
        # client._job_api.api_client.cookie = f"authservice_session={self.auth_session.session_cookie}"
        return client

    # def get_session_cookie(self):
    #     cookie = self.auth_session.session_cookie.split("=")[-1]
    #     return cookie

    def get_kfp_client(self):
        return self.kfp_client
