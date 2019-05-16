from contextlib import ExitStack
import heapq


def merge_sorted_files(inputs, result):
    with open(result, 'w') as result, ExitStack() as stack:
        files = [stack.enter_context(open(f)) for f in inputs]

        for line in heapq.merge(*files):
            result.write(line)


merge_sorted_files(['10GB.txt', '20GB.txt'], "merged.txt")
