# 사용 안내

스킬 폴더 전체를 설치한 뒤 `$korean-writing`으로 요청한다. [SKILL.md](../skills/korean-writing/SKILL.md)만 복사하면 필요한 참조와 UI 메타데이터가 빠진다.

## 릴리스 ZIP으로 설치하기

1. [v0.1.0 릴리스](https://github.com/monancho/korean-writing-skill/releases/tag/v0.1.0)에서 `korean-writing-0.1.0.zip`과 `SHA256SUMS.txt`를 받는다.
2. 아래 명령의 SHA256을 `SHA256SUMS.txt`에 적힌 값과 비교한다.
3. ZIP을 새 폴더에 풀고 `korean-writing/` 폴더 전체를 대상 프로젝트의 `.agents/skills/` 아래에 복사한다. 같은 이름의 스킬이 있으면 내용과 판본을 비교한 뒤 갱신한다.

```powershell
Get-FileHash -LiteralPath './korean-writing-0.1.0.zip' -Algorithm SHA256
```

설치 폴더 안에는 `LICENSE`가 포함돼 있다. ZIP 루트의 `manifest.json`은 파일별 해시를 담은 무결성 확인 자료이며 스킬 지침 파일이 아니다.

## 저장소에서 설치하기

`skills/korean-writing/` 폴더 전체를 대상 프로젝트의 `.agents/skills/korean-writing/`에 복사하고, 저장소 루트의 `LICENSE`도 그 설치 폴더에 넣는다.

다음 PowerShell 예시는 이 저장소 루트에서 실행한다. `../my-project`를 실제 대상 프로젝트로 바꾼다. 기존 같은 이름의 스킬을 발견하면 중단해 먼저 비교하도록 했다.

```powershell
$targetProject = Resolve-Path -LiteralPath '../my-project'
$targetSkill = Join-Path $targetProject '.agents/skills/korean-writing'
if (Test-Path -LiteralPath $targetSkill) { throw '같은 이름의 스킬이 이미 있습니다. 내용을 먼저 비교하세요.' }
New-Item -ItemType Directory -Path (Split-Path -Parent $targetSkill) -Force | Out-Null
Copy-Item -LiteralPath './skills/korean-writing' -Destination $targetSkill -Recurse
Copy-Item -LiteralPath './LICENSE' -Destination (Join-Path $targetSkill 'LICENSE')
```

공식 [로컬 스킬 탐색·호출 안내](https://learn.chatgpt.com/docs/build-skills)는 Codex의 프로젝트 `.agents/skills`와 사용자 스킬 위치를 설명한다. 다른 Agent Skills 호스트에서는 해당 제품의 등록 위치와 호출 방식을 확인한다. 플러그인 마켓 등록이나 모든 제품의 자동 선택은 검증하지 않았다.

확인한 설치 범위는 격리된 작업 폴더에 파일을 복사하고 바이트와 공식 스킬 검사를 대조한 것이다. 사용자 전역 설치와 설치된 제품의 자동 탐색·호출은 수행하지 않았다.

## 요청하기

목적·독자·자료·채널·격식·원하는 결과 중 필요한 정보만 제공한다. 짧은 문장 수정에 별도 입력 양식을 채울 필요는 없다.

수정 요청:

```text
$korean-writing으로 다음 문구를 다듬어 주세요.
대상: 함께 일하는 팀원 / 채널: Slack / 격식: 공손하되 간결하게
원문: 검토가 끝나면 게시 여부를 논의할 수 있습니다.
조건과 가능성은 유지하고 수정본만 주세요.
```

검토 요청:

```text
$korean-writing으로 문제 위치와 이유만 검토해 주세요. 재작성은 하지 마세요.
원문: 첫 절에는 검토 미정, 마지막 절에는 검토 완료라고 적혀 있습니다.
```

작성 요청:

```text
$korean-writing으로 ADR 제안을 작성해 주세요.
제공한 대안·기준·장단점으로 권장안을 정리하되 승인된 결정으로 쓰지 마세요.
결정자와 일정은 미정입니다.
```

작성은 요청한 글, 수정은 수정본, 검토는 문제 위치·이유·수정 방향을 기본 결과로 낸다. 결합 요청은 사용자가 지정한 순서로 처리한다. 점수·등급·전체 체크리스트를 기본으로 출력하지 않는다. 이미 적절한 원문은 유지하며 선택 입력이 없다고 무조건 질문하지 않는다.

## 결과를 확인할 때

사실·수치·조건·부정·확신의 정도·사용자 의도가 원문과 같은지 확인한다. 정확한 인용과 기술 식별자는 보존하며 근거가 없으면 미확인으로 남긴다. 지침형 스킬이므로 사실의 진실성, 법률·전문 판단, 고정된 출력이나 한국어 개선 효과를 보증하지 않는다.

Word/PDF/HWPX 생성과 외부 발송은 실제 환경의 별도 도구와 사용자 위임에 따른다. 확인한 구성 검사와 작성자 직접 적용은 다른 모델의 성능이나 사람 사용성 수락을 입증하지 않는다. 문제가 생기면 원문·요청·달라진 의미 조건·사용 판본을 연결해 남긴다. 개인정보나 비공개 내용이 있는 실제 문서 대신 문제를 설명할 가상 자료로 제보한다. [기여 안내](../CONTRIBUTING.md)와 [검증 보고](verification-report.md)를 함께 확인한다.
