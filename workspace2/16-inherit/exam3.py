# 여러 클래스의 공통 내용을 부모 클래스에 만들고,
# 상속 받아서 사용
class Article :
    def __init__(self) :
        self.num = 0   # 글 번호
        self.title = 0 # 글 제목

# 파일 관리        
class FileArticle(Article) :
    def __init__(self) :
        self.fileName = 0   # 파일 이름
    def __str__(self) :
        return '자료실 [번호=%s, 제목=%s, 첨부파일=%s]'\
            %(self.num, self.title, self.fileName)


# QNA 관리
class QNAArticle(Article) :
    def __init__(self) :
        self.answer = 0   # 답변
    def __str__(self) :
        return '질문/답변 [번호=%s, 제목=%s, 첨부파일=%s]'\
            %(self.num, self.title, self.answer)

file = FileArticle()
file.num = 1
file.title = '첫 번째 자료 입니다.'
file.fileName = 'python.ppt'
print(file)

qna = QNAArticle()
qna.num = 1
qna.title = '첫 번째 질문 입니다.'
qna.answer = '첫 번째 답변 입니다.'
print(qna)