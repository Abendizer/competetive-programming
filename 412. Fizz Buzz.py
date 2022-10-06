class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            outPut=""
            if i%3==0:
                outPut+="Fizz"
            if i%5==0:
                outPut+="Buzz"
            if len(outPut)<4:
                outPut=str(i)
            answer.append(outPut)
        return answer
