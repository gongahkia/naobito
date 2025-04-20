# ----- required imports -----

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.storage import Storage
from diagrams.onprem.client import User
from diagrams.generic.device import Mobile, Tablet  
from diagrams.programming.framework import React
from diagrams.programming.language import Python
from diagrams.custom import Custom

# ----- initialization code -----

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white",
    "rankdir": "TB",
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "fontname": "Sans-Serif",
    "fontcolor": "#2D3436",
    "pad": "0.4"
}
node_attr = {
    "fontsize": "12",
    "fontname": "Sans-Serif",
    "shape": "box",
    "style": "rounded",
    "labelloc": "b",
    "imagepos": "tc",
    "width": "1.6",
    "height": "1.8",
    "imagescale": "true",
    "fontcolor": "#2D3436",
    "margin": "0.2"
}
edge_attr = {
    "fontsize": "11",
    "fontname": "Sans-Serif",
    "fontcolor": "#2D3436"
}
opencv_icon = "https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg"

# ----- execution code -----

with Diagram("Naobito App Architecture", 
           show=False, 
           direction="TB",
           graph_attr=graph_attr,
           node_attr=node_attr,
           edge_attr=edge_attr):
    user = User("User")
    browser = Mobile("Web Browser") 
    with Cluster("Frontend (React)"):
        react = React("Naobito UI")
        upload_component = React("Upload Component")
        panel_gallery = React("Panel Gallery")
        react - [upload_component, panel_gallery]
    with Cluster("Backend (Flask)"):
        flask = Python("Flask Server")
        upload_handler = Python("Upload Handler")
        panel_detector = Custom("Panel Detection", opencv_icon)
        image_processor = Python("Image Processor")
        flask - [upload_handler, panel_detector, image_processor]
    with Cluster("Storage Services"):
        raw_storage = Storage("Uploads Directory")
        panel_storage = Storage("Panels Directory")
        raw_storage - Edge(style="dashed") - panel_storage
    user >> Edge(label="Interacts with") >> browser
    browser >> Edge(label="Uploads Image") >> react
    react >> Edge(label="POST /upload") >> flask
    upload_handler >> Edge(label="Save Original") >> raw_storage
    panel_detector << Edge(label="Process Image") << image_processor
    panel_detector >> Edge(label="Save Panels") >> panel_storage
    panel_storage >> Edge(label="Serve Panels") >> panel_gallery
    image_processor << Edge(label="Load Image") << raw_storage