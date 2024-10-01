from config.settings import get_settings
from core.kubeflow_manager import KubeflowManager
from fastapi import FastAPI

app = FastAPI()

settings = get_settings()

print(f"{settings.KUBEFLOW_ENDPOINT}")


kf = KubeflowManager(
    endpoint=settings.KUBEFLOW_ENDPOINT,
    username=settings.KUBEFLOW_USERNAME,
    password=settings.KUBEFLOW_PASSWORD,
    namespace=settings.KUBEFLOW_NAMESPACE,
)

client = kf.get_kfp_client()
print(client.get_kfp_healthz())
# print(client.get_experiment(namespace=settings.KUBEFLOW_NAMESPACE, experiment_name='aipaas-ml-workflow'))
# print(client._context_setting)
# print(client.list_experiments())
# print(client.list_runs())
# print(client.list_pipelines())
# print(client.list_recurring_runs(experiment_id='cb702f34-3347-4973-9c94-472fc68520bf'))
# 실험 가져오기 또는 생성


# client.delete_experiment(experiment_id='910813c5-fa59-4e65-b5b5-6864a1305313')
# experiment = client.create_experiment(name='test-ml-workflow', namespace=settings.KUBEFLOW_NAMESPACE)
