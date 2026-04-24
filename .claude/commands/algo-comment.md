입력에서 날짜·문제명·코멘트를 파싱하고, 해당 HTML의 problem-item 하단에 코멘트 블록을 추가해줘.

## 입력

$ARGUMENTS

입력 형식:

```
날짜: YY-MM-DD
문제: 문제이름
코멘트: 내용 (여러 줄도 가능)
```

---

## 처리 순서

### STEP 1 — 파일·위치 파악

- HTML 파일: `YYYYMM.html` (예: `26-04-24` → `202604.html`)
- day id: `MMDD` (예: `0424`)
- 표시용 날짜: `MM.DD` (예: `04.24`)

### STEP 2 — problem-item 찾기

HTML 파일을 읽고 아래 순서로 타깃을 찾는다:

1. `<!-- ===== MMDD =====` 주석으로 해당 날짜 day-entry 진입
2. 그 안에서 `<span class="problem-name">문제명</span>` 이 일치하는 problem-item 탐색
3. 해당 problem-item의 닫는 `</div>` 바로 앞을 삽입 위치로 결정

### STEP 3 — 코멘트 블록 삽입

찾은 problem-item의 마지막 `</div>` 직전에 아래 블록을 추가한다:

```html
        <div class="comment">
          <div class="comment-meta">💬 MM.DD</div>
          <p>코멘트 내용</p>
        </div>
```

여러 줄 코멘트는 `<p>` 태그 안에서 `<br>` 로 연결한다.

### STEP 4 — CSS 확인

HTML `<style>` 블록에 `.comment` 스타일이 없으면 `/* Note */` 섹션 바로 아래에 추가한다:

```css
    /* Comment */
    .comment {
      margin-top: 10px;
      font-size: 13px;
      color: var(--muted);
      line-height: 1.75;
      padding: 8px 12px;
      background: #fffdf0;
      border-left: 2px solid #f6c56a;
      border-radius: 0 6px 6px 0;
    }
    .comment-meta {
      font-size: 11px;
      color: #a0aec0;
      margin-bottom: 3px;
      font-family: 'JetBrains Mono', monospace;
    }
```

---

## 최종 출력

```
✅ YYYYMM.html — MMDD "문제명" 에 코멘트 추가
```
