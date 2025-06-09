#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <climits>

void setup_fast_io() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
}

const int INF_IDX = INT_MAX;
const int NO_TYPE = -1;

struct SegTreeNode {
    int min_orig_idx;
    int type_idx;

    SegTreeNode() : min_orig_idx(INF_IDX), type_idx(NO_TYPE) {}
    SegTreeNode(int idx, int type) : min_orig_idx(idx), type_idx(type) {}
};

SegTreeNode merge_nodes(const SegTreeNode& left, const SegTreeNode& right) {
    if (left.min_orig_idx <= right.min_orig_idx) {
        return left;
    }
    return right;
}

class SegmentTree {
public:
    int num_actual_types;
    int tree_leaf_start_idx;
    std::vector<SegTreeNode> tree;

    SegmentTree(int m, const std::vector<SegTreeNode>& initial_leaf_values)
        : num_actual_types(m) {
        
        tree_leaf_start_idx = 1;
        while (tree_leaf_start_idx < num_actual_types) {
            tree_leaf_start_idx *= 2;
        }
        tree.resize(2 * tree_leaf_start_idx);

        for (int i = 0; i < num_actual_types; ++i) {
            tree[tree_leaf_start_idx + i] = initial_leaf_values[i];
        }

        for (int i = tree_leaf_start_idx - 1; i >= 1; --i) {
            tree[i] = merge_nodes(tree[2 * i], tree[2 * i + 1]);
        }
    }

    void update(int type_to_update, const SegTreeNode& new_node_val) {
        int pos = tree_leaf_start_idx + type_to_update;
        tree[pos] = new_node_val;
        
        while (pos > 1) {
            pos /= 2;
            tree[pos] = merge_nodes(tree[2 * pos], tree[2 * pos + 1]);
        }
    }

    SegTreeNode query(int query_L_type, int query_R_type) {
        if (query_L_type > query_R_type) {
            return SegTreeNode(INF_IDX, NO_TYPE);
        }
        
        query_L_type = std::max(0, query_L_type);
        query_R_type = std::min(num_actual_types - 1, query_R_type);

        if (query_L_type > query_R_type) {
            return SegTreeNode(INF_IDX, NO_TYPE);
        }

        SegTreeNode result(INF_IDX, NO_TYPE);
        
        int l_node = tree_leaf_start_idx + query_L_type;
        int r_node = tree_leaf_start_idx + query_R_type;

        for (; l_node <= r_node; l_node /= 2, r_node /= 2) {
            if (l_node % 2 == 1) {
                result = merge_nodes(result, tree[l_node]);
                l_node++;
            }
            if (r_node % 2 == 0) {
                result = merge_nodes(result, tree[r_node]);
                r_node--;
            }
        }
        return result;
    }
};

int main() {
    setup_fast_io();

    int n_items, m_types;
    std::cin >> n_items >> m_types;

    if (n_items == 0) {
        std::cout << std::endl;
        return 0;
    }

    std::vector<std::deque<int> > items_by_type(m_types);
    for (int i = 0; i < n_items; ++i) {
        int item_type;
        std::cin >> item_type;
        items_by_type[item_type].push_back(i);
    }

    std::vector<SegTreeNode> initial_segment_tree_leaves(m_types);
    for (int type_idx = 0; type_idx < m_types; ++type_idx) {
        if (!items_by_type[type_idx].empty()) {
            initial_segment_tree_leaves[type_idx] = SegTreeNode(items_by_type[type_idx].front(), type_idx);
        } else {
            initial_segment_tree_leaves[type_idx] = SegTreeNode(INF_IDX, type_idx);
        }
    }
    
    SegmentTree seg_tree(m_types, initial_segment_tree_leaves);

    std::vector<int> result_indices;
    result_indices.reserve(n_items);
    int last_selected_type = NO_TYPE;

    for (int k = 0; k < n_items; ++k) {
        SegTreeNode current_best_choice;

        if (last_selected_type == NO_TYPE) {
            current_best_choice = seg_tree.query(0, m_types - 1);
        } else {
            SegTreeNode choice_from_left_part = seg_tree.query(0, last_selected_type - 1);
            SegTreeNode choice_from_right_part = seg_tree.query(last_selected_type + 1, m_types - 1);
            
            current_best_choice = merge_nodes(choice_from_left_part, choice_from_right_part);
        }

        if (current_best_choice.min_orig_idx == INF_IDX) {
            break;
        }

        int chosen_original_idx = current_best_choice.min_orig_idx;
        int chosen_type = current_best_choice.type_idx;

        result_indices.push_back(chosen_original_idx);
        last_selected_type = chosen_type;

        items_by_type[chosen_type].pop_front();

        if (!items_by_type[chosen_type].empty()) {
            seg_tree.update(chosen_type, SegTreeNode(items_by_type[chosen_type].front(), chosen_type));
        } else {
            seg_tree.update(chosen_type, SegTreeNode(INF_IDX, chosen_type));
        }
    }

    for (size_t i = 0; i < result_indices.size(); ++i) {
        std::cout << result_indices[i] << (i == result_indices.size() - 1 ? "" : " ");
    }
    std::cout << std::endl;

    return 0;
}