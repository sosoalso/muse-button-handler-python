# 대충 사용법

button_handler = Button()
button_handler.add_event_handler("push", callback_action_push)
button_handler.add_event_handler("release", callback_action_release)
DV_TP.port[2].button[101].watch(button_handler.handle_event)

repeat_button_handler = Button(repeat_interval=0.3)
repeat_button_handler.add_event_handler("repeat", callback_action_repeat)
DV_TP.port[2].button[102].watch(repeat_button_handler.handle_event)

hold_button_handler.append(Button(hold_time=1.7))
hold_button_handler[i].add_event_handler("hold", callback_action_hold)
DV_TP.port[2].button[103].watch(hold_button_handler.handle_event)