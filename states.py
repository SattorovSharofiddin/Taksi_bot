from aiogram.fsm.state import StatesGroup, State


class AuthState(StatesGroup):
    full_name = State()
    phone = State()


class DriverState(StatesGroup):
    from_region = State()
    from_district = State()
    to_region = State()
    to_district = State()
    seats_count = State()


class ClientState(StatesGroup):
    from_region = State()
    from_district = State()
    to_region = State()
    to_district = State()
    passenger_count = State()
    price = State()
    type = State()
    additional_info = State()

