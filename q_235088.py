# https://quera.org/problemset/235088
n = int(input())
l, r = map(int, input().split())

# حداقل تعداد روز ممکن
days = (n + r - 1) // r

# بررسی اینکه آیا می‌توان دقیقاً n ساعت را در این تعداد روز تقسیم کرد
if days * l <= n <= days * r:
    print(days)
else:
    print(-1)
