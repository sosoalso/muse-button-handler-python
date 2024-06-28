# 대충 사용법

```
<<<<<<< HEAD
# 넣고 싶은 액션 넣으면 됨... 잉

button_handler = ButtonHandler()
=======
# push, release 넣고 싶은대로 넣으면 됨
button_handler = Button()
>>>>>>> origin/main
button_handler.add_event_handler("push", callback_action_push)
button_handler.add_event_handler("release", callback_action_release)
DV_TP.port[2].button[101].watch(button_handler.handle_event)

repeat_button_handler = ButtonHandler(repeat_interval=0.3)
repeat_button_handler.add_event_handler("repeat", callback_action_repeat)
DV_TP.port[2].button[102].watch(repeat_button_handler.handle_event)

<<<<<<< HEAD
hold_button_handler.append(ButtonHandler(hold_time=1.7, trigger_release_on_hold=True))
hold_button_handler[i].add_event_handler("hold", callback_action_hold)
hold_button_handler[i].add_event_handler("release", callback_action_release)
DV_TP.port[2].button[103].watch(hold_button_handler.handle_event)
```
=======
hold_button_handler.append(Button(hold_time=1.7, trigger_release_on_hold=True))
hold_button_handler[i].add_event_handler("hold", callback_action_hold)
hold_button_handler[i].add_event_handler("release", callback_action_release)
DV_TP.port[2].button[103].watch(hold_button_handler.handle_event)
```
>>>>>>> origin/main
