# chapter 1-1
# Problem

# You have an N-element tuple or sequence that you would like to unpack into a collection
# of N variables.
def unpacking_a_sequence_into_separate_variables():
    p = (4, 5)
    x, y = p
    print(x)

    data = ['ACME', 50, 91.1, (2020, 1, 14)]
    name, shares, price, date = data   
    print(date)

    s = 'Hello'
    a, b, c, d, e = s
    print(a,b,c)
    
    _, shares, price, _ = data
    # (언더바)를 사용하여 해당 순서 데이터 생략가능
    print(shares, price)

#chapter1-2
def unpacking_elements_from_iterables_of_arbitrary_length():
    record = ['anjoy', 'anhs0220@gmail.com', '010-7777-7777', '010-3333-3333']
    name, email, *phone_number = record 
    # *(별표)를 이용하면 여러개의 데이터 삽입가능 
    print(phone_number)

    star_expression = [1,2,3,4,5,6]
    *a, b = star_expression

    print(b)

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')

    print(fields)

    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record # _, * 혼용가능

    print(name, year)

    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    def do_foo(x, y):
        print('foo', x, y)
    
    def do_bar(s):
        print('bar', s)

    for tag, *arg in records:
        if tag == 'foo':
            do_foo(*arg) 
        elif tag == 'bar':
            do_bar(*arg)

    items = [1, 10, 7, 4, 5, 9]
    def sum(items):
        head, *tail = items
        return head + sum(tail) if tail else head # why use if sentence ? 재귀함수로 마지막 함수 수행에서 head만 있기 떄문에 tail이 없는 경우 head만 return 해줘야 하기 떄문
        # 사용자 정의 sum 함수를 재귀하여 전체 덧셈을 return 해줌

        # must remember ! 
        # if data = [1,2,3,4]
        # print(data) => [1,2,3,4]
        # print(*data) => 1 2 3 4
        # 무슨차이 ? data는 list형태로 반환 , *data는 각각 변수로 반환해주기 떄문에 함수를 사용할 때 넣어야 하는 변수 개수에 따라 사용을 주의할 것 !

    print(sum(items))

# chapter1-3
# Problem
# You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing.
def keeping_the_last_N_items():
    from collections import deque

    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

# chapter1-4

# Problem
# You want to make a list of the largest or smallest N items in a collection.

def finding_the_largest_or_smallest_N_items():
    import heapq

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

    print('cheap list')
    for ch in cheap:
        print(ch)
    print('-'*20)
    print('expensive list')
    for exp in expensive:
        print(exp)
    print('-'*20)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)

    # --------------------
    # 숙제 : 이해해오기
    # --------------------


finding_the_largest_or_smallest_N_items()