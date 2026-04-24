입력에서 날짜·문제명·설명·코드를 파싱하고, 5단계 리뷰를 수행한 뒤 MD 저장과 HTML 반영까지 자동으로 처리해줘.

## 입력

$ARGUMENTS

입력 형식은 아래를 따른다:

```
날짜: YY-MM-DD
문제: 문제이름
설명: 한두 줄 설명 (제약 조건 포함해도 됨)
코드:
def solution(...):
    ...
```

---

## STEP 1 — 파일·날짜 파악

날짜 `YY-MM-DD` 에서:
- HTML 파일명: `YYYYMM.html` (예: `26-04-25` → `202604.html`)
- day id: `MMDD` (예: `0425`)
- 요일: 해당 날짜를 계산해서 한국어 한 글자 (월/화/수/목/금/토/일)

---

## STEP 2 — 5단계 리뷰 수행

각 단계: 문제 없으면 "✅ 이상 없음", 있으면 구체적 지적 + 개선 코드 제시. 마지막 한 줄 총평.

### 01 정확성
- 엣지케이스 (빈값, 최솟값, 최댓값, 음수, 0) 처리 여부
- 인덱스 범위 초과 여부
- 문제의 제약조건이 코드에 반영됐는가

### 02 시간복잡도
- 빅오 명시
- 중첩 루프가 있으면 O(n²) 이상인지 확인
- 리스트 `in` / `remove` / `insert` 를 `set` / `dict` 으로 개선 가능한가
- 완전탐색 → BFS/DFS → DP 로 낮출 수 있는가

### 03 공간복잡도
- 불필요한 리스트/딕셔너리 복사 여부
- 재귀라면 최대 깊이 안전 여부 (파이썬 기본 1000)

### 04 코드 품질
- 변수명이 의도를 설명하는가 (`a`, `tmp` → `count`, `current_sum`)
- 중복 로직을 함수로 분리 가능한가
- 조건문 중첩 3단계 이상 여부

### 05 보안 관점 (선택)
- 외부 입력 크기 제한 여부
- 정규표현식 ReDoS 위험 패턴 여부
- 민감값 직접 `==` 비교 여부

---

## STEP 3 — MD 저장

`reviews/YYYYMM-문제명.md` 파일에 5단계 리뷰 내용을 마크다운으로 저장한다.

---

## STEP 4 — HTML 반영

`YYYYMM.html` 을 읽고 아래 규칙으로 내용을 삽입한다.

### 날짜 섹션이 이미 있는 경우

`<!-- ===== MMDD =====` 주석이 파일 안에 있으면,
해당 day-entry 안 `<div class="problem-list">` 의 마지막 `</div>` 바로 앞에 `problem-item` 블록을 추가한다.

### 날짜 섹션이 없는 경우

`<!-- ===== 다음 날 추가 예시` 주석 바로 앞에 아래 블록을 삽입한다:

```html
  <hr class="day-divider">

  <!-- ===== MMDD ===== -->
  <div class="day-entry">
    <div class="day-header">
      <span class="day-date">MMDD</span>
      <span class="day-weekday">요일</span>
    </div>
    <div class="problem-list">

      (problem-item 블록)

    </div>
  </div>
```

### problem-item 블록 구조

```html
      <div class="problem-item">
        <div class="problem-title-row">
          <span class="status">✅</span>
          <span class="problem-source">pyalgo</span>
          <span class="problem-name">문제명</span>
        </div>
        <div class="note">설명</div>
        <div class="code-wrap">
          <pre><code class="language-python">코드 (들여쓰기 유지)</code></pre>
          <details class="review-details">
            <summary>🔍 리뷰 보기</summary>
            <div class="review-panel">

              <div class="review-section">
                <h4>01 정확성</h4>
                <p class="review-ok 또는 review-warn">결과 한 줄</p>
                <p class="review-body">상세 설명 (인라인 코드는 &lt;code&gt; 태그 사용)</p>
                <!-- 개선 코드가 있으면 -->
                <div class="review-code"><pre><code class="language-python">개선 코드</code></pre></div>
              </div>

              <!-- 02~05도 동일 구조 반복 -->

              <div class="review-verdict">
                <strong>총평:</strong> 총평 내용
              </div>

            </div>
          </details>
        </div>
      </div>
```

`review-ok` 클래스는 ✅ 결과, `review-warn` 클래스는 ⚠️ 결과에 사용한다.
개선 코드가 없는 섹션은 `review-code` 블록을 생략한다.

### HTML 파일이 아예 없는 경우

`202604.html` 을 기준 템플릿으로 복사 후 월 헤더(h1, .sub)와 기존 day-entry를 새 달에 맞게 수정하고, problem-item을 삽입한다.

---

## 최종 출력

작업 완료 후 아래 형식으로 한 줄씩 보고한다:

```
✅ reviews/YYYYMM-문제명.md 저장
✅ YYYYMM.html — MMDD 섹션에 "문제명" 추가
```
