import asyncio

from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

router = Router()


class Form(StatesGroup):
    miles = State()
    mili_in_cilometrs = State()
    shvidkosti_polutu = State()
    tisk = State()
    temperature = State()
    weight = State()
    volume = State()
    flight_speeds = State()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    text = "Привіт я створений для розрахунку величин.\nПереглянути інструкцію та повну інформацію про бота ти можеш у вкладці Допомога"
    text2 = "Для початку роботи натисни на кнопку Калькулятор /calc"
    kb = [
        [KeyboardButton(text="Калькулятор"), KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text)
    await asyncio.sleep(1)
    await message.answer(text2, reply_markup=keyboard)


@router.message(lambda message: message.text == "Назад")
async def back(message: types.Message, state: FSMContext):
    text2 = "Для повернення в меню калькулятора натисніть на кнопку"
    kb = [[KeyboardButton(text="Калькулятор")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer(text2, reply_markup=keyboard)


@router.message(
    lambda message: message.text == "Калькулятор" or message.text == "/calc"
)
async def cmd_menu(message: types.Message, state: FSMContext):
    text1 = "Оберіть потрібну вам величину для розрахунку"

    kb = [
        [KeyboardButton(text="1.Конвертування відстаней")],
        [KeyboardButton(text="4.Температури")],
        [KeyboardButton(text="2.Швидкості польоту")],
        [KeyboardButton(text="5.Вага")],
        [KeyboardButton(text="3.Тиск")],
        [KeyboardButton(text="6.Англійських галонів в літри")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await asyncio.sleep(1)
    await message.answer(text1, reply_markup=keyboard)


@router.message(lambda message: message.text == "Допомога")
async def process_with_puree(message: types.Message):
    text1 = "Телеграм бот створенно на замовленння студентам НАУ, розробник @ds0903"
    text2 = """Ви можете підтримати розробника донатом; це не обов'язково, але бот працює на сервері не безкоштовно.\n\nMonobank: `5375.4141.2663.2131`\n\nРозробка телеграм-ботів для вашого бізнесу під ключ @ds0903"""
    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(text1)
    await asyncio.sleep(2)
    await message.answer(text2)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)


@router.message(lambda message: message.text == "1.Конвертування відстаней")
async def process_with_puree(message: types.Message, state: FSMContext):
    text1 = "Напишіть відстань а вона буде конвертована"
    await asyncio.sleep(1)
    await message.answer(text1, reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.mili_in_cilometrs)


@router.message(lambda message: message.text == "2.Швидкості польоту")
async def process_with_puree(message: types.Message, state: FSMContext):
    text1 = "Введіть число а воно буде конвертовано до величини відносно інших одиниць виміру"

    await message.answer(text1, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await state.set_state(Form.flight_speeds)


@router.message(lambda message: message.text == "3.Тиск")
async def process_with_puree(message: types.Message, state: FSMContext):
    text1 = "Введіть число а воно буде конвертовано до величини відносно інших одиниць виміру"

    await message.answer(text1, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await state.set_state(Form.tisk)


@router.message(lambda message: message.text == "4.Температури")
async def process_with_puree(message: types.Message, state: FSMContext):
    text1 = "Введіть число а воно буде конвертовано до величини відносно інших одиниць виміру"

    await message.answer(text1, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await state.set_state(Form.temperature)


@router.message(lambda message: message.text == "5.Вага")
async def process_with_puree(message: types.Message, state: FSMContext):
    text1 = "Введіть число а воно буде конвертовано до величини відносно інших одиниць виміру"

    await message.answer(text1, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await state.set_state(Form.weight)


@router.message(lambda message: message.text == "6.Англійських галонів в літри")
async def process_with_puree(message: types.Message, state: FSMContext):
    text1 = "Введіть число а воно буде конвертовано до величини відносно інших одиниць виміру"

    await message.answer(text1, reply_markup=types.ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await state.set_state(Form.volume)


@router.message(Form.mili_in_cilometrs)
async def miles_in_cilometrs(message: types.Message, state: FSMContext):
    try:
        number = float(message.text)
        result = {
            "NM_to_km": number * 1.852,  # Морські милі в кілометрах
            "km_to_NM": number / 1.852,  # Кілометри в морські милі
            "SM_to_km": number * 1.609,  # Статутні милі в кілометрах
            "km_to_SM": number / 1.609,  # Кілометри в статутні милі
            "ft_to_m": number * 0.305,  # Фути в метрах
            "m_to_ft": number * 3.281,  # Метри в футах
            "inch_to_mm": number * 25.4,  # Дюйми в міліметри
            "mm_to_inch": number * 0.0394,  # Міліметри в дюйми
            "inch_to_cm": number * 2.54,  # Дюйми в сантиметри
        }

        await message.answer(f"Морські милі в кілометри: {result['NM_to_km']} км")
        await asyncio.sleep(0.5)
        await message.answer(f"Кілометри в морські милі: {result['km_to_NM']} NM")
        await asyncio.sleep(0.5)
        await message.answer(f"Англійські милі в кілометри: {result['SM_to_km']} км")
        await asyncio.sleep(0.5)
        await message.answer(f"Кілометри в англійські милі: {result['km_to_SM']} SM")
        await asyncio.sleep(0.5)
        await message.answer(f"Фути в метри: {result['ft_to_m']} м")
        await asyncio.sleep(0.5)
        await message.answer(f"Метри в фути: {result['m_to_ft']} ft")
        await asyncio.sleep(0.5)
        await message.answer(f"Дюйми в міліметри: {result['inch_to_mm']} мм")
        await asyncio.sleep(0.5)
        await message.answer(f"Міліметри в дюйми: {result['mm_to_inch']} дюйми")
        await asyncio.sleep(0.5)
        await message.answer(f"Дюйми в сантиметри: {result['inch_to_cm']} см")

        await state.clear()
    except ValueError:
        await message.answer("Похибка, введіть число, будь ласка!")

    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)


@router.message(Form.flight_speeds)
async def flight_speeds(message: types.Message, state: FSMContext):
    try:
        number = float(
            message.text
        )  # Використовуйте float для більшої точності з числами
        result = {
            "kt_to_kmh": number * 1.852,  # Вузли в км/год
            "kmh_to_kt": number * 0.539,  # Км/год у вузли
            "kt_to_ms": number * 0.514,  # Вузли в м/с
            "ms_to_kt": number * 1.9438,  # М/с у вузли
            "ftmin_to_ms": number * 0.00508,  # Фути/хв в м/с
            "ms_to_ftmin": number * 196.85,  # М/с у футів/хв
        }

        await message.answer(f"Вузли в км/год: {result['kt_to_kmh']} км/год")
        await asyncio.sleep(0.5)
        await message.answer(f"Км/год у вузли: {result['kmh_to_kt']} kt")
        await asyncio.sleep(0.5)
        await message.answer(f"Вузли в м/с: {result['kt_to_ms']} м/с")
        await asyncio.sleep(0.5)
        await message.answer(f"М/с у вузли: {result['ms_to_kt']} kt")
        await asyncio.sleep(0.5)
        await message.answer(f"Фути/хв в м/с: {result['ftmin_to_ms']} м/с")
        await asyncio.sleep(0.5)
        await message.answer(f"М/с у футів/хв: {result['ms_to_ftmin']} ft/min")

        await state.clear()

    except ValueError:
        await message.answer("Похибка, введіть число, будь ласка!")

    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)


@router.message(Form.tisk)
async def tisk_conversion(message: types.Message, state: FSMContext):
    try:
        number = float(
            message.text
        )  # Використовуйте float для обробки чисел з дробовою частиною
        result = {
            "hPa_to_mmHg": number * 0.75,  # Гектопаскалі в мм рт. ст.
            "mmHg_to_hPa": number * 4 / 3,  # Мм рт. ст. в гектопаскалі
            "inHg_to_mmHg": number * 25.4,  # Дюйми рт. ст. в мм рт. ст.
            "mmHg_to_inHg": number / 25.4,  # Мм рт. ст. в дюйми рт. ст.
            "inHg_to_hPa": number * 33.863,  # Дюйми рт. ст. в гектопаскалі
            "hPa_to_inHg": number / 33.863,  # Гектопаскалі в дюйми рт. ст.
        }

        await message.answer(f"{number} hPa = {result['hPa_to_mmHg']} мм рт. ст.")
        await asyncio.sleep(0.5)
        await message.answer(f"{number} мм рт. ст. = {result['mmHg_to_hPa']} hPa")
        await asyncio.sleep(0.5)
        await message.answer(
            f"{number} дюйми рт. ст. = {result['inHg_to_mmHg']} мм рт. ст."
        )
        await asyncio.sleep(0.5)
        await message.answer(
            f"{number} мм рт. ст. = {result['mmHg_to_inHg']} дюйми рт. ст."
        )
        await asyncio.sleep(0.5)
        await message.answer(f"{number} дюйми рт. ст. = {result['inHg_to_hPa']} hPa")
        await asyncio.sleep(0.5)
        await message.answer(f"{number} hPa = {result['hPa_to_inHg']} дюйми рт. ст.")

        await state.clear()

    except ValueError:
        await message.answer("Похибка, введіть число, будь ласка!")

    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)


@router.message(Form.temperature)
async def temperature_conversion(message: types.Message, state: FSMContext):
    try:
        temp_c = float(message.text)
        result = {
            "c_to_f": (temp_c * 1.8) + 32,  # Цельсій в Фаренгейт
            "f_to_c": (temp_c - 32) / 1.8,  # Фаренгейт в Цельсій
        }

        await message.answer(f"{temp_c} ºC = {result['c_to_f']} ºF")
        await asyncio.sleep(0.5)
        await message.answer(f"{temp_c} ºF = {result['f_to_c']} ºC")

        await state.clear()

    except ValueError:
        await message.answer("Похибка, введіть число, будь ласка!")

    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)


@router.message(Form.weight)
async def weight_conversion(message: types.Message, state: FSMContext):
    try:
        number = float(message.text)
        result = {
            "lbs_to_kg": number * 0.45359,  # Фунти в кілограми
            "kg_to_lbs": number * 2.2046,  # Кілограми в фунти
            "tons_to_lbs": number * 2204.6,  # Метричні тонни в фунти
            "lbs_to_tons": number / 2204.6,  # Фунти в метричні тонни
        }

        await message.answer(f"{number} lbs = {result['lbs_to_kg']} кг")
        await asyncio.sleep(0.5)
        await message.answer(f"{number} кг = {result['kg_to_lbs']} lbs")
        await asyncio.sleep(0.5)
        await message.answer(f"{number} метричних тонн = {result['tons_to_lbs']} lbs")
        await asyncio.sleep(0.5)
        await message.answer(f"{number} lbs = {result['lbs_to_tons']} метричних тонн")

        await state.clear()

    except ValueError:
        await message.answer("Похибка, введіть число, будь ласка!")

    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)


@router.message(Form.volume)
async def volume_conversion(message: types.Message, state: FSMContext):
    try:
        number = float(message.text)
        result = {
            "gallons_to_liters": number * 4.546,  # Англійські галони в літри
            "liters_to_gallons": number / 4.546,  # Літри в англійські галони
            "gallons_to_us_gallons": number
            * 1.2205,  # Англійські галони в умовні галони
            "us_gallons_to_gallons": number
            * 0.830,  # Умовні галони в англійські галони
        }

        await message.answer(
            f"{number} англ. галонів = {result['gallons_to_liters']} літрів"
        )
        await asyncio.sleep(0.5)
        await message.answer(
            f"{number} літрів = {result['liters_to_gallons']} англ. галонів"
        )
        await asyncio.sleep(0.5)
        await message.answer(
            f"{number} англ. галонів = {result['gallons_to_us_gallons']} умовних галонів"
        )
        await asyncio.sleep(0.5)
        await message.answer(
            f"{number} умовних галонів = {result['us_gallons_to_gallons']} англ. галонів"
        )

        await state.clear()

    except ValueError:
        await message.answer("Похибка, введіть число, будь ласка!")

    kb = [
        [KeyboardButton(text="Калькулятор")],
        [KeyboardButton(text="Допомога")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await asyncio.sleep(1)
    await message.answer("Повернутися в головне меню?", reply_markup=keyboard)

    ###########

    try:
        number = int(message.text)
        currency = "Кілометри"
        kilometrs, santimetrs, metrs = await cmd_calc(message, number, currency)
        await asyncio.sleep(0.5)
        await message.answer(f"Кілометри в милях {str(kilometrs)}")
        await asyncio.sleep(0.5)
        await message.answer(f"Кілометри в сантиметрах {str(santimetrs)}")
        await asyncio.sleep(0.5)
        await message.answer(f"Кілометри в метрах {str(metrs)}")
        await state.clear()
    except ValueError:
        await message.answer("Введіть правильне число, будь ласка!")
