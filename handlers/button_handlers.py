from aiogram import Router
from aiogram.filters import Text, Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, ReplyKeyboardRemove
from aiogram.types import Message

from keyboards.default import back_to_main, main_menu, driver_accaunt, region, driver_menu, \
    passenger_menu, panel_referal, panel_mandatory, panel_channel, panel_menu
from states import ClientState, DriverState

buttons_router = Router()


@buttons_router.message(Text('🆘 Aloqa'))
async def sos(message: Message):
    await message.answer(
        "@taksi_clone_bot botining <a href=\"https://t.me/all_nc\">TAXIDASUPPORT</a> bilan bog'lanish",
        # noqa
        reply_markup=back_to_main.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Text('🔝 Asosiy Menyu'))
async def start(message: Message):
    photo = FSInputFile('/home/user/projects/aiogram_projects/taksi_bot/images/taksi.jpeg')
    await message.answer_photo(
        caption=f"""😊 Assalomu alaykum {message.from_user.full_name} ,
❗️ Taxi botimizga xush kelibsiz, o'zingizga maqul bo'limni tanlang""",
        photo=photo,
        reply_markup=main_menu.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Command(commands=["cancel"]))
@buttons_router.message(Text(text="cancel", ignore_case=True))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Bekor qilindi!",
        reply_markup=ReplyKeyboardRemove()
    )

'Panel'


@buttons_router.message(Text('🔰 Panel'))
async def panel(message: Message):
    await message.answer(
        f"😊 Admin panelga xush kelibsiz hurmatli {message.from_user.full_name}",
        reply_markup=panel_menu.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Text('📈 Kanal / Guruh'))
async def channel_or_group(message: Message):
    await message.answer(
        "Kanal va guruhlarni qo'shish orqali siz mablag' yig'ishingiz mumkin",
        reply_markup=panel_channel.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Text("Kanal qo'shish"))
async def add_to_channel(message: Message):
    await message.answer(
        "O'z kanalingizga ushbu @uzb_taksi_bot botni admin qilib barcha huquqlarni bering va biror xabarni shu yerga (forward shaklda) yuboring yoki kanalingiz ID raqamini yuboring yoki kanalingiz telegram manzilini yuboring.", # noqa
    )


@buttons_router.message(Text("Guruh qo'shish"))
async def add_to_group(message: Message):
    await message.answer(
        "Kanalingiz qaysi viloyatlar aro ish faoliyatini olib boradi?"
    )


@buttons_router.message(Text("♾ Majburiy a'zo bot"))
async def force_subscribe(message: Message):
    await message.answer(
        "Ushbu bo'lim orqali guruhingizning a'zolari @uzb_taksi_bot ga a'zo bo'lmaguncha yozdirmaydi\n\nBotni guruhingizga ulash uchun Guruhga ulash tugmasini bosing", # noqa
        reply_markup=panel_mandatory.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Text("Majbur guruh qo'shish"))
async def add_to_force_group(message: Message):
    await message.answer(
        "O'z guruhingizga ushbu @uzb_taksi_bot botni admin qilib barcha huquqlarni bering va guruhingiz ID raqamini yuboring yoki guruhingiz telegram manzilini yuboring." # noqa
    )


# referal

@buttons_router.message(Text("👥 Referal"))
async def referal(message: Message):
    await message.answer(
        """Bu havola bilan foydalanuvchilarni yig'ing va pul ishlang https://t.me/uzb_taksi_bot""", # noqa
        reply_markup=panel_referal.as_markup(resize_keyboard=True)
    )


# yordam

@buttons_router.message(Text("🆘 Yordam"))
async def support(message: Message):
    await message.answer(
        "@taksi_clone_bot botining <a href=\"https://t.me/all_nc\">TAXIDASUPPORT</a> bilan bog'lanish", # noqa
        reply_markup=back_to_main.as_markup(resize_keyboard=True)
    )


"""passenger"""


@buttons_router.message(Text("🧍‍♂️ Haydovchi kerak"))
async def need_driver(message: Message):
    await message.answer(
        "Taxi turini tanlang",
        reply_markup=passenger_menu.as_markup(resize_keyboard=True)
    )


"""driver"""


@buttons_router.message(Text("🚕 Haydovchiman"))
async def need_client(message: Message):
    await message.answer(
        "😊 Assalomu alaykum hurmatli .  siz haydovchilik bo'limidasiz Yo'lovchilarni olmoqchi bo'lsangiz yo'l haqqining 5% miqdorida hisobingizda mablag' bo'lishi zarur", # noqa
        reply_markup=driver_menu.as_markup(resize_keyboard=True)
    )


@buttons_router.message(Text("💳 Balans"))
async def balance(message: Message):
    await message.answer(
        """🆔 Hisob raqamingiz: 13261
💳 Hisobingizda:  0.00 so'm

Hisobingizni Payme yoki Click ilovalari orqali Taxida ni izlab ID raqamingizni kiritasiz va to'lov qilmoqchi bo'lgan summangizni yozib hisobni to'ldirasiz. Yoki pasdagi knopkalar orqali to'lov qilishingiz mumkin.

👇🏻 Hisobingizni to'ldirish uchun kerak to'lov tizimini tanlang!""",
        reply_markup=driver_accaunt.as_markup(resize_keyboard=True)
    )


"""region_district"""


@buttons_router.message(or_f(
    Text("Yetib borish"), or_f(Text("Yetkazib berish"), Text("Yo'lovchi kutish"))
))
async def start(message: Message, state: FSMContext):
    if message.text != "Yo'lovchi kutish": # noqa
        await state.set_state(ClientState.to_region)
    else:
        await state.set_state(DriverState.to_region)

    await message.answer(
        "Qayerdasiz?",  # noqa
        reply_markup=region.as_markup(resize_keyboard=True)
    )

