# 사용 안내

## 로컬로 사용하기

`skills/korean-writing/` 전체 폴더를 사용한다. `SKILL.md`만 복사하면 참조와 UI 메타데이터가 빠진다. 이 저장소는 현재 비공개이므로 GitHub에서 받을 때 접근 권한이 필요하다. 아래 명령은 설치 예시이며 이번 작업에서 사용자 전역 환경에 실행하지 않았다.

Codex에서 프로젝트 범위로 쓰려면 해당 프로젝트의 `.agents/skills/korean-writing/`에 폴더 전체를 복사한다. 목적지에 같은 이름의 스킬이 이미 있으면 원문과 버전을 비교한 뒤 병합·대체 여부를 판단한다.

PowerShell 예시 — 이 저장소 루트에서 실행한다. `../my-project`는 실제 대상 프로젝트로 바꾼다.

```powershell
$targetProject = Resolve-Path -LiteralPath '../my-project'
$targetSkill = Join-Path $targetProject '.agents/skills/korean-writing'
if (Test-Path -LiteralPath $targetSkill) { throw '같은 이름의 스킬이 이미 있습니다. 내용을 먼저 비교하세요.' }
New-Item -ItemType Directory -Path (Split-Path -Parent $targetSkill) -Force | Out-Null
Copy-Item -LiteralPath './skills/korean-writing' -Destination $targetSkill -Recurse
```

공식 [로컬 스킬 탐색·호출 안내](https://learn.chatgpt.com/docs/build-skills)에 따르면 Codex는 프로젝트 `.agents/skills`와 사용자 스킬 위치를 탐색한다. 다른 Agent Skills 호스트에서는 해당 호스트의 등록 위치·호출 방식을 확인한다. 플러그인 마켓 등록·모든 호스트의 자동 선택은 검증하지 않았다.

## 호출과 입력

명시 호출 예시:

```text
$korean-writing으로 다음 문구를 다듬어 주세요.
대상: 함께 일하는 팀원 / 채널: Slack / 격식: 공손하되 간결하게
원문: 검토가 끝나면 게시 여부를 논의할 수 있습니다.
조건과 가능성은 유지하고 수정본만 주세요.
```

```text
$korean-writing으로 문제 위치와 이유만 검토해 주세요. 재작성은 하지 마세요.
원문: 첫 절에는 검토 미정, 마지막 절에는 검토 완료라고 적혀 있습니다.
```

```text
$korean-writing으로 ADR 제안을 작성해 주세요.
제공한 대안·기준·장단점으로 권장안을 정리하되 승인된 결정으로 쓰지 마세요.
결정자와 일정은 미정입니다.
```

목적·독자·자료·채널·격식·원하는 결과 중 필요한 정보를 주면 된다. 간단한 요청에 별도 입력 양식을 강제하지 않는다. 충분히 적절한 원문은 유지하며 선택 입력이 없다고 무조건 질문하지 않는다.

## 결과와 제한

작성은 요청한 글, 수정은 수정본, 검토는 문제 위치·이유·방향을 낸다. 결합 요청은 요청 순서대로 처리한다. 기본으로 점수·등급·모든 체크리스트를 출력하지 않는다.

지침형 스킬이므로 사실의 진실성·법률/전문 판단·고정된 출력·한국어 개선 효과를 보증하지 않는다. 근거가 없으면 미확인으로 남기고 정확한 인용·식별자는 보존한다. Word/PDF/HWPX 생성과 외부 발송은 실제 환경의 별도 도구·위임에 따른다.

이번 확인은 구성 검사와 작성자 직접 적용이다. 실제 설치 후 자동 선택·다른 모델·사람 사용성 검토는 별도 확인해야 한다. 문제가 생기면 원문·요청·달라진 의미 조건·사용 판본을 연결해 남기고 개인정보를 포함한 실제 문서를 공개 이슈에 올리지 않는다.

