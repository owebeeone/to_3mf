from to_3mf.threemf_config import SERIALIZATION_SPEC as CONFIG_SERIALIZATION_SPEC
from to_3mf.threemf_model import SERIALIZATION_SPEC as MODEL_SERIALIZATION_SPEC

import lxml.etree as etree

from unittest import TestCase, main


XML_DATA = """\
<?xml version="1.0" encoding="UTF-8"?>
<config>
  <object id="2">
    <metadata key="name" value="OpenSCAD Model"/>
    <metadata key="extruder" value="2"/>
    <part id="1" subtype="normal_part">
      <metadata key="name" value="OpenSCAD Model"/>
      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
      <metadata key="source_file" value="basic_4_model.3mf"/>
      <metadata key="source_object_id" value="0"/>
      <metadata key="source_volume_id" value="0"/>
      <metadata key="source_offset_x" value="40"/>
      <metadata key="source_offset_y" value="40"/>
      <metadata key="source_offset_z" value="10"/>
      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>
    </part>
  </object>
  <object id="4">
    <metadata key="name" value="OpenSCAD Model"/>
    <metadata key="extruder" value="1"/>
    <part id="3" subtype="normal_part">
      <metadata key="name" value="OpenSCAD Model"/>
      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
      <metadata key="source_file" value="basic_4_model.3mf"/>
      <metadata key="source_object_id" value="1"/>
      <metadata key="source_volume_id" value="0"/>
      <metadata key="source_offset_x" value="-20"/>
      <metadata key="source_offset_y" value="40"/>
      <metadata key="source_offset_z" value="10"/>
      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>
    </part>
  </object>
  <object id="6">
    <metadata key="name" value="OpenSCAD Model"/>
    <metadata key="extruder" value="3"/>
    <part id="5" subtype="normal_part">
      <metadata key="name" value="OpenSCAD Model"/>
      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
      <metadata key="source_file" value="basic_4_model.3mf"/>
      <metadata key="source_object_id" value="2"/>
      <metadata key="source_volume_id" value="0"/>
      <metadata key="source_offset_x" value="-20"/>
      <metadata key="source_offset_y" value="-20"/>
      <metadata key="source_offset_z" value="10"/>
      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>
    </part>
  </object>
  <object id="8">
    <metadata key="name" value="OpenSCAD Model"/>
    <metadata key="extruder" value="4"/>
    <part id="7" subtype="normal_part">
      <metadata key="name" value="OpenSCAD Model"/>
      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
      <metadata key="source_file" value="basic_4_model.3mf"/>
      <metadata key="source_object_id" value="3"/>
      <metadata key="source_volume_id" value="0"/>
      <metadata key="source_offset_x" value="40"/>
      <metadata key="source_offset_y" value="-20"/>
      <metadata key="source_offset_z" value="10"/>
      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>
    </part>
  </object>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value=""/>
    <metadata key="locked" value="false"/>
    <metadata key="thumbnail_file" value="Metadata/plate_1.png"/>
    <metadata key="top_file" value="Metadata/top_1.png"/>
    <metadata key="pick_file" value="Metadata/pick_1.png"/>
    <model_instance>
      <metadata key="object_id" value="2"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="463"/>
    </model_instance>
    <model_instance>
      <metadata key="object_id" value="4"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="483"/>
    </model_instance>
    <model_instance>
      <metadata key="object_id" value="6"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="503"/>
    </model_instance>
    <model_instance>
      <metadata key="object_id" value="8"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="523"/>
    </model_instance>
  </plate>
  <assemble>
   <assemble_item object_id="2" instance_id="0" transform="1 0 0 0 1 0 0 0 1 40 40 10" offset="0 0 0" />
   <assemble_item object_id="4" instance_id="0" transform="1 0 0 0 1 0 0 0 1 -20 40 10" offset="0 0 0" />
   <assemble_item object_id="6" instance_id="0" transform="1 0 0 0 1 0 0 0 1 -20 -20 10" offset="0 0 0" />
   <assemble_item object_id="8" instance_id="0" transform="1 0 0 0 1 0 0 0 1 40 -20 10" offset="0 0 0" />
  </assemble>
</config>
"""

