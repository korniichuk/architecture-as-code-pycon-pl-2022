from diagrams import Diagram
from diagrams.aws.compute import EC2

graph_attr = {
    "bgcolor": "white"
}

with Diagram(
        "Example 2",
        filename="example2",
        outformat=["png", "dot"],
        direction="LR",
        show=False):
    EC2("web")
