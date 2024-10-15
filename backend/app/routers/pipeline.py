import logging

from config.settings import get_settings
from core.kubeflow_manager import KubeflowManager
from fastapi import APIRouter
from kfp import dsl

router = APIRouter(prefix="/pipeline", tags=["Pipeline"])

logger = logging.getLogger(__name__)

settings = get_settings()


@router.post("/all-step")
def all_step():
    print(f"{settings.KUBEFLOW_ENDPOINT}")

    experiment_name = "aipaas-ml-workflow"
    # pipeline_name = "ml-workflow-sample-pipeline"

    kf = KubeflowManager(
        endpoint=settings.KUBEFLOW_ENDPOINT,
        username=settings.KUBEFLOW_USERNAME,
        password=settings.KUBEFLOW_PASSWORD,
        namespace=settings.KUBEFLOW_NAMESPACE,
    )

    @dsl.container_component
    def say_hello(name: str):
        return dsl.ContainerSpec(image="alpine", command=["echo"], args=[f"Hello, {name}!"])

    @dsl.component
    def say_bye(name: str) -> str:
        return f"Bye, {name}!!"

    @dsl.pipeline
    def sample_pipeline(name: str = "World") -> str:
        # say_hello(name=name)
        bye_task = say_bye(name=name)
        return bye_task.output

    client = kf.get_kfp_client()

    experiment = kf.get_experiment_by_name(experiment_name=experiment_name)
    # kf.create_pipeline(sample_pipeline, pipeline_name )

    client.create_run_from_pipeline_func(
        sample_pipeline,
        # enable_caching=True,  # overrides the above disabling of caching
        experiment_id=experiment.experiment_id,
        arguments={"name": "KFP!"},
    )