XML_DATA2 = """\
<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:slic3rpe="http://schemas.slic3r.org/3mf/2017/06" xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" requiredextensions="p">
 <metadata name="Application">BambuStudio-01.07.04.52</metadata>
 <metadata name="BambuStudio:3mfVersion">1</metadata>
 <metadata name="CopyRight"></metadata>
 <metadata name="CreationDate">2023-09-22</metadata>
 <metadata name="Description"></metadata>
 <metadata name="Designer"></metadata>
 <metadata name="DesignerCover"></metadata>
 <metadata name="DesignerUserId"></metadata>
 <metadata name="License"></metadata>
 <metadata name="ModificationDate">2023-09-22</metadata>
 <metadata name="Origin"></metadata>
 <metadata name="Title"></metadata>
 <resources>
  <object id="2" p:uuid="00000001-61cb-4c03-9d28-80fed5dfa1dc" type="model">
   <components>
    <component p:path="/3D/Objects/OpenSCAD Model_1.model" objectid="1" transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
   </components>
  </object>
  <object id="4" p:uuid="00000002-61cb-4c03-9d28-80fed5dfa1dc" type="model">
   <components>
    <component p:path="/3D/Objects/OpenSCAD Model_2.model" objectid="3" transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
   </components>
  </object>
  <object id="6" p:uuid="00000003-61cb-4c03-9d28-80fed5dfa1dc" type="model">
   <components>
    <component p:path="/3D/Objects/OpenSCAD Model_3.model" objectid="5" transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
   </components>
  </object>
  <object id="8" p:uuid="00000004-61cb-4c03-9d28-80fed5dfa1dc" type="model">
   <components>
    <component p:path="/3D/Objects/OpenSCAD Model_4.model" objectid="7" transform="1 0 0 0 1 0 0 0 1 0 0 0"/>
   </components>
  </object>
 </resources>
 <build p:uuid="d8eb061-b1ec-4553-aec9-835e5b724bb4">
  <item objectid="2" p:uuid="00000002-b1ec-4553-aec9-835e5b724bb4" transform="1 0 0 0 1 0 0 0 1 160.251097 160.519201 10" printable="1"/>
  <item objectid="4" p:uuid="00000004-b1ec-4553-aec9-835e5b724bb4" transform="1 0 0 0 1 0 0 0 1 100.251097 160.519201 10" printable="1"/>
  <item objectid="6" p:uuid="00000006-b1ec-4553-aec9-835e5b724bb4" transform="1 0 0 0 1 0 0 0 1 100.251097 100.519201 10" printable="1"/>
  <item objectid="8" p:uuid="00000008-b1ec-4553-aec9-835e5b724bb4" transform="1 0 0 0 1 0 0 0 1 160.251097 100.519201 10" printable="1"/>
 </build>
</model>
"""

XML_DATA3 = """\
<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:slic3rpe="http://schemas.slic3r.org/3mf/2017/06" xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" requiredextensions="p">
 <metadata name="BambuStudio:3mfVersion">1</metadata>
 <resources>
  <object id="3" type="model">
   <mesh>
    <vertices>
     <vertex x="-10" y="-10" z="-10"/>
     <vertex x="-10" y="-10" z="10"/>
     <vertex x="-10" y="10" z="-10"/>
     <vertex x="-10" y="10" z="10"/>
     <vertex x="10" y="-10" z="-10"/>
     <vertex x="10" y="-10" z="10"/>
     <vertex x="10" y="10" z="-10"/>
     <vertex x="10" y="10" z="10"/>
    </vertices>
    <triangles>
     <triangle v1="0" v2="1" v3="3"/>
     <triangle v1="0" v2="2" v3="6"/>
     <triangle v1="0" v2="3" v3="2"/>
     <triangle v1="0" v2="4" v3="5" paint_color="4"/>
     <triangle v1="0" v2="5" v3="1" paint_color="4"/>
     <triangle v1="0" v2="6" v3="4"/>
     <triangle v1="1" v2="5" v3="3" paint_color="0C"/>
     <triangle v1="2" v2="3" v3="6"/>
     <triangle v1="3" v2="5" v3="7" paint_color="0C"/>
     <triangle v1="3" v2="7" v3="6"/>
     <triangle v1="4" v2="6" v3="5"/>
     <triangle v1="5" v2="6" v3="7"/>
    </triangles>
   </mesh>
  </object>
 </resources>
</model>
"""


class ExtrudeTest(TestCase):
    def getXml(self):
        return etree.fromstring(XML_DATA.encode("utf-8"))

    def getXml2(self):
        return etree.fromstring(XML_DATA2.encode("utf-8"))

    def getXml3(self):
        return etree.fromstring(XML_DATA3.encode("utf-8"))

    def testSerializationSpec_config(self):
        config, status = CONFIG_SERIALIZATION_SPEC.deserialize(self.getXml())
        self.assertEqual(status.contains_unknown_elements, False)
        self.assertEqual(status.contains_unknown_attributes, False)
        self.assertEqual(len(config.objects), 4)

        new_tree = CONFIG_SERIALIZATION_SPEC.serialize(config)
        config1, status = CONFIG_SERIALIZATION_SPEC.deserialize(new_tree)
        self.assertEqual(config, config1)

    def testSerializationSpec_model2(self):
        model, status = MODEL_SERIALIZATION_SPEC.deserialize(self.getXml2())
        self.assertEqual(status.contains_unknown_elements, False)
        self.assertEqual(status.contains_unknown_attributes, False)
        self.assertEqual(len(model.build.items), 4)

        new_tree = MODEL_SERIALIZATION_SPEC.serialize(model)
        model1, status = MODEL_SERIALIZATION_SPEC.deserialize(new_tree)
        self.assertEqual(model, model1)

    def testSerializationSpec_model3(self):
        model, status = MODEL_SERIALIZATION_SPEC.deserialize(self.getXml3())
        self.assertEqual(status.contains_unknown_elements, False)
        self.assertEqual(status.contains_unknown_attributes, False)
        self.assertEqual(len(model.resources.objects[0].mesh.vertices.vertices), 8)

        new_tree = MODEL_SERIALIZATION_SPEC.serialize(model)
        model1, status = MODEL_SERIALIZATION_SPEC.deserialize(new_tree)
        self.assertEqual(model, model1)


if __name__ == "__main__":
    # import sys; sys.argv = ['', 'ExtrudeTest.testDeserialize3']
    main()
