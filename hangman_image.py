def hangman_display(list):
    for row in list:
        print(row)


x = 3

y = 2

row0 = '          []=========]       '
row1 = '          ||         |       '
row2full = '          ||         O       '
row3full = '          ||  =====--H--====='
row4full = '          ||         H       '
row5full = '          ||         H       '
row6full = '          ||       -----     '
row7full = '          ||       |   |     '
row8full = '          ||       |   |     '
row9full = '          ||      _|   |_    '
row10 = '          ||                 '
row11 = '======================       '

row7_one_leg = '          ||       |         '
row8_one_leg = '          ||       |         '
row9_one_leg = '          ||      _|         '

row7_no_leg = '          ||                 '
row8_no_leg = '          ||                 '
row9_no_leg = '          ||                 '

row3_one_arm = '          ||  =====--H--     '

row3_no_arm = '          ||       --H--     '

row3_no_body = '          ||                 '
row4_no_body = '          ||                 '
row5_no_body = '          ||                 '
row6_no_body = '          ||                 '

row2_no_grape = '          ||                 '

fully_hung = [row0, row1, row2full, row3full, row4full, row5full, row6full, row7full, row8full, row9full, row10, row11]
one_leg = [row0, row1, row2full, row3full, row4full, row5full, row6full, row7_one_leg, row8_one_leg, row9_one_leg, row10, row11]
two_arms = [row0, row1, row2full, row3full, row4full, row5full, row6full, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
one_arm = [row0, row1, row2full, row3_one_arm, row4full, row5full, row6full, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
head_and_body = [row0, row1, row2full, row3_no_arm, row4full, row5full, row6full, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
head = [row0, row1, row2full, row3_no_body, row4_no_body, row5_no_body, row6_no_body, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]
empty = [row0, row1, row2_no_grape, row3_no_body, row4_no_body, row5_no_body, row6_no_body, row7_no_leg, row8_no_leg, row9_no_leg, row10, row11]

display_progression = [[empty, head, head_and_body, one_arm, two_arms, one_leg, fully_hung], [empty, head, head_and_body, one_arm, two_arms, one_leg, fully_hung]]


