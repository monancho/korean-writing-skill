# 한국어 업무 작성 스킬

한국어 글·업무 문서·Slack 문구의 작성, 수정, 검토를 돕는 지침형 Agent Skill이다. 사실·수치·조건·부정·확신의 정도와 사용자 의도를 보존하는 것을 우선한다.

첫 정식 판본은 **v0.1.0**이다. 한 진입점과 다섯 조건부 참조를 구현했다. 자체 스킬·문서·코드·가상 예시는 [MIT 라이선스](LICENSE)로 제공한다.

[정식 릴리스와 ZIP 다운로드](https://github.com/monancho/korean-writing-skill/releases/tag/v0.1.0)에서 `korean-writing-0.1.0.zip`과 `SHA256SUMS.txt`를 받는다. ZIP은 스킬 파일 7개·MIT 고지·파일별 해시 manifest를 포함한다.

## 사용하기

[스킬 본문](skills/korean-writing/SKILL.md)과 폴더 전체를 사용한다. 프로젝트 `.agents/skills/korean-writing/`에 복사하는 방법과 명시 호출은 [사용 안내](docs/usage.md)에 있다. 사용자 전역 설치를 자동 수행하지 않는다.

```text
$korean-writing으로 이 Slack 문구를 공손하고 간결하게 다듬어 주세요.
조건과 가능성은 유지하고 수정본만 주세요.
```

작성·수정·검토를 구분하며 이미 적절한 글은 유지한다. 점수·등급·긴 변경표를 기본 출력하지 않는다. 문서 파일 생성·외부 발송은 실제 환경의 별도 도구·위임을 따른다.

## 산출물과 근거

- [설계 결정](docs/adr/0001-entrypoint.md) · [구현 계획](docs/implementation-plan.md) · [구현 기록](docs/implementation-record.md)
- [요구 추적](docs/requirements-traceability.md) · [검증 보고와 실제 관찰](docs/verification-report.md)
- [연구·공개 스킬·템플릿 조사](research/README.md) · [출처/자산 범위](docs/source-and-assets.md)
- [공개 범위와 릴리스 인계](docs/release-readiness.md) · [공개 점검과 릴리스 검증](docs/publication-review.md) · [변경 기록](CHANGELOG.md) · [유지관리](CONTRIBUTING.md)

기본 구성·UTF-8·참조와 ZIP 무결성 시험을 수행했다. 28개 사례는 작성자 직접 적용·도구 경계의 가상 대응·파일 정적 확인을 구분한다. 독립 검토·호스트 자동 선택·다른 환경의 실제 설치·글쓰기 효과를 검증한 결과는 아니다.

