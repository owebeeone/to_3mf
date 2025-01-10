"""
3mf XML xdatatree classes for the 3mf config file.
"""

from xdatatrees import (
    xdatatree,
    xfield,
    Attribute,
    Metadata,
    Element,
    CamelSnakeConverter,
    XmlSerializationSpec,
)

from to_3mf.xdatatree_utils import MatrixConverter, TransformConverter, VectorConverter

from typing import List

"""Create a default config for all xdatatree annotated classes."""
DEFAULT_CONFIG = xfield(ename_transform=CamelSnakeConverter, ftype=Element)


@xdatatree
class MeshStat:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Attribute)
    edges_fixed: int = xfield(doc="Number of fixed edges")
    degenerate_facets: int = xfield(doc="Number of degenerate facets")
    facets_removed: int = xfield(doc="Number of facets removed")
    facets_reversed: int = xfield(doc="Number of facets reversed")
    backwards_edges: int = xfield(doc="Number of backwards edges")


@xdatatree
class Part:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Metadata)
    id: str = xfield(ftype=Attribute, doc="Id of the part")
    subtype: str = xfield(ftype=Attribute, doc="Subtype of the part")
    name: str = xfield(ftype=Metadata, doc="Name of the part")
    matrix: MatrixConverter = xfield(ftype=Metadata, doc="Frame of ref of the object")
    source_file: str = xfield(
        doc="Path to the original source file that this part was derived from"
    )
    source_object_id: str = xfield(doc="ID of the object in the source file")
    source_volume_id: str = xfield(doc="ID of the specific volume/mesh within the source object")
    source_offset_x: float = xfield(doc="X offset from source position")
    source_offset_y: float = xfield(doc="Y offset from source position")
    source_offset_z: float = xfield(doc="Z offset from source position")
    mesh_stat: MeshStat = xfield(ftype=Element, doc="Mesh statistics of the part")


@xdatatree
class Object:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Attribute)
    id: int = xfield(ftype=Attribute, doc="Id of the object")
    name: str = xfield(ftype=Metadata, doc="Name of the object")
    extruder: str = xfield(ftype=Metadata, doc="extruder to be used")
    parts: List[Part] = xfield(ftype=Element, doc="List of parts")


@xdatatree
class ModelInstance:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Metadata)
    object_id: str = xfield(doc="Reference to the object ID in the 3MF file")
    instance_id: str = xfield(doc="Unique identifier for this specific instance of the object")
    identify_id: str = xfield(
        doc="Identifier used to track this instance across different plate arrangements"
    )


@xdatatree
class Plate:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Metadata)
    plater_id: str = xfield(doc="Unique identifier for the build plate")
    plater_name: str = xfield(doc="Display name of the build plate")
    locked: bool = xfield(doc="Whether the plate layout is locked for editing")
    thumbnail_file: str = xfield(doc="Path to the plate preview thumbnail image")
    top_file: str = xfield(doc="Path to the top view image of the plate")
    pick_file: str = xfield(doc="Path to the picking preview image used for part selection")
    model_instances: List[ModelInstance] = xfield(
        ename="model_instance",
        ftype=Element,
        doc="List of model instances placed on this build plate",
    )


@xdatatree
class AssembleItem:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Attribute)
    object_id: str = xfield(doc="Reference to the object ID in the 3MF file")
    instance_id: str = xfield(doc="Unique identifier for this specific instance")
    transform: TransformConverter = xfield(
        doc="Transformation matrix defining rotation and scaling"
    )
    offset: VectorConverter = xfield(doc="Translation vector defining position offset")


@xdatatree
class Assemble:
    XDATATREE_CONFIG = DEFAULT_CONFIG(ftype=Element)
    assemble_items: List[AssembleItem] = xfield(ename="assemble_item", doc="List of assemble items")


@xdatatree
class Config:
    """
    The config class is the root of the config part of a 3mf file.
    """

    XDATATREE_CONFIG = DEFAULT_CONFIG
    objects: List[Object] = xfield(ename="object", doc="List of objects in the 3MF file")
    plate: Plate = xfield(doc="Build plate configuration and layout")
    assemble: Assemble = xfield(
        doc="Assembly information defining how objects are arranged together"
    )


SERIALIZATION_SPEC = XmlSerializationSpec(Config, "config")
