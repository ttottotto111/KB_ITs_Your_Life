#부모클래스
class Person:
    def __init__(self, no, name):
        self.no = no
        self.name = name
    def __str__(self):
        return f"{self.no}-{self.name}"

#학생클래스
class Student(Person):
    def __init__(self, no, name, major):
        super().__init__(no,name)
        self.major = major      
        #부모와 중복되는 함수 제거 => 부모의 함수를 호출
    def __str__(self):
        return super().__str__()+f"-{self.major}"
    
#직원클래스
class Emp(Person):
    def __init__(self, no, name, dept):
        super().__init__(no, name)
        self.dept = dept
    def __str__(self):
        return super().__str__()+f"-{self.dept}"

#__name__ => 모듈명 출력
#__name__값이 __main__인 경우에만 테스트 코드 실행, 그외엔 비활성
if __name__ == "__main__":#메인상황일때 테스트 코드 활성화
    print("person.__name__", __name__)
