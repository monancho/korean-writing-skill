# 요구사항 추적

R1–R9 요구사항이 어느 지침과 사례에 연결되는지 확인하는 개발용 대응표다. K01–K12는 의미 보호 조건, B01–B11은 처리 분기, TC01–TC28은 확인 사례다. K 규칙은 핵심에 한 번 정의하고 참조는 적용 문맥을 제공한다. 이 식별자를 모든 사용자 결과에 출력하지 않는다.

## 요구사항별 대응

아래 대응의 근거는 구현 파일과 작성자 직접 적용 기록이다. 설치된 제품의 자동 스킬 선택이나 개선 효과를 확인한 표가 아니다. 실제 결과와 미수행 범위는 [검증 보고](verification-report.md)에서 확인한다.

| 요구 | 내용 | 의미 조건·분기 | 구현 책임 | 확인 사례 |
| --- | --- | --- | --- | --- |
| R1 | 작업·범위에 맞는 모드 | B01–B04; K08 K12 | 핵심 모드 해석 | TC01 TC15 TC27 TC28 |
| R2 | 독자·목적·채널 파악 | B05 B06; K01 K08 | 핵심 / documents·messages | TC01 TC16 TC17 TC23 |
| R3 | 사실·의미 보존 | K01–K11; B06 B07 | 핵심 / korean-language·evidence | TC02–TC12 TC17–TC19 TC22 |
| R4 | 한국어 격식·자연스러움 | K01 K04–K08 K12 | korean-language / messages | TC05 TC06 TC09 TC13 TC14 |
| R5 | 목적별 구성 | B01 B02 B10; K04 K09 | documents / messages | TC01 TC20 TC22 TC23 |
| R6 | 근거·미확인 구분 | B06–B08; K03 K06 K07 K09 K10 | 핵심 / evidence | TC07 TC08 TC10 TC11 TC16–TC18 TC21 |
| R7 | 원문 유지·과잉 출력 억제 | B03 B09; K12 | 핵심 / examples | TC14 TC15 TC16 |
| R8 | 환경 밖 재사용 가능 | B11; K11 | 핵심 경계 / 패키지·안내 | TC25 TC26 TC28 |
| R9 | 지정 양식의 목적/상태 보존 | B10; K03 K07 K09 K12 | documents / examples | TC20 TC21 TC23 TC24 |
