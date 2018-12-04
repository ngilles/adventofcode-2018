
from collections import defaultdict
from parse import parse
from pprint import pprint
from functools import reduce
from itertools import groupby, chain
from operator import itemgetter as IG

input_txt = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''

input_txt = open('input.txt', 'r').read()

def print_routine(routine):
    for day, guard, sleep in routine:
        print(day, guard, ''.join('#' if s else '.' for s in sleep))

def guard_events(events):
    guard = None
    routine = []
    for event in events:
        if event[5][0] == 'G': # New guard
            if guard:
                routine.append((day, guard, sleep))

            guard = parse('Guard #{:d} begins shift', event[5])[0]
            sleep = [0] * 60

        elif event[5][0] == 'f': # Falls asleep

            day = event[1:3]
            sleep_start = event[4]

        elif event[5][0] == 'w': # wakes up
            sleep[sleep_start:event[4]] = [1] * (event[4] - sleep_start)
            
    routine.append((day, guard, sleep))

    return routine

def guard_max_sleep(routine):
    cumul_sleep = []
    for key, group in groupby(sorted(routine, key=IG(1)), key=IG(1)):
        guard_total = sum(sum(g[2]) for g in group)
        cumul_sleep.append((key, guard_total))
        print(key, guard_total)
    cumul_sleep.sort(key=IG(1), reverse=True)
    return cumul_sleep[0][0]

def guard_sleep_avg(routine, guard):
    guard_routine = [e for e in routine if e[1] == guard]
    print(guard_routine)
    totals = reduce(lambda a, b: [a+b for a, b in zip(a,b)], (d[2] for d in guard_routine))
    print(totals)
    index, value = max(enumerate(totals), key=IG(1))
    print(index, value)
    return index, value

def guard_sleep_avg_all(routine):
    guard_sleeps = defaultdict(lambda: [0] * 60)
    
    for day, guard, sleep in routine:
        guard_sleeps[guard] = [a + b for a, b  in zip(guard_sleeps[guard], sleep)]

    return guard_sleeps


raw_events = sorted(tuple(parse("[{:d}-{:d}-{:d} {:d}:{:d}] {}", l)) for l in input_txt.split('\n'))

routine = guard_events(raw_events)
print_routine(routine)
guard = guard_max_sleep(routine)
print(guard)
guard_sleeps = guard_sleep_avg_all(routine)
index, value = max(enumerate(guard_sleeps[guard]), key=IG(1))
print(index * guard)

guard, gs = max(((guard, max(enumerate(sleeps), key=IG(1))) for guard, sleeps in guard_sleeps.items()), key=lambda v: v[1][1])
print(guard, gs)
print(guard * gs[0])
#pprint(raw_events)