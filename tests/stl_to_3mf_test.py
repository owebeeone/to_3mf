import io
import os
from unittest import TestCase, main
from to_3mf.stl_to_3mf import stl_to_3mf, stl_to_scad
from zipfile import ZipFile


class TestStlTo3mf(TestCase):
    def setUp(self):
        # Get the directory containing test files
        self.test_dir = os.path.join(os.path.dirname(__file__), "test-data")

    def assertZipEqual(self, zip_data1, zip_path2, msg=None):
        """Assert that a ZIP file in memory equals a ZIP file on disk.

        Args:
            zip_data1: A file-like object containing ZIP data
            zip_path2: Path to ZIP file to compare against
            msg: Optional message prefix for failure messages
        """
        msg_prefix = f"{msg}: " if msg else ""

        with ZipFile(zip_data1, "r") as zip1, ZipFile(zip_path2, "r") as zip2:
            # Compare file lists
            files1 = sorted(zip1.namelist())
            files2 = sorted(zip2.namelist())
            self.assertEqual(files1, files2, f"{msg_prefix}ZIP files contain different files")

            # Compare contents of each file
            for filename in files1:
                with zip1.open(filename) as f1, zip2.open(filename) as f2:
                    content1 = f1.read()
                    content2 = f2.read()
                    self.assertEqual(
                        content1, content2, f"{msg_prefix}Content mismatch in {filename}"
                    )

    def test_stl_to_3mf(self):
        # Input STL files
        stl_files = [
            os.path.join(self.test_dir, "test_file_01.stl"),
            os.path.join(self.test_dir, "test_file_02.stl"),
        ]

        # Create an in-memory buffer for the output
        output_buffer = io.BytesIO()

        # Convert STL to 3MF
        status = stl_to_3mf(stl_files, output_buffer)

        # Check conversion was successful
        self.assertEqual(status, 0)

        # Compare ZIP contents
        output_buffer.seek(0)  # Reset buffer position to start
        golden_path = os.path.join(self.test_dir, "test_result.3mf")
        self.assertZipEqual(output_buffer, golden_path, "3MF file comparison")

    def test_stl_to_scad(self):
        # Input STL files
        stl_files = [
            os.path.join(self.test_dir, "test_file_01.stl"),
            os.path.join(self.test_dir, "test_file_02.stl"),
        ]

        # Create an in-memory buffer for the output
        output_buffer = io.StringIO()

        # Convert STL to SCAD
        stl_to_scad(stl_files, output_buffer)

        # Get the resulting string
        result = output_buffer.getvalue()

        # Compare with golden file
        golden_path = os.path.join(self.test_dir, "test_result.scad")
        with open(golden_path, "r") as f:
            golden_data = f.read()

        self.assertEqual(result, golden_data)


if __name__ == "__main__":
    # import sys; sys.argv = ['', 'ExtrudeTest.testDeserialize3']
    main()
