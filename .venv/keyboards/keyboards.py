from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import  LEXICON_RU

button_yes = KeyboardButton(text = LEXICON_RU['yes_button'])
button_no = KeyboardButton(text = LEXICON_RU['no_button'])

yes_no_builder = ReplyKeyboardBuilder()
yes_no_builder.row(button_yes,button_no,width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_builder.as_markup(one_time_keyboard = True,
                                                          resize_keyboard = True)

button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_paper= KeyboardButton(text=LEXICON_RU['paper'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
game_builder = ReplyKeyboardBuilder()
game_builder.row(button_rock,button_scissors,button_paper,width=1)

game_kb : ReplyKeyboardMarkup = game_builder.as_markup(resize_keyboard = True)

