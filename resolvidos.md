# resolvidos.md

Problemas aceitos num juiz. Um `.py` por problema em `solucoes/<juiz>/`, com nome e link nas 2 primeiras linhas.
Só entra aqui depois do AC.

| # | Problema | Juiz | Técnicas | Solução |
|---|---|---|---|---|
| 1 | [Independent Set (EDPC P)](https://atcoder.jp/contests/dp/tasks/dp_p) | AtCoder | DP em árvore, DFS iterativa, mod | `solucoes/atcoder/edpc_p_independent_set.py` |
| 2 | [Game Routes](https://cses.fi/problemset/task/1681) | CSES 1681 | DP em DAG, Kahn, mod | `solucoes/cses/1681_game_routes.py` |
| 3 | [Static Range Minimum Queries](https://cses.fi/problemset/task/1647) | CSES 1647 | Sparse table | `solucoes/cses/1647_static_range_minimum.py` |
| 84 | [Tree Distances II](https://cses.fi/problemset/task/1133) | CSES 1133 | Rerooting (DP em árvore) | `solucoes/cses/1133_tree_distances_ii.py` |
| 87 | [Dynamic Range Minimum Queries](https://cses.fi/problemset/task/1649) | CSES 1649 | Segment tree (min com update) | `solucoes/cses/1649_dynamic_range_minimum.py` |
| 88 | [Investigation](https://cses.fi/problemset/task/1202) | CSES 1202 | Dijkstra + DP em DAG (contar menores caminhos), argsort por distância | `solucoes/cses/1202_investigation.py` |
| 89 | [Distance Queries](https://cses.fi/problemset/task/1135) | CSES 1135 | Binary lifting (LCA) + profundidade | `solucoes/cses/1135_distance_queries.py` |
| 93 | [Maximum Subarray Sum](https://cses.fi/problemset/task/1643) | CSES 1643 | Kadane | `solucoes/cses/1643_maximum_subarray_sum.py` |
| 94 | [Playlist](https://cses.fi/problemset/task/1141) | CSES 1141 | Two pointers / janela (última posição de cada valor) | `solucoes/cses/1141_playlist.py` |
| 95 | [Tree Diameter](https://cses.fi/problemset/task/1131) | CSES 1131 | Diâmetro de árvore (duas BFS) | `solucoes/cses/1131_tree_diameter.py` |
| 96 | [Apple Division](https://cses.fi/problemset/task/1623) | CSES 1623 | Bitmask (todos os subconjuntos) | `solucoes/cses/1623_apple_division.py` |
| 97 | [Tower of Hanoi](https://cses.fi/problemset/task/2165) | CSES 2165 | Recursão (n → n−1) | `solucoes/cses/2165_tower_of_hanoi.py` |
| 98 | [Message Route](https://cses.fi/problemset/task/1667) | CSES 1667 | BFS + reconstruir o caminho pelo pai | `solucoes/cses/1667_message_route.py` |
| 101 | [Road Reparation](https://cses.fi/problemset/task/1675) | CSES 1675 | Árvore geradora mínima (Prim com heap) | `solucoes/cses/1675_road_reparation.py` |
| 102 | [Advertisement](https://cses.fi/problemset/task/1142) | CSES 1142 | Pilha monotônica (1º menor à esquerda e à direita de cada tábua) | `solucoes/cses/1142_advertisement.py` |
| 4 | [Reverse Permutation (ABC465 C)](https://atcoder.jp/contests/abc465/tasks/abc465_c) | AtCoder | Construção nas duas pontas, deque | `solucoes/atcoder/abc465_c_reverse_permutation.py` |
| 5 | [Skill Up (ABC167 C)](https://atcoder.jp/contests/abc167/tasks/abc167_c) | AtCoder | DFS enumerando escolhas (pilha), poda | `solucoes/atcoder/abc167_c_skill_up.py` |
| 6 | [Plumage Palette (ABC464 C)](https://atcoder.jp/contests/abc464/tasks/abc464_c) | AtCoder | Offline com ponteiro, dicionário de contagem | `solucoes/atcoder/abc464_c_plumage_palette.py` |
| 7 | [Giant Domino (ABC412 C)](https://atcoder.jp/contests/abc412/tasks/abc412_c) | AtCoder | Guloso de alcance, ordenação | `solucoes/atcoder/abc412_c_giant_domino.py` |
| 8 | [Bonus EXP (ABC369 D)](https://atcoder.jp/contests/abc369/tasks/abc369_d) | AtCoder | DP com estado pequeno (paridade) | `solucoes/atcoder/abc369_d_bonus_exp.py` |
| 9 | [LOWER (ABC314 D)](https://atcoder.jp/contests/abc314/tasks/abc314_d) | AtCoder | Processamento reverso | `solucoes/atcoder/abc314_d_lower.py` |
| 10 | [Illuminate Buildings (ABC385 C)](https://atcoder.jp/contests/abc385/tasks/abc385_c) | AtCoder | Enumerar passo + início | `solucoes/atcoder/abc385_c_illuminate_buildings.py` |
| 11 | [Cuboid Sum Query (ABC366 D)](https://atcoder.jp/contests/abc366/tasks/abc366_d) | AtCoder | Prefixo 3D | `solucoes/atcoder/abc366_d_cuboid_sum_query.py` |
| 12 | [Union of Interval (ABC256 D)](https://atcoder.jp/contests/abc256/tasks/abc256_d) | AtCoder | Unir intervalos (ordenar + esticar o fim) | `solucoes/atcoder/abc256_d_union_of_interval.py` |
| 13 | [Doubles (ABC392 D)](https://atcoder.jp/contests/abc392/tasks/abc392_d) | AtCoder | Dicionário de contagem, todos os pares | `solucoes/atcoder/abc392_d_doubles.py` |
| 14 | [Take ABC 2 (ABC447 D)](https://atcoder.jp/contests/abc447/tasks/abc447_d) | AtCoder | Emparelhamento guloso com ponteiros | `solucoes/atcoder/abc447_d_take_abc_2.py` |
| 15 | [Swap to Gather (ABC393 D)](https://atcoder.jp/contests/abc393/tasks/abc393_d) | AtCoder | Mediana como ponto de encontro | `solucoes/atcoder/abc393_d_swap_to_gather.py` |
| 16 | [Chalkboard Median (ABC458 D)](https://atcoder.jp/contests/abc458/tasks/abc458_d) | AtCoder | Duas heaps (mediana em fluxo) | `solucoes/atcoder/abc458_d_chalkboard_median.py` |
| 17 | [IPFL (ABC199 C)](https://atcoder.jp/contests/abc199/tasks/abc199_c) | AtCoder | Operação global com flag | `solucoes/atcoder/abc199_c_ipfl.py` |
| 18 | [Sake or Water (ABC441 C)](https://atcoder.jp/contests/abc441/tasks/abc441_c) | AtCoder | Guloso de pior caso, ordenação | `solucoes/atcoder/abc441_c_sake_or_water.py` |
| 19 | [Max Straight (ABC446 D)](https://atcoder.jp/contests/abc446/tasks/abc446_d) | AtCoder | DP por valor (dicionário) | `solucoes/atcoder/abc446_d_max_straight.py` |
| 20 | [Sum = 0 (ABC362 C)](https://atcoder.jp/contests/abc362/tasks/abc362_c) | AtCoder | Começar no mínimo e distribuir a folga | `solucoes/atcoder/abc362_c_sum_0.py` |
| 21 | [One Time Swap (ABC345 C)](https://atcoder.jp/contests/abc345/tasks/abc345_c) | AtCoder | Contar pares pelo complemento | `solucoes/atcoder/abc345_c_one_time_swap.py` |
| 22 | [Splitting Pile (ARC078 C)](https://atcoder.jp/contests/abc067/tasks/arc078_a) | AtCoder | Prefixo (soma da esquerda e da direita) | `solucoes/atcoder/arc078_a_splitting_pile.py` |
| 23 | [Maximize the Gap (ABC463 D)](https://atcoder.jp/contests/abc463/tasks/abc463_d) | AtCoder | Busca binária na resposta + verificador guloso | `solucoes/atcoder/abc463_d_maximize_the_gap.py` |
| 24 | [Template Matching (ABC054 B)](https://atcoder.jp/contests/abc054/tasks/abc054_b) | AtCoder | Força bruta em grid (toda posição × todo deslocamento) | `solucoes/atcoder/abc054_b_template_matching.py` |
| 83 | [Knight (ABC145 D)](https://atcoder.jp/contests/abc145/tasks/abc145_d) | AtCoder | Aritmética modular (fatorial + inverso), C(n, k) | `solucoes/atcoder/abc145_d_knight.py` |
| 85 | [Matching (EDPC O)](https://atcoder.jp/contests/dp/tasks/dp_o) | AtCoder | DP sobre bitmask | `solucoes/atcoder/edpc_o_matching.py` |
| 86 | [Present (ABC038 D)](https://atcoder.jp/contests/abc038/tasks/abc038_d) | AtCoder | LIS com bisect + ordenar com desempate | `solucoes/atcoder/abc038_d_present.py` |
| 90 | [Fenwick Tree (ALPC B)](https://atcoder.jp/contests/practice2/tasks/practice2_b) | AtCoder | Fenwick (soma com update), 0-indexado → 1-indexado | `solucoes/atcoder/alpc_b_fenwick_tree.py` |
| 91 | [転倒数 (Chokudai 001 J)](https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j) | AtCoder | Inversões com Fenwick (contagem por valor) | `solucoes/atcoder/chokudai_s001_j_inversions.py` |
| 92 | [Shift and Inversions (ABC190 F)](https://atcoder.jp/contests/abc190/tasks/abc190_f) | AtCoder | Inversões com Fenwick + atualizar a resposta pelo que muda na rotação | `solucoes/atcoder/abc190_f_shift_and_inversions.py` |
| 100 | [Friends (ABC177 D)](https://atcoder.jp/contests/abc177/tasks/abc177_d) | AtCoder | DSU (tamanho do maior grupo) | `solucoes/atcoder/abc177_d_friends.py` |
| 25 | [Two Sum](https://leetcode.com/problems/two-sum/) | LeetCode | Dicionário (complemento) | `solucoes/leetcode/two_sum.java` |
| 26 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | LeetCode | Lista ligada | `solucoes/leetcode/remove_duplicates_from_sorted_list.py` |
| 27 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | LeetCode | Ordenação | `solucoes/leetcode/merge_sorted_array.py` |
| 28 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | LeetCode | Árvore binária (em-ordem) | `solucoes/leetcode/binary_tree_inorder_traversal.py` |
| 29 | [Same Tree](https://leetcode.com/problems/same-tree/) | LeetCode | Árvore binária (recursão) | `solucoes/leetcode/same_tree.py` |
| 30 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | LeetCode | Árvore binária (recursão) | `solucoes/leetcode/symmetric_tree.py` |
| 31 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | LeetCode | Árvore binária (recursão) | `solucoes/leetcode/maximum_depth_of_binary_tree.py` |
| 32 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | LeetCode | Árvore binária (dividir ao meio) | `solucoes/leetcode/convert_sorted_array_to_binary_search_tree.py` |
| 33 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | LeetCode | DP de contagem | `solucoes/leetcode/climbing_stairs.py` |
| 34 | [Circular Sentence](https://leetcode.com/problems/circular-sentence/) | LeetCode | String | `solucoes/leetcode/circular_sentence.py` |
| 35 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) | LeetCode | Lista ligada | `solucoes/leetcode/swap_nodes_in_pairs.py` |
| 36 | [String Compression III](https://leetcode.com/problems/string-compression-iii/) | LeetCode | String (contar sequências) | `solucoes/leetcode/string_compression_iii.py` |
| 37 | [Minimum Number of Changes to Make Binary String Beautiful](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/) | LeetCode | Guloso em pares | `solucoes/leetcode/minimum_number_of_changes_to_make_binary_string_beautiful.py` |
| 38 | [Find if Array Can Be Sorted](https://leetcode.com/problems/find-if-array-can-be-sorted/) | LeetCode | Bits, blocos | `solucoes/leetcode/find_if_array_can_be_sorted.py` |
| 39 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | LeetCode | Árvore binária (recursão) | `solucoes/leetcode/minimum_depth_of_binary_tree.py` |
| 40 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | LeetCode | Árvore binária (pré-ordem) | `solucoes/leetcode/binary_tree_preorder_traversal.py` |
| 41 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | LeetCode | Árvore binária (pós-ordem) | `solucoes/leetcode/binary_tree_postorder_traversal.py` |
| 42 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | LeetCode | Lista ligada (nó sentinela) | `solucoes/leetcode/remove_linked_list_elements.py` |
| 43 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | LeetCode | Árvore binária (recursão) | `solucoes/leetcode/invert_binary_tree.py` |
| 44 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | LeetCode | Árvore binária (recursão) | `solucoes/leetcode/sum_of_left_leaves.py` |
| 45 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | LeetCode | Árvore binária de busca | `solucoes/leetcode/search_in_a_binary_search_tree.py` |
| 46 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | LeetCode | Exponenciação rápida | `solucoes/leetcode/powx_n.py` |
| 47 | [Remove Nth Node from End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | LeetCode | Lista ligada (dois ponteiros com distância fixa) | `solucoes/leetcode/remove_nth_node_from_end_of_list.py` |
| 48 | [Largest Combination with Bitwise and Greater than Zero](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/) | LeetCode | Contar por bit | `solucoes/leetcode/largest_combination_with_bitwise_and_greater_than_zero.py` |
| 49 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | LeetCode | DP (triângulo de Pascal) | `solucoes/leetcode/pascals_triangle.py` |
| 50 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | LeetCode | Guloso | `solucoes/leetcode/can_place_flowers.py` |
| 51 | [Counting Words with a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/) | LeetCode | String | `solucoes/leetcode/counting_words_with_a_given_prefix.py` |
| 52 | [Container with Most Water](https://leetcode.com/problems/container-with-most-water/) | LeetCode | Dois ponteiros nas pontas | `solucoes/leetcode/container_with_most_water.py` |
| 53 | [Jump Game](https://leetcode.com/problems/jump-game/) | LeetCode | Guloso de alcance | `solucoes/leetcode/jump_game.py` |
| 54 | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) | LeetCode | DP em grid (de trás pra frente) | `solucoes/leetcode/dungeon_game.py` |
| 55 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | LeetCode | Lista ligada (nó sentinela) | `solucoes/leetcode/add_two_numbers.py` |
| 56 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | LeetCode | Ordenação | `solucoes/leetcode/maximum_gap.py` |
| 57 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | LeetCode | Matemática (dígitos) | `solucoes/leetcode/palindrome_number.py` |
| 58 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | LeetCode | String | `solucoes/leetcode/roman_to_integer.py` |
| 59 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | LeetCode | String | `solucoes/leetcode/longest_common_prefix.py` |
| 60 | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) | LeetCode | Grid (contar o início de cada peça) | `solucoes/leetcode/battleships_in_a_board.py` |
| 61 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | LeetCode | Mochila ilimitada + contagem | `solucoes/leetcode/coin_change_ii.py` |
| 62 | [Check if Matrix Is X Matrix](https://leetcode.com/problems/check-if-matrix-is-x-matrix/) | LeetCode | Grid | `solucoes/leetcode/check_if_matrix_is_x_matrix.py` |
| 63 | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | LeetCode | Marcar no próprio array | `solucoes/leetcode/find_all_numbers_disappeared_in_an_array.py` |
| 64 | [Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/) | LeetCode | Simulação | `solucoes/leetcode/sign_of_the_product_of_an_array.py` |
| 65 | [Convert 1d Array into 2d Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | LeetCode | Simulação | `solucoes/leetcode/convert_1d_array_into_2d_array.py` |
| 66 | [Array Partition](https://leetcode.com/problems/array-partition/) | LeetCode | Ordenação + guloso | `solucoes/leetcode/array_partition.py` |
| 67 | [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) | LeetCode | Conjunto | `solucoes/leetcode/check_if_the_sentence_is_pangram.py` |
| 68 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | LeetCode | Dois ponteiros nas pontas | `solucoes/leetcode/squares_of_a_sorted_array.py` |
| 69 | [Thousand Separator](https://leetcode.com/problems/thousand-separator/) | LeetCode | Formatação | `solucoes/leetcode/thousand_separator.py` |
| 70 | [Count Dominant Indices](https://leetcode.com/problems/count-dominant-indices/) | LeetCode | Sufixo (soma) | `solucoes/leetcode/count_dominant_indices.py` |
| 71 | [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | LeetCode | Grid (varrer por coluna) | `solucoes/leetcode/the_k_weakest_rows_in_a_matrix.py` |
| 72 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) | LeetCode | Simulação | `solucoes/leetcode/monotonic_array.py` |
| 73 | [Split Strings by Separator](https://leetcode.com/problems/split-strings-by-separator/) | LeetCode | String | `solucoes/leetcode/split_strings_by_separator.py` |
| 74 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | LeetCode | Simulação | `solucoes/leetcode/fizz_buzz.py` |
| 75 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | LeetCode | Simulação | `solucoes/leetcode/concatenation_of_array.py` |
| 76 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | LeetCode | Simulação | `solucoes/leetcode/shuffle_the_array.py` |
| 77 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | LeetCode | Contar sequências | `solucoes/leetcode/max_consecutive_ones.py` |
| 78 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) | LeetCode | Contagem | `solucoes/leetcode/set_mismatch.py` |
| 79 | [Can Make Arithmetic Progression from Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) | LeetCode | Ordenação | `solucoes/leetcode/can_make_arithmetic_progression_from_sequence.py` |
| 80 | [Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer/) | LeetCode | Matemática (soma de PA) | `solucoes/leetcode/find_the_pivot_integer.py` |
| 81 | [Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/) | LeetCode | Grid (varrer nas 4 direções) | `solucoes/leetcode/count_unguarded_cells_in_the_grid.py` |
| 82 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | LeetCode | Prefixo + dicionário | `solucoes/leetcode/subarray_sum_equals_k.py` |
| 99 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | LeetCode | Melhor valor até aqui (mínimo de prefixo) | `solucoes/leetcode/best_time_to_buy_and_sell_stock.py` |
