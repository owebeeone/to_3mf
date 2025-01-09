# to_3mf
A set of Python tools for managing the 3mf file format. Includes an STL to 3mf file converter.

## STL to 3MF Converter

The `stl_to_3mf.py` script converts one or more STL files into a single 3MF file or OpenSCAD file. Each STL model is assigned a unique color in the output 3MF file.

### Performance

Even though the code is written in Python, the conversion is very fast. The STL to 3MF conversion uses numpy and the conversion from STL triangles to indexed triangles is very fast
on numpy accelerated systems.

### Usage

You can run the converter using Python's module syntax (the output file name must end in .3mf):

```
python -m to_3mf.stl_to_3mf <stl_file_1> <stl_file_2> <output_file>.3mf
```

Or to convert to OpenSCAD format (file name must end in .scad):

```
python -m to_3mf.stl_to_3mf <stl_file_1> <stl_file_2> <output_file>.scad
```

### Programmatic Usage

The `stl_to_3mf` function can be used to convert STL files to 3MF or OpenSCAD files programmatically.

```
from to_3mf.stl_to_3mf import stl_to_3mf

stl_to_3mf(['test_file_01.stl', 'test_file_02.stl'], 'test_result.3mf')
```

Or you can get in memory representation like this:

```python
from to_3mf.stl_to_3mf import stl_to_model_group, ModelGroup

# Convert STL files to 3MF
models: ModelGroup = stl_to_model_group(stl_files)
```

### Future

This was a quick and dirty implementation. I'm interested in providing more features 
but right now, it's seems like it's all I need. The threemf_model and threemf_config
modules are not used here as this pre-dates the xdatatree libraries.

## 3MF Model and Config APIs

The package provides two main APIs for working with 3MF files:

### ThreeMF Model API

The `threemf_model` module provides classes for working with the core 3MF model structure:

```python
from to_3mf.threemf_model import Model, Object, Mesh, Vertices, Triangles
import numpy as np

# Create a new 3MF model
model = Model(
    unit="millimeter",
    lang="en-US"
)

# Add a mesh object
mesh = Mesh(
    vertices=Vertices(vertices=np.array([[0,0,0], [1,0,0], [0,1,0]])),
    triangles=Triangles(triangles_paint_colors=(
        np.array([[0,1,2]]),
        ["#FF0000"]
    ))
)

# Add an object to the model
obj = Object(
    id=1,
    type="model",
    mesh=mesh
)

# Add the object to the model
model.resources.objects.append(obj)

# Serialize the model to XML
xml_content = SERIALIZATION_SPEC.serialize(model)

# Deserialize the model from XML
model: Model = SERIALIZATION_SPEC.deserialize(xml_content)
```

### ThreeMF Config API

The `threemf_config.py` module provides classes for working with 3MF printer configuration data:

```python
from to_3mf.threemf_config import Config, Object, Part

# Create a new config
config = Config()

# Add an object with parts
obj = Object(
        id=1,
        name="MyObject",
        parts=[
            Part(
                id="1",
                name="Part1",
                matrix=[1,0,0,0, 0,1,0,0, 0,0,1,0],
                source_file="model.stl"
            )
        ]
    )
config.objects.append(obj)

# Serialize the config to XML
xml_content = SERIALIZATION_SPEC.serialize(config)

# Deserialize the config from XML
config: Config = SERIALIZATION_SPEC.deserialize(xml_content)
```
