# import tracemalloc

# tracemalloc.start()


# class Solution:
#     def lastInteger(self, n: int) -> int:
#         arr=list(range(1,n+1))
#         for i in range(int(n**0.5)+1):
#             if len(arr)==1:
#                 return arr[0]
#             if i%2==0:
#                 arr=arr[::2]
#             else:
#                 arr=(arr[::-2])[::-1]
#         return arr[0]
# print(Solution().lastInteger(23503313))

# current, peak = tracemalloc.get_traced_memory()
# print(f"Current: {current / 1024 / 1024:.2f} MB")
# print(f"Peak: {peak / 1024 / 1024:.2f} MB")

# tracemalloc.stop()
n=5
with open("output.txt","a")as file:
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    for e in range(n):
                        for f in range(n):
                            for g in range(n):
                                for h in range(n):
                                    for i in range(n):
                                        for j in range(n):
                                            t=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)
                                            file.write(t+"\n")