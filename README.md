# to_3mf
A set of Python tools for managing the 3mf file format. Includes an STL to 3mf file converter.

## Installation

```
pip install to_3mf
```

## STL to 3MF Converter

The `stl_to_3mf.py` script converts one or more STL files into a single 3MF file or OpenSCAD file. Each STL model is assigned a unique color in the output 3MF file.

### Performance

Even though the code is written in Python, the conversion is very fast. The STL to 3MF conversion uses numpy and the conversion from STL triangles to indexed triangles is very fast
on numpy accelerated systems.

### Usage

You can run the converter using Python's module syntax (the output file name must end in .3mf):

```
python -m to_3mf.stl_to_3mf <stl_file_1> ... <stl_file_N> <output_file>.3mf
```

Or to convert to OpenSCAD format (file name must end in .scad):

```
python -m to_3mf.stl_to_3mf <stl_file_1> ... <stl_file_N> <output_file>.scad
```

### Programmatic Usage

Used as a module, the `to_3mf.stl_to_3mf` function `stl_to_3mf` can be used to convert STL files to 3MF or `stl_to_scad` can be used to convert STL files to OpenSCAD files programmatically.

```
from to_3mf.stl_to_3mf import stl_to_3mf

stl_to_3mf(['test_file_01.stl', 'test_file_02.stl'], 'test_result.3mf')
```

Or you can get in memory representation like this:

```python
from to_3mf.stl_to_3mf import stl_to_3mf

# Create an in-memory buffer for the output
output_buffer = io.BytesIO()
# Convert STL to 3MF
stl_to_3mf(stl_files, output_buffer)

# Or convert to OpenSCAD
output_buffer = io.StringIO()
stl_to_scad(stl_files, output_buffer)
```

### Future

This was a quick and dirty implementation. There is interest in providing more features 
but right now, it's seems like it's all that is needed. The threemf_model and threemf_config
modules are not used here as this pre-dates the xdatatree libraries.

## 3MF Model and Config APIs `threemf_model` and `threemf_config`

The `to_3mf` package provides XML serialization/deserialization APIs for working with 3MF files. These are a work in progress but are functional.

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
## Slicer Project File Editor

The `slicer_project_file_editor.py` module provides tools for manipulating 3MF slicer project files. This is particularly useful for working with slicer-specific 3MF files that contain both model data and printer configuration settings.

**Note: This is a work in progress and the API will change.**

### Usage

```python
from to_3mf.slicer_project_file_editor import SlicerProjectFileEditor, Options
from io import BytesIO

# Create options for the editor
options = Options(
    print_xml_unused=False,      # Don't print warnings about unknown XML elements
    assert_xml_unused=False,     # Don't assert on unknown XML elements
    recover_xml_errors=True,     # Try to recover from XML parsing errors
    recover_undeclared_namespace=True  # Handle undeclared XML namespaces
)

# Create editor from a template file
editor = SlicerProjectFileEditor(
    template_file="input.3mf",
    output_file="output.3mf", 
    options=options
)

# Make changes to the file here....

# Write the modified project
editor.write()
```

### Command Line Interface

The editor can also be used from the command line:

```bash
python -m to_3mf.slicer_project_file_editor input.3mf output.3mf [options]
```

Options include:
- `--print-xml-unused/--noprint-xml-unused`: Control warnings about unknown XML elements
- `--assert-xml-unused/--noassert-xml-unused`: Control assertions on unknown XML elements
- `--recover-xml-errors/--norecover-xml-errors`: Control XML error recovery
- `--recover-undeclared-namespace/--norecover-undeclared-namespace`: Control handling of undeclared namespaces

### Features

- Load and parse 3MF slicer project files
- Access and modify model data and printer configurations
- Handle multiple model files within a single project
- Preserve metadata and other project files
- Support for both file-based and in-memory operations

The editor uses the `threemf_model` and `threemf_config` APIs internally to parse and manipulate the 3MF data structures.
