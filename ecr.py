import pulumi
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("ecr_repository", force_delete=True)

image = awsx.ecr.Image(
    "image",
    repository_url=repository.url,
    context="handlers/",
    platform="linux/amd64",
)

pulumi.export("url", repository.url)