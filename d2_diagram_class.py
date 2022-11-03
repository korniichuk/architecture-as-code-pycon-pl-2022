from diagrams import Diagram
from diagrams.aws.compute import EC2

graph_attr = {
    "bgcolor": "white"
}

with Diagram(
        name="Example 2",
        filename="example2",
        outformat=["png", "dot"],
        direction="LR",
        graph_attr=graph_attr,
        show=False):
    EC2("web")
