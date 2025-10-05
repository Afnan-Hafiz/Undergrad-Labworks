n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

def pre_order(in_order, post_order):
    if not in_order:
        return []

    root = post_order[-1]
    root_idx = in_order.index(root)

    left_subtree = pre_order(in_order[:root_idx], post_order[:root_idx])
    right_subtree = pre_order(in_order[root_idx+1:], post_order[root_idx:-1])

    return [root] + left_subtree + right_subtree

print(*pre_order(in_order, post_order))
