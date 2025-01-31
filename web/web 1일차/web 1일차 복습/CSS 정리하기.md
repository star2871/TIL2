# CSS
## 1. CSS는 HTML이나 XML(XML의 방언인 SVG, XHTML 포함)로 작성된 문서의 표시 방법을 기술하기 위한 스타일 시트 언어이다. CSS는 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링되어야 하는지 지정한다.
## 2. CSS(Cascading Style Sheets)는 웹 페이지에 스타일과 레이아웃을 적용할 때 사용한다. 예시를 몇 가지 들자면 글꼴, 색상, 크기를 조절하고, 콘텐츠의 간격을 조정하고, 페이지를 여러개의 열로 나누고, 애니메이션 등 장식을 추가할 수도 있다. 이 모듈에서는 CSS의 기본적인 작동 원리와 구문의 생김새, HTML에 실제로 적용하는 법을 배우면서 다음 과정으로 가는 길을 닦는다.
## 3. CSS는 스타일을 지정하기 위한 언어를 선택하고, 스타일을 지정한다.
## 4. CSS 구문
![[CSS 구문.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/CSS%20%EA%B5%AC%EB%AC%B8.jpg)
- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
	- 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
	- 값 (Value) : 어떻게 스타일 기능을 변경할지 결정

## 5. CSS 정의 방법
- 인라인(inline)
![[CSS 인라인.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/CSS%20%EC%9D%B8%EB%9D%BC%EC%9D%B8.jpg)
- 내부 참조(embedding) - `<style>`
![[CSS 내부참조.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/CSS%20%EB%82%B4%EB%B6%80%EC%B0%B8%EC%A1%B0.jpg)
- 외부 참조(link file) – 분리된 CSS 파일
![[CSS 외부참조.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/CSS%20%EC%99%B8%EB%B6%80%EC%B0%B8%EC%A1%B0.jpg)
## 6. CSS with 개발자 도구
- styles : 해당 요소에 선언된 모든 CSS
![[CSS 개발자 도구 styles.jpg]]
- computed : 해당 요소에 최종 계산된 CSS
![[CSS 개발자 도구 computed.jpg]]
## 7. CSS 기초 선택자
- 요소 선택자
	- HTML 태그를 직접 선택
- 클래스(class) 선택자
	- 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
	- `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
	- 일반적으로 하나의 문서에 1번만 사용
	- 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장