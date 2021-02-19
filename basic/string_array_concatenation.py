import timeit

domain = 'some_really_long_example.com'
lang = 'en'
path = 'some/really/long/path/'
iterations = 100000


def meth_plus(n):
    '''Using + operator'''
    result = ""
    for i in range(n):
        result += 'a'
    return result


def meth_join(n):
    '''Using ''.join()'''
    arr = []
    for i in range(n):
        arr.append('a')
    return ''.join(arr)


def meth_form(n):
    '''Using string.format'''
    result = ''
    for i in range(n):
        result = '{0}{1}'.format(result, 'a')
    return result


def meth_intp(n):
    '''Using string interpolation'''
    result = ''
    for i in range(n):
        result = '%s%s' % (result, 'a')
    return result


def meth_advanced_form(n):
    '''Using f"{}"'''
    result = ''
    for i in range(n):
        result = f'{result}a'
    return result


n = 1000

plus = timeit.Timer(stmt=f"meth_plus({n})", setup="from __main__ import meth_plus")
join = timeit.Timer(stmt=f"meth_join({n})", setup="from __main__ import meth_join")
form = timeit.Timer(stmt=f"meth_form({n})", setup="from __main__ import meth_form")
intp = timeit.Timer(stmt=f"meth_intp({n})", setup="from __main__ import meth_intp")
adv_form = timeit.Timer(stmt=f"meth_advanced_form({n})", setup="from __main__ import meth_advanced_form")

plus.val = plus.timeit(iterations)
join.val = join.timeit(iterations)
form.val = form.timeit(iterations)
intp.val = intp.timeit(iterations)
adv_form.val = adv_form.timeit(iterations)

min_val = min([plus.val, join.val, form.val, intp.val, adv_form.val])

print('plus %0.12f (%0.2f%% as fast)' % (plus.val, (100 * min_val / plus.val),))
print('join %0.12f (%0.2f%% as fast)' % (join.val, (100 * min_val / join.val),))
print('form %0.12f (%0.2f%% as fast)' % (form.val, (100 * min_val / form.val),))
print('intp %0.12f (%0.2f%% as fast)' % (intp.val, (100 * min_val / intp.val),))
print('adv_form %0.12f (%0.2f%% as fast)' % (adv_form.val, (100 * min_val / adv_form.val),))
