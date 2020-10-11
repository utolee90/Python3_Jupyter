with open ('test.txt', 'w') as f :
           for i in range(1, 6):
               f.write(str(i) + '번째 줄입니다.\n')
    
with open ('test.txt', 'r') as f :
           print(f.read())