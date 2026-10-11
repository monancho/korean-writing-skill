"""손상된 배포 후보의 거부와 아카이브 무결성을 확인한다."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_package import check
from build_package import build


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT / "skills", self.root / "skills")
        shutil.copyfile(ROOT / "LICENSE", self.root / "LICENSE")
        self.entry = self.root / "skills/korean-writing/SKILL.md"

    def test_current_package(self):
        self.assertEqual(check(ROOT), [])

    def test_missing_reference_is_rejected(self):
        (self.root / "skills/korean-writing/references/messages.md").unlink()
        self.assertTrue(any("없는 참조" in error for error in check(self.root)))

    def test_reference_escape_is_rejected(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8") + "\n[잘못된 자원](../../../../outside.md)\n", encoding="utf-8")
        self.assertTrue(any("저장소 밖" in error for error in check(self.root)))

    def test_wrong_name_is_rejected(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8").replace("name: korean-writing", "name: other-skill"), encoding="utf-8")
        self.assertTrue(any("스킬명" in error for error in check(self.root)))

    def test_non_utf8_metadata_is_rejected(self):
        (self.root / "skills/korean-writing/agents/openai.yaml").write_bytes("한국어".encode("cp949"))
        self.assertTrue(any("UTF-8" in error for error in check(self.root)))

    def test_unreachable_resource_is_rejected(self):
        (self.root / "skills/korean-writing/references/unused.md").write_text("미참조 자원", encoding="utf-8")
        self.assertTrue(any("찾을 수 없는" in error for error in check(self.root)))

    def test_private_material_is_rejected(self):
        url = "https://" + "private.example.atlassian.net/wiki/page"
        self.entry.write_text(self.entry.read_text(encoding="utf-8") + "\n" + url + "\n", encoding="utf-8")
        self.assertTrue(any("내부 URL" in error for error in check(self.root)))

    def test_missing_license_is_rejected(self):
        (self.root / "LICENSE").unlink()
        self.assertTrue(any("배포용 LICENSE" in error for error in check(self.root)))

    def test_mismatched_license_metadata_is_rejected(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8").replace("license: MIT", "license: other"), encoding="utf-8")
        self.assertTrue(any("라이선스 표기" in error for error in check(self.root)))

    def test_reproducible_archive_has_exact_files_and_hashes(self):
        first, second = Path(self.temp.name) / "first.zip", Path(self.temp.name) / "second.zip"
        self.assertEqual(build(self.root, first)["sha256"], build(self.root, second)["sha256"])
        with ZipFile(first) as archive:
            manifest = json.loads(archive.read("manifest.json"))
            self.assertEqual(manifest["version"], "0.1.0")
            self.assertEqual(manifest["license"], "MIT")
            self.assertEqual(manifest["release_channel"], "stable")
            self.assertEqual(archive.read("korean-writing/LICENSE"), (ROOT / "LICENSE").read_bytes().replace(b"\r\n", b"\n"))
            self.assertEqual(set(archive.namelist()), set(manifest["files"]) | {"manifest.json"})
            for name, sha in manifest["files"].items():
                self.assertFalse(Path(name).is_absolute())
                self.assertNotIn("..", Path(name).parts)
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), sha)


if __name__ == "__main__":
    unittest.main()

