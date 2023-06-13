from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from db import db
from keyboards.default import main_menu
from states import AuthState

main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    if not await db.exists('tlg_user_id', message.from_user.id, 'users'):
        await state.set_state(AuthState.full_name)
        return await message.answer(
            "❗️ Ro'yxatdan o'tish uchun iltimos familiya va ismingizni yuboring!",
            reply_markup=main_menu.as_markup(resize_keyboard=True)
        )
    photo = FSInputFile('/home/user/projects/aiogram_projects/taksi_bot/images/taksi.jpeg')
    await message.answer_photo(
        caption=f"""
😊 Assalomu alaykum Shadowraze ,
❗️ Taxi botimizga xush kelibsiz, o'zingizga maqul bo'limni tanlang
        """,
        photo=photo,
        reply_markup=main_menu.as_markup(resize_keyboard=True)
    )
