import collections
import sys

INF = float('inf')


class SegmentTree:
    def __init__(self, num_types, initial_leaf_values_pairs):
        self.m_types = num_types
        self.num_leaves_pow2 = 1
        while self.num_leaves_pow2 < self.m_types:
            self.num_leaves_pow2 *= 2
        self.tree = [(INF, -1)] * (2 * self.num_leaves_pow2)
        for type_idx in range(self.m_types):
            self.tree[self.num_leaves_pow2 +
                      type_idx] = initial_leaf_values_pairs[type_idx]
        for i in range(self.num_leaves_pow2 - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2 * i], self.tree[2 * i + 1])

    def _merge(self, left_child_pair, right_child_pair):
        if left_child_pair[0] <= right_child_pair[0]:
            return left_child_pair
        return right_child_pair

    def update(self, type_to_update, new_value_pair):
        pos = self.num_leaves_pow2 + type_to_update
        self.tree[pos] = new_value_pair
        while pos > 1:
            pos //= 2
            self.tree[pos] = self._merge(
                self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, query_L_type, query_R_type):
        if query_L_type > query_R_type or query_L_type >= self.m_types or query_R_type < 0:
            return (INF, -1)
        query_L_type = max(0, query_L_type)
        query_R_type = min(self.m_types - 1, query_R_type)
        if query_L_type > query_R_type:
            return (INF, -1)
        res_val_pair = (INF, -1)
        l_pos = self.num_leaves_pow2 + query_L_type
        r_pos = self.num_leaves_pow2 + query_R_type
        while l_pos <= r_pos:
            if l_pos % 2 == 1:
                res_val_pair = self._merge(res_val_pair, self.tree[l_pos])
                l_pos += 1
            if r_pos % 2 == 0:
                res_val_pair = self._merge(res_val_pair, self.tree[r_pos])
                r_pos -= 1
            l_pos //= 2
            r_pos //= 2
        return res_val_pair


def solve():
    n, m = map(int, input().split())
    items_by_type = [collections.deque() for _ in range(m)]
    for original_idx in range(n):
        item_type = int(input())
        if 0 <= item_type < m:
            items_by_type[item_type].append(original_idx)
    initial_st_leaf_values = []
    for type_idx in range(m):
        if items_by_type[type_idx]:
            initial_st_leaf_values.append(
                (items_by_type[type_idx][0], type_idx))
        else:
            initial_st_leaf_values.append((INF, type_idx))
    seg_tree = SegmentTree(m, initial_st_leaf_values)
    result_indices = []
    last_selected_type = -1
    for _ in range(n):
        current_best_val_pair = (INF, -1)
        if last_selected_type == -1:
            current_best_val_pair = seg_tree.query(0, m - 1)
        else:
            res_part1 = seg_tree.query(0, last_selected_type - 1)
            res_part2 = seg_tree.query(last_selected_type + 1, m - 1)
            current_best_val_pair = seg_tree._merge(res_part1, res_part2)
        chosen_original_idx, chosen_type = current_best_val_pair
        if chosen_original_idx == INF:
            break
        result_indices.append(chosen_original_idx)
        last_selected_type = chosen_type
        items_by_type[chosen_type].popleft()
        if items_by_type[chosen_type]:
            new_val_for_type = items_by_type[chosen_type][0]
            seg_tree.update(chosen_type, (new_val_for_type, chosen_type))
        else:
            seg_tree.update(chosen_type, (INF, chosen_type))
    print(" ".join(map(str, result_indices)))


if __name__ == '__main__':
    solve()
