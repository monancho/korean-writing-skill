"""배포 파일의 구성·경로·UTF-8을 확인한다. 문장 품질은 판정하지 않는다."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PRIVATE = re.compile(r"https?://[^/\s]+\.(?:atlassian\.net|slack\.com)(?:/|\b)|[A-Z]:[\\/]Users[\\/]", re.I)


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    skill = root / "skills/korean-writing"
    entry = skill / "SKILL.md"
    if not entry.is_file():
        return ["핵심 SKILL.md가 없습니다."]
    metadata = skill / "agents/openai.yaml"
    if not metadata.is_file():
        errors.append("배포용 UI 메타데이터 agents/openai.yaml이 없습니다.")
    reachable: set[Path] = {entry.resolve(), metadata.resolve()}
    for path in sorted(root.rglob("*")):
        if any(p in {".git", "dist", "__pycache__", ".venv"} for p in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            errors.append(f"배포 후보에 심볼릭 링크가 있습니다: {path.relative_to(root)}")
            continue
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".json", ".csv", ".yaml", ".yml", ".py"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"UTF-8 읽기 실패: {path.relative_to(root)}")
            continue
        if PRIVATE.search(text):
            errors.append(f"내부 URL·개인 경로 후보: {path.relative_to(root)}")
        if path.suffix != ".md":
            continue
        for value in LINK.findall(text):
            value = unquote(value.strip("<>"))
            if value.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", value):
                continue
            target = (path.parent / value.split("#", 1)[0]).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"저장소 밖 참조: {path.relative_to(root)} → {value}")
                continue
            if path.is_relative_to(skill) and not target.is_relative_to(skill):
                errors.append(f"스킬 배포 범위 밖 참조: {path.relative_to(root)} → {value}")
                continue
            if not target.exists():
                errors.append(f"없는 참조: {path.relative_to(root)} → {value}")
            if path == entry:
                reachable.add(target)
    for path in skill.rglob("*"):
        if path.is_file() and path.resolve() not in reachable:
            errors.append(f"핵심에서 찾을 수 없는 자원: {path.relative_to(root)}")
    try:
        text = entry.read_text(encoding="utf-8")
    except UnicodeError:
        return errors
    frontmatter_match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    frontmatter = frontmatter_match.group(1) if frontmatter_match else ""
    if frontmatter_match is None:
        errors.append("YAML frontmatter 경계가 없습니다.")
    if not re.search(r"(?m)^name: korean-writing$", frontmatter):
        errors.append("스킬명과 폴더명이 일치하지 않습니다.")
    if not re.search(r"(?m)^description: \S", frontmatter):
        errors.append("호출 설명이 없습니다.")
    if not re.search(r"(?m)^license: MIT$", frontmatter):
        errors.append("릴리스 라이선스 표기가 MIT와 일치하지 않습니다.")
    license_file = root / "LICENSE"
    if not license_file.is_file():
        errors.append("배포용 LICENSE가 없습니다.")
    else:
        try:
            license_text = license_file.read_text(encoding="utf-8")
            if "MIT License" not in license_text or "Copyright (c) 2026 monancho" not in license_text:
                errors.append("MIT 저작권·허가 고지를 확인할 수 없습니다.")
        except UnicodeError:
            errors.append("LICENSE UTF-8 읽기 실패")
    if re.search(r"\bTODO\b|\[TODO", text):
        errors.append("핵심 지침에 미완성 표시가 있습니다.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check(args.root)
    print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors}, ensure_ascii=True))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())

