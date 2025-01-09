import os
from io import BytesIO
from unittest import TestCase, main
from to_3mf.slicer_project_file_editor import SlicerProjectFileEditor, Options
from zipfile import ZipFile

class TestSlicerProjectFileEditor(TestCase):
    def setUp(self):
        # Get the directory containing test files
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test-data')
        self.test_3mf = os.path.join(self.test_dir, 'test_result.3mf')
        
        # Create default options - disable warnings/assertions for unknown attributes
        self.options = Options(
            print_xml_unused=False,
            assert_xml_unused=False,
            recover_xml_errors=True,
            recover_undeclared_namespace=True)
        
        # Load test file into memory
        with open(self.test_3mf, 'rb') as f:
            self.test_3mf_data = f.read()
            
    def test_load_3mf_from_memory(self):
        """Test loading a 3MF file from memory"""
        output = BytesIO()
        
        # Create editor with in-memory data
        editor = SlicerProjectFileEditor(
            template_file=BytesIO(self.test_3mf_data),
            output_file=output,
            options=self.options)
        
        # Verify model files were loaded
        self.assertTrue(len(editor.model.model_files) > 0, 
                       "No model files were loaded from 3MF")
        
        # Write to in-memory buffer
        editor.write()
        
        # Verify the written content matches original
        output.seek(0)
        with ZipFile(BytesIO(self.test_3mf_data)) as original_zip, \
             ZipFile(output) as written_zip:
            
            # Compare file lists
            self.assertEqual(
                sorted(original_zip.namelist()),
                sorted(written_zip.namelist()),
                "File lists don't match")
            
            # Compare contents of each file
            for filename in original_zip.namelist():
                with original_zip.open(filename) as f1, \
                     written_zip.open(filename) as f2:
                    self.assertEqual(
                        f1.read(),
                        f2.read(),
                        f"Content mismatch in {filename}")

    def test_file_classification(self):
        """Test the file classification methods"""
        output = BytesIO()
        editor = SlicerProjectFileEditor(
            template_file=BytesIO(self.test_3mf_data),
            output_file=output,
            options=self.options)
        
        # Test model file detection
        self.assertTrue(editor.is_model_file("some/path/file.model"))
        self.assertFalse(editor.is_model_file("some/path/file.txt"))
        
        # Test config file detection
        self.assertTrue(editor.is_config_file("Metadata/model_settings.config"))
        self.assertTrue(editor.is_config_file("Metadata/Slic3r_PE_model.config"))
        self.assertFalse(editor.is_config_file("some/other/file.config"))

if __name__ == "__main__":
    main() 