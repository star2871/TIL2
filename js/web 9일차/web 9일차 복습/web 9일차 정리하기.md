# JavaScript의 필요성
## 브라우저 화면을 '동적'으로 만들기 위함
## 브라우저를 조작할 수 있는 유일한 언어

## JavaScript ES6+
### 2015년 ES2015 (ES6) 탄생
- “Next-gen of JS” 
- JavaScript의 고질적인 문제들을 해결 
- JavaScript의 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이한 버전 
- 이때부터 버전 순서가 아닌 출시 연도를 붙이는 것이 공식 명칭이나 통상적으로 ES6라 부름 
- 현재는 표준 대부분이 ES6+로 넘어옴

## Vanilla JavaScript
- 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장 (jQuery 등)
- ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용의 증대

## JavaScript 실행 순서
```
<script>
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
</script>
```

## 문법과 자료형
```
var 갑을 = "병정";
var Früh = "foobar";
```
### JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용합니다. 예를 들면, Früh(독일어로 "이른")을 변수명으로 사용할 수도 있습니다.
### 하지만 `Früh`는 `früh`와 다릅니다. 대소문자를 구분하기 때문입니다.
### 주석
```
// 한 줄 주석

/* 이건 더 긴,
 * 여러 줄 주석입니다.
 */

/* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */
```

## 선언
### JavaScript의 선언에는 3가지 방법이 있습니다.
#### var
- 변수를 선언. 추가로 동시에 값을 초기화
```
var x = 42
```
- 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있습니다.
#### let
- 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화
- 선언한 변수는 재선언이 불가능하고 재할당이 가능하다.
#### const
- 블록 스코프 읽기 전용 상수를 선언
- 선언한 변수는 재선언이 불가능하고 재할당이 불가능하다.
```
let y = 13
```
이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다. 아래 변수 스코프를 참고하세요.
## DOM
### 브라우저에서 할 수 있는 일
- DOM 조작
	- 문서(HTML)조작
- BOM 조작
	- navigator, screen, location, frames, history, XHR
- JavaScript Core (ECMAScript)
	- Data Structure(Object, Array), Conditional Expression, Iteration

## DOM 이란?
### HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스 
### 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델 
### 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급 
### 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
### 주요 객체
- window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능) 
- document : 페이지 컨텐츠의 Entry Point 역할을 하며, 등과 같은 수많은 다른 요소들을 포함
- navigator, location, history, screen

## DOM - 해석
### 파싱 (Parsing)
- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

## BOM 이란?
### Browser Object Model 
### 자바스크립트가 브라우저와 소통하기 위한 모델 
### 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단 
- 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능 
### window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

## DOM 조작 - 개념
### Document는 문서 한 장(HTML)에 해당하고 이를 조작
### DOM 조작 순서
#### 1. 선택 (Select)
#### 2. 변경 (Manipulation)

## DOM 객체의 상속 구조
### EventTarget 
- Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
### Node
- 여러 가지 DOM 타입들이 상속하는 인터페이스

![[Event Target Node.jpg]](https://github.com/star2871/TIL/blob/master/js/web%209%EC%9D%BC%EC%B0%A8/web%209%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%9E%90%EB%A3%8C/Event%20Target%20Node.jpg)

### Element
- Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스 
- 부모인 Node와 그 부모인 EventTarget의 속성을 상속
### Document 
- 브라우저가 불러온 웹 페이지를 나타냄 
- DOM 트리의 진입점(entry point) 역할을 수행 
### HTMLElement 
- 모든 종류의 HTML 요소 
- 부모 element의 속성 상속

![[Event Target Node 1.jpg]](https://github.com/star2871/TIL/blob/master/js/web%209%EC%9D%BC%EC%B0%A8/web%209%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%9E%90%EB%A3%8C/Element%20Document%20HTML.jpg)

## DOM 선택 – 선택 관련 메서드

### document.querySelector(selector) 
- 제공한 선택자와 일치하는 element 하나 선택 
- 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)

### document.querySelectorAll(selector) 
- 제공한 선택자와 일치하는 여러 element를 선택 
- 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음 
- 지정된 셀렉터에 일치하는 NodeList를 반환

### getElementById(id) 
### getElementsByTagName(name) 
### getElementsByClassName(names) 
### querySelector(), querySelectorAll()을 사용하는 이유 
- id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능 ex) document.querySelector('#id’), document.querySelectAll(‘.class')

## DOM 선택 - 선택 메서드별 반환 타입
### 1. 단일 element
- getElementById() 
- querySelector()
### 2. HTMLCollection
- getElementsByTagName() 
- getElementsByClassName()
### 3. NodeList 
- querySelectorAll()

## DOM 선택 - HTMLCollection & NodeList
### 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열) 
### HTMLCollection
- name, id, index 속성으로 각 항목에 접근 가능
### NodeList
- index로만 각 항목에 접근 가능 
- 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
### 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음

## DOM 선택 - Collection
### Live Collection
- 문서가 바뀔 때 실시간으로 업데이트 됨 
- DOM의 변경사항을 실시간으로 collection에 반영 
- ex) HTMLCollection, NodeList
### Static Collection (non-live) 
- DOM이 변경되어도 collection 내용에는 영향을 주지 않음 
- querySelectorAll()의 반환 NodeList만 static collection

## DOM 변경 - 변경 관련 메서드 (Creation)
### document.createElement() 
- 작성한 태그 명의 HTML 요소를 생성하여 반환

## DOM 변경 - 변경 관련 메서드 (append DOM)
### Element.append() 
- 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입 
- 여러 개의 Node 객체, DOMString을 추가 할 수 있음 
- 반환 값이 없음
### Node.appendChild()
- 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능) 
- 한번에 오직 하나의 Node만 추가할 수 있음 
- 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

## ParentNode.append() vs Node.appendChild()
- append()를 사용하면 DOMString 객체를 추가할 수도 있지만, 
	.appendChild()는 Node 객체만 허용
- append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체를 반환
- append()는 여러 Node 객체와 문자열을 추가할 수 있지만, 
	.appendChild()는 하나의 Node 객체만 추가할 수 있음

## DOM 변경 – 변경 관련 속성 (property)
### Node.innerText
- Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
- 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
### Element.innerHTML
- 요소(element) 내에 포함된 HTML 마크업을 반환 
- [참고] XSS 공격에 취약하므로 사용 시 주의

## XSS (Cross-site Scripting)
- 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입 해 공격하는 방법
- 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함

## DOM 삭제 - 삭제 관련 메서드
### ChildNode.remove()
- Node가 속한 트리에서 해당 Node를 제거
### Node.removeChild()
- DOM에서 자식 Node를 제거하고 제거된 Node를 반환 
- Node는 인자로 들어가는 자식 Node의 부모 Node

## DOM 속성 – 속성 관련 메서드
### Element.setAttribute(name, value)
- 지정된 요소의 값을 설정 
- 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
### Element.getAttribute(attributeName)
- 해당 요소의 지정된 값(문자열)을 반환 
- 인자(attributeName)는 값을 얻고자 하는 속성의 이름

## DOM 조작 - 정리

![[DOM 조작 정리.jpg]](https://github.com/star2871/TIL/blob/master/js/web%209%EC%9D%BC%EC%B0%A8/web%209%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%9E%90%EB%A3%8C/DOM%20%EC%A1%B0%EC%9E%91%20%EC%A0%95%EB%A6%AC.jpg)
