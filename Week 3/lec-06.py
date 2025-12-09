# # # #####################################
# # # # EXAMPLE:  Towers of Hanoi
# # # #####################################
# # #
# # # def printMove(fr, to):
# # #     # '출발 기둥'과 '도착 기둥' 이름을 문자열로 변환하여 출력 (원반 이동을 기록)
# # #     print('move from ' + str(fr) + ' to ' + str(to))
# # #
# # #
# # # def Towers(n, fr, to, spare):
# # #     # n: 옮겨야 할 원반의 개수
# # #     # fr: 출발 기둥 (From)
# # #     # to: 도착 기둥 (To)
# # #     # spare: 보조 기둥
# # #     if n == 1: # 원반이 1개일 때: 그냥 출발지에서 도착지로 옮기면 끝!
# # #         printMove(fr, to)
# # #     else:
# # #         Towers(n - 1, fr, spare, to)
# # #
# # #         # Step A: n-1개의 원반을 출발(fr)에서 보조(spare) 기둥으로 옮김
# # #         # 이 호출은 'spare'를 임시 도착지로, 'to'를 임시 보조 기둥으로 사용함
# # #         # 컴퓨터는 이 시점에서 현재 함수 호출을 멈추고 메모리 스택에 저장한 후,
# # #         # Towers(n-1, ...)을 실행하기 위해 다시 처음부터 함수를 호출
# # #
# # #         Towers(1, fr, to, spare)
# # #
# # #         # Step B: 가장 큰 n번째 원반(1개)을 출발(fr)에서 도착(to) 기둥으로 옮김
# # #         # (이 단계는 n=1의 기본 조건을 실행하여 실제 이동을 출력)
# # #
# # #         Towers(n - 1, spare, to, fr)
# # #
# # #          # Step C: n-1개의 원반을 보조(spare)에서 도착(to) 기둥으로 옮김
# # #          # 이 호출은 'to'를 최종 도착지로, 'fr'을 임시 보조 기둥으로 사용함
# # #          # Step A와 마찬가지로, 다시 Towers(n-1, ...)을 실행하기 위해 재귀 호출
# # #
# # #
# # # print(Towers(4, 'P1', 'P2', 'P3') #최종 실행 명령: 원반 4개를 P1에서 P2로, P3를 보조 기둥으로 사용하여 옮겨라
# # #
# # # #####################################
# # # # EXAMPLE:  fibonacci
# # # #####################################
# # #
# #
# # # x = int(input('x = '))
# # #
# # # def fib(x):
# # #     """assumes x an int >= 0
# # #        returns Fibonacci of x"""
# # #     if x == 0 or x == 1:
# # #         return 1
# # #     else:
# # #         return fib(x - 1) + fib(x - 2)
# # #
# # # print(fib(x))
# #
# # ## x = 10000000000
# # #   =>  RecursionError: maximum recursion depth exceeded in comparison
# #
# #
# # #
# # #
# # # #####################################
# # # # EXAMPLE:  testing for palindromes
# # # #####################################
#

def isPalindrome(s):
    def toChars(s):
        s = s.lower() #대문자 -> 소문자
        ans = '' #변수 초기화
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c #changing binding
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


print(isPalindrome('eve'))

print(isPalindrome('Able was I, ere I saw Elba'))

print(isPalindrome('Is this a palindrome'))
#
# # # #####################################
# # # # EXAMPLE: using dictionaries
# # # #          counting frequencies of words in song lyrics
# # # #####################################
#
# def lyrics_to_frequencies(lyrics):
#     myDict = {}
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict
#
#
# she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
#                  'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#
#                  'you', 'think', "you've", 'lost', 'your', 'love',
#                  'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
#                  "it's", 'you', "she's", 'thinking', 'of',
#                  'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
#
#                  'she', 'says', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'she', 'said', 'you', 'hurt', 'her', 'so',
#                  'she', 'almost', 'lost', 'her', 'mind',
#                  'and', 'now', 'she', 'says', 'she', 'knows',
#                  "you're", 'not', 'the', 'hurting', 'kind',
#
#                  'she', 'says', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'you', 'know', "it's", 'up', 'to', 'you',
#                  'i', 'think', "it's", 'only', 'fair',
#                  'pride', 'can', 'hurt', 'you', 'too',
#                  'pologize', 'to', 'her',
#
#                  'Because', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'Yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'yeah', 'yeah', 'yeah',
#                  'yeah', 'yeah', 'yeah', 'yeah'
#                  ]
#
# beatles = lyrics_to_frequencies(she_loves_you)
#
#
# def most_common_words(freqs):
#     values = freqs.values()
#     best = max(freqs.values())
#     words = []
#     for k in freqs:
#         if freqs[k] == best:
#             words.append(k)
#     return (words, best)
#
#
# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         temp = most_common_words(freqs)
#         if temp[1] >= minTimes:
#             result.append(temp)
#             for w in temp[0]:
#                 del (freqs[w])  # remove word from dict
#         else:
#             done = True
#     return result
#
#
# # print(words_often(beatles, 5))
#
# # # #####################################
# # # # EXAMPLE: comparing fibonacci using memoization
# # # #####################################
# # #
# # #
# # # def fib(n):
# # #     if n == 1:
# # #         return 1
# # #     elif n == 2:
# # #         return 2
# # #     else:
# # #         return fib(n - 1) + fib(n - 2)
# # #
# # #
# # # def fib_efficient(n, d):
# # #     if n in d:
# # #         return d[n]
# # #     else:
# # #         ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
# # #         d[n] = ans
# # #         return ans
# # #
# # #
# # # d = {1: 1, 2: 2}
# # #
# # # argToUse = 34
# # # # print("")
# # # # print('using fib')
# # # # print(fib(argToUse))
# # # # print("")
# # # # print('using fib_efficient')
# # # # print(fib_efficient(argToUse, d))