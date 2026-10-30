
'''

파이썬 정렬과 검색


    오늘 배운 내용

정렬과 검색은 리스트에 저장된 데이터를 원하는 순서로
정리하거나 특정 데이터를 찾을 때 사용하는 기능이다.

예를 들어 학생들의 점수를 높은 순서대로 정리하거나
리스트에서 특정 학생의 점수가 있는지 확인할 수 있다.

파이썬에서는 sort(), sorted(), in 등의 기능을
활용하여 데이터를 정렬하고 검색할 수 있다.



    정렬과 검색의 정의


1) 정렬(Sorting)

데이터를 일정한 기준에 따라 순서대로 나열하는 것이다.

예를 들어 숫자를 작은 순서대로 정렬하거나
문자열을 알파벳 순서대로 정렬할 수 있다.

2) 검색(Searching)

여러 데이터 중에서 원하는 값이 있는지 확인하거나
특정 데이터의 위치를 찾는 것이다.

3) sort()

리스트 자체의 순서를 변경하는 메서드이다.
기본적으로 오름차순으로 정렬한다.

4) sorted()

리스트의 원본은 유지하면서 정렬된 새로운 리스트를 반환하는 함수이다.

5) reverse

정렬 순서를 반대로 바꾸는 옵션이다.
sort()와 sorted()에서 reverse=True를 사용하면
내림차순으로 정렬할 수 있다.

6) in

리스트나 문자열 등에 특정 값이 포함되어 있는지 확인한다.
결과는 True 또는 False로 반환된다.

7) index()

리스트에서 특정 값이 처음 등장하는 위치를 반환한다.
해당 값이 없으면 ValueError가 발생한다.



    sort()로 정렬하기

numbers = [5, 2, 8, 1, 9]

numbers.sort()

print(numbers)

실행 결과:
[1, 2, 5, 8, 9]

sort()는 기존 리스트의 순서를 직접 변경한다.



    sorted()로 정렬하기


numbers = [5, 2, 8, 1, 9]

result = sorted(numbers)

print("원본 리스트:", numbers)
print("정렬된 리스트:", result)

실행 결과:
원본 리스트: [5, 2, 8, 1, 9]
정렬된 리스트: [1, 2, 5, 8, 9]

sorted()는 정렬된 새로운 리스트를 반환하기 때문에
원본 리스트의 순서는 그대로 유지된다.



    내림차순으로 정렬하기

numbers = [5, 2, 8, 1, 9]

numbers.sort(reverse=True)

print(numbers)

실행 결과:
[9, 8, 5, 2, 1]

reverse=True를 사용하면 큰 값부터 작은 값 순서로 정렬된다.

sorted()에서도 같은 방법을 사용할 수 있다.

numbers = [5, 2, 8, 1, 9]

result = sorted(numbers, reverse=True)

print(result)



    in으로 데이터 검색하기


students = ["민수", "지훈", "서연", "지우"]

print("지훈" in students)
print("철수" in students)

실행 결과:
True
False

in은 특정 값이 리스트 안에 존재하는지 확인한다.

값이 있으면 True, 없으면 False를 반환한다.



    index()로 위치 찾기


students = ["민수", "지훈", "서연", "지우"]

position = students.index("서연")

print("서연의 위치:", position)

실행 결과:
서연의 위치: 2

리스트의 위치는 0부터 시작한다.
따라서 서연은 세 번째 항목이지만 위치는 2이다.



    정렬과 검색을 활용한 학생 점수 관리


students = [
    ["민수", 85],
    ["지훈", 92],
    ["서연", 78],
    ["지우", 96]
]

print("전체 학생 목록:")

for student in students:
    print(student[0], student[1])

print("점수 기준 내림차순 정렬:")

sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

for student in sorted_students:
    print(student[0], student[1])

print("학생 검색:")

search_name = input("검색할 학생 이름: ")

found = False

for student in students:
    if student[0] == search_name:
        print("검색 결과:", student[0], student[1])
        found = True
        break

if not found:
    print("해당 학생을 찾을 수 없습니다.")



    코드 분석


sorted(students, key=lambda student: student[1], reverse=True)

- students에 저장된 학생 정보를 정렬한다.
- key는 어떤 값을 기준으로 정렬할지 지정한다.
- lambda student: student[1]은 각 학생 정보에서
  두 번째 값인 점수를 기준으로 정렬한다.
- reverse=True는 점수가 높은 순서대로 정렬한다.

for student in students:

- 리스트에 있는 학생 정보를 하나씩 가져온다.

if student[0] == search_name:

- 학생 이름과 입력한 이름이 같은지 비교한다.

found = True

- 검색할 학생을 찾았다는 것을 표시한다.

break

- 원하는 학생을 찾았으므로 반복문을 종료한다.

if not found:

- 학생을 찾지 못했을 때 안내 문장을 출력한다.



    복습하면서 알게 된 점


1) sort()는 기존 리스트의 순서를 직접 변경한다.

2) sorted()는 원본 리스트를 유지하면서
   정렬된 새로운 리스트를 반환한다.

3) reverse=True를 사용하면 내림차순으로 정렬할 수 있다.

4) in은 특정 데이터가 존재하는지 확인할 때 사용한다.

5) index()는 특정 값이 리스트에서 몇 번째 위치에 있는지
   확인할 때 사용한다. 위치는 0부터 시작한다.

6) key를 사용하면 원하는 기준으로 데이터를 정렬할 수 있다.

7) 정렬과 검색을 함께 사용하면 학생 관리와 같은
   데이터 관리 프로그램을 만들 수 있다.


========================================
📌 11. AI 활용 복습 문제
========================================

1) 리스트 자체의 순서를 변경하면서 정렬하는 메서드는?
1. sorted()   2. sort()   3. index()   4. in

정답: 2번 (sort())


2) 원본 리스트를 유지하면서 정렬된 새로운 리스트를
만드는 함수는?
1. sort()   2. index()   3. sorted()   4. reverse()

정답: 3번 (sorted())


3) 숫자를 큰 순서대로 정렬하려면 어떤 옵션을 사용할까?
1. reverse=True
2. reverse=False
3. sort=False
4. order=True

정답: 1번 (reverse=True)


4) 특정 값이 리스트에 존재하는지 확인하는 연산자는?
1. index   2. sort   3. in   4. return

정답: 3번 (in)


5) 리스트에서 특정 값의 위치를 찾는 메서드는?
1. append()   2. index()   3. sort()   4. remove()

정답: 2번 (index())


6) 다음 코드의 실행 결과는?

numbers = [3, 1, 2]
result = sorted(numbers)

print(numbers)

1. [1, 2, 3]
2. [3, 1, 2]
3. [2, 1, 3]
4. 오류 발생

정답: 2번 ([3, 1, 2])


7) 리스트에서 "민수"가 존재하는지 확인하는 올바른 코드는?
1. "민수" == students
2. students.sort("민수")
3. "민수" in students
4. students.sorted("민수")

정답: 3번 ("민수" in students)


8) 리스트에서 index()로 찾으려는 값이 존재하지 않으면?
1. 0을 반환한다.
2. False를 반환한다.
3. None을 반환한다.
4. ValueError가 발생한다.

정답: 4번 (ValueError)
'''
