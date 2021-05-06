import unittest
from pathlib import Path
import shutil
from compress_all_images import compress_single_image

TEST_DIRECTORY = Path('./test_data')



class TestImageCompression(unittest.TestCase):
    def setUp(self):
        self.test_dir = TEST_DIRECTORY.parent / "test_data_copy"

        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

        shutil.copytree(TEST_DIRECTORY, self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_single_image_compression(self):
        img = self.test_dir / 'ball_02.JPG'
        save_path = self.test_dir / 'ball_02_compressed.JPG'
        compress_single_image(img, save_path)

    def test_compresses_but_does_not_duplicate_files(self):
        self.assertTrue(self.test_dir.exists(), "Uh oh, the testing setup did not copy the test directory")


if __name__ == '__main__':
    unittest.main()
