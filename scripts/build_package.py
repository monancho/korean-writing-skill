"""구성 확인을 마친 스킬과 LICENSE를 재현 가능한 릴리스 ZIP으로 만든다."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from check_package import check


def build(root: Path, destination: Path) -> dict:
    errors = check(root)
    if errors:
        raise ValueError("구성 확인 실패: " + "; ".join(errors))
    files = sorted((root / "skills/korean-writing").rglob("*"))
    data = {}
    for path in files:
        if path.is_file():
            name = path.relative_to(root / "skills").as_posix()
            data[name] = path.read_bytes().replace(b"\r\n", b"\n")
    data["korean-writing/LICENSE"] = (root / "LICENSE").read_bytes().replace(b"\r\n", b"\n")
    manifest = {"name": "korean-writing", "version": "0.1.0", "license": "MIT", "release_channel": "stable", "files": {name: hashlib.sha256(content).hexdigest() for name, content in data.items()}}
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for name, content in {**data, "manifest.json": (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")}.items():
            info = ZipInfo(name, date_time=(2026, 10, 12, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return {"path": str(destination), "files": len(data), "sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("dist/korean-writing-0.1.0.zip"))
    args = parser.parse_args()
    print(json.dumps(build(Path(__file__).resolve().parents[1], args.output), ensure_ascii=True))


if __name__ == "__main__":
    main()

