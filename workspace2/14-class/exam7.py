class Score :
    def set(self) :
        print(self)
        self.num = input('학번 : ')
        self.name = input('이름 : ')
        self.kor = int(input('국어 : '))
        self.eng = int(input('영어 : '))
        self.mat = int(input('수학 : '))
        self.tot = self.kor + self.eng + self.mat
        self.avg = self.tot / 3
        
    def output_title(self) :
        print(self)
        print('** 성적 출력 **')
        print('%4s %6s %4s %4s %4s %4s %4s'
              %('학번', '이름', '국어', '영어', '수학', '총점', '평균'))
        
    def output(self) :
        print(self)
        print('%4s %6s %4s %4s %4s %4s %1.1f'
              %(self.num, self.name, self.kor, self.eng, self.mat, self.tot, self.avg, ))
        
s1 = Score()
s2 = Score()
print('s1 : ', s1)
print('s2 : ', s2)
print('-' * 30)

s1.set()
s2.set()
s1.output_title()
s1.output()
s2.output()