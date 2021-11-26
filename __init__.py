# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from aqt.reviewer import Reviewer
from aqt import gui_hooks


def answer_buttons(buttons_tuple, reviewer, card):
    count = reviewer.mw.col.sched.answerButtons(card)

    good_button_index = 3
    if count in (2, 3):
        good_button_index = 2

    def button(colour, text):
        return f'<b style="color:{colour}">{text}</b>'

    return (1, button('#f00', '外れ')), (good_button_index, button('#0f0', '当たり'))


def answer_card(self, ease):
    button_ease_by_button_count = {
        2: [None, 1, 2, 2, 2],  # 2 buttons: 1 Fail, 2 Pass
        3: [None, 1, 2, 2, 2],  # 3 buttons: 1 Fail, 2 Pass
        4: [None, 1, 3, 3, 3]  # 4 buttons: 1 Fail, 3 Pass
    }

    cnt = self.mw.col.sched.answerButtons(self.card)  # Get button count

    try:
        ease = button_ease_by_button_count[cnt][ease]
    except (KeyError, IndexError):
        pass

    __old_answer_card(self, ease)


gui_hooks.reviewer_will_init_answer_buttons.append(answer_buttons)
__old_answer_card = Reviewer._answerCard
Reviewer._answerCard = answer_card
