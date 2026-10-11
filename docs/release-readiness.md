# 공개 결정과 v0.1.0 릴리스 인계

2026-10-12 Asia/Seoul, 사용자 위임에 따라 기존 `monancho/korean-writing-skill`을 공개하고 MIT를 확정해 첫 정식 릴리스 `v0.1.0`을 게시했다. 이 문서는 실제 결정·배포 구성·게시 확인을 연결한다.

## 결정 기록 — DACI 형식

| 역할·항목 | 실제 내용 |
|---|---|
| 결정 권한 | 실제 사용자가 이 프로젝트의 공개·라이선스 확정·정식 릴리스를 명시적으로 위임함 |
| 실행과 선택 | Codex가 위임 범위에서 MIT와 v0.1.0을 선택하고 변경·검증·PR 병합·게시·재조회를 수행함 |
| 기여·통지 | 별도 검토자나 기한은 지정되지 않음. 저장소 소유자는 monancho |
| 대상 | 기존 monancho/korean-writing-skill의 공개 저장소와 정식 GitHub Release |
| 선택 이유 | 자체 작성 지침·코드·예시의 재사용을 허용하고 저작권·허가 고지를 유지하는 단순한 배포 조건 |
| 대안 | Apache-2.0의 명시 특허 조항 등을 비교했으나 이 판본에 적용하지 않음 |
| 영향 | 저장소 파일·이력·PR·CI 로그·작성자 메타데이터가 공개됨. 외부 원출처의 권리는 그대로 유지됨 |

[MIT 원문](https://opensource.org/license/mit)을 LICENSE에 반영하고 스킬 메타데이터와 ZIP manifest를 MIT로 맞췄다. 권리 경계는 [자료와 권리 고지](../NOTICE.md)에 있다. 비공개 구현 후보의 라이선스 미결·공개 미수행 문구는 당시 이력이다.

## 배포 구성

| 자료 | 포함 범위 | 실제 확인 |
|---|---|---|
| 설치 ZIP | SKILL.md·참조 5개·UI 메타데이터·LICENSE: 8개 파일, 별도 manifest.json | 경로·개수·파일별 SHA256·MIT 본문·반복 빌드 동일성 |
| SHA256SUMS.txt | ZIP 전체의 SHA256과 파일명 | 로그인 없이 내려받은 ZIP의 해시와 대조 |
| 저장소·소스 아카이브 | skills·scripts·tests·CI·문서·외부 링크와 자체 메모·목적 분석·고지 | 공개 범위·Git 이력·PR·CI 로그 직접 확인 |
| GitHub 실행 증거 | PR HEAD·병합 커밋·main CI·태그·릴리스 속성·자산 | 원본 재조회 |

## 게시 결과

| 항목 | 확인한 값·원본 |
|---|---|
| 저장소 | [monancho/korean-writing-skill](https://github.com/monancho/korean-writing-skill), PUBLIC·MIT |
| 릴리스 | [v0.1.0](https://github.com/monancho/korean-writing-skill/releases/tag/v0.1.0), draft=false·prerelease=false |
| 게시 시각 | 2026-10-12 01:31:54 Asia/Seoul |
| 태그가 가리키는 커밋 | e4121903bc1df0bcc04d5f03931d51c5bf404050 |
| 릴리스 변경 PR | [PR #2](https://github.com/monancho/korean-writing-skill/pull/2), 병합 완료 |
| 정확한 PR HEAD | b2c5792a92633d4e2cdbdcf28e0e1adf51d5bb23 |
| HEAD CI | [구성·패키지 검사](https://github.com/monancho/korean-writing-skill/actions/runs/38155616656)·[PR 검사](https://github.com/monancho/korean-writing-skill/actions/runs/38155633167), 성공 |
| 릴리스 커밋의 main CI | [실행 38155713469](https://github.com/monancho/korean-writing-skill/actions/runs/38155713469), 성공 |
| 설치 ZIP | korean-writing-0.1.0.zip, 11,657바이트 |
| ZIP SHA256 | 8714377fdcc22d6da357e8c1903889141d115e59918facb9999b3b7cb5b24cd2 |

라이선스·패키지 변경을 검토 가능한 PR로 만들고 공식 검사·구성 검사·10개 시험·반복 빌드·설치 파일 대조를 수행했다. 정확한 HEAD의 CI 성공 후 위임 범위에서 병합했고, 병합 후 CI와 파일 동일성을 확인했다. 병합 판본에 태그를 연결해 ZIP·체크섬·한국어 안내를 게시한 뒤 인증 없는 조회로 가시성·태그 커밋·릴리스 속성·자산 바이트를 확인했다.

위 main CI는 릴리스 커밋의 기록이다. 이후 문서 변경 등 저장소 main의 최신 결과와 구분한다.

## 인계와 남은 확인

독립 순방향 시험·사람 사용성 평가·호스트 자동 선택·효과 수치·확정 일정은 이 릴리스의 완료 조건에 포함하지 않았다. 확인 수준은 [검증 보고](verification-report.md)에 있다. 결함 제보는 저장소 Issues로 받으며 응답 기한은 지정하지 않았다. 공개 이후 내려받은 사본의 회수는 보장하지 않는다.
