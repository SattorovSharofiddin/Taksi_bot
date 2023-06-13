from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import ClientState
from utils.misc import region_list, get_districts_by_region

order_taxi_router = Router()

######################################################
#                  Validators
######################################################


######################################################
#                  Handlers
######################################################

@order_taxi_router.message(ClientState.from_region)
async def process_from_region(message: Message, state: FSMContext):
    if message.text not in region_list:
        return await message.answer("❗️ Viloyat tanlashda xatolik yuz berdi, iltimos quyidagi viloyatlardan birini tanlang!") # noqa
    await state.update_data(from_region=message.text)
    await message.answer("❗️ Tumanni tanlang")


@order_taxi_router.message(ClientState.from_district)
async def process_from_district(message: Message, state: FSMContext):
    region_name = (await state.get_data())['to_region']
    if message.text not in get_districts_by_region(region_name):
        return await message.answer("❗️ Tuman tanlashda xatolik!") # noqa
    await state.update_data(from_district=message.text)
    await message.answer("Qayerga bormoqchisiz?")️️️ # noqa


@order_taxi_router.message(ClientState.to_region)
async def process_to_region(message: Message, state: FSMContext):
    if message.text not in region_list:
        return await message.answer("❗️ Viloyat tanlashda xatolik yuz berdi, iltimos quyidagi viloyatlardan birini tanlang!") # noqa
    await state.update_data(to_region=message.text)
    await message.answer("❗️ Tumanni tanlang")


@order_taxi_router.message(ClientState.to_district)
async def process_to_district(message: Message, state: FSMContext):
    region_name = (await state.get_data())['to_region']
    if message.text not in get_districts_by_region(region_name):
        return await message.answer("❗️ Tuman tanlashda xatolik!") # noqa
    await state.update_data(to_district=message.text)
    await message.answer("Qayerga bormoqchisiz?")️️️ # noqa


@order_taxi_router.message(ClientState.passenger_count)
async def process_to_district(message: Message, state: FSMContext):
    region_name = (await state.get_data())['to_region']
    if message.text not in get_districts_by_region(region_name):
        return await message.answer("❗️ Tuman tanlashda xatolik!") # noqa
    await state.update_data(to_district=message.text)
    await message.answer("Qayerga bormoqchisiz?")️️️ # noqa


