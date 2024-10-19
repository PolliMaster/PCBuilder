import logging
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from aiogram import F
from aiogram.types import CallbackQuery
from builds import ready_builds, format_build, save_user_request
from config import ADMIN_ID

logger = logging.getLogger(__name__)

def register_handlers(dp):  # Функция для регистрации обработчиков
    @dp.message(Command("start"))
    async def start(message: types.Message):
        await message.answer("Привет! Я помогу собрать компьютер. Выбери действие:\n"
                             "/choose_components - выбрать комплектующие\n"
                             "/select_ready_builds - выбрать готовую сборку")

    @dp.message(Command("choose_components"))
    async def choose_components(message: types.Message):
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="Процессор", callback_data="cpu"))
        builder.add(types.InlineKeyboardButton(text="Видеокарта", callback_data="gpu"))
        builder.add(types.InlineKeyboardButton(text="ОЗУ", callback_data="ram"))
        builder.add(types.InlineKeyboardButton(text="Диск", callback_data="ssd"))
        builder.add(types.InlineKeyboardButton(text="Мат плата", callback_data="mtp"))
        await message.answer("Выберите компонент:", reply_markup=builder.as_markup())
        await message.answer("Вернуться на главное меню: /start")

    @dp.callback_query(F.data.in_(['cpu', 'gpu', 'ram', 'ssd', 'mtp']))
    async def handle_component_choice(call: CallbackQuery):
        component = call.data
        await call.message.answer(f"Вы выбрали {component.upper()}. Вот доступные варианты:")
        
        if component == "cpu":
            await call.message.answer("1. Ryzen 5 5600X\nЦена: 12 499 руб.\nСсылка: https://www.dns-shop.ru/product/61d281e916f9ed20/processor-amd-ryzen-5-5600x-oem/")
            await call.message.answer("2. Ryzen 7 5800X\nЦена: 21 499 руб.\nСсылка: https://www.dns-shop.ru/product/4e48fbd4fb77ed20/processor-amd-ryzen-7-5800x-oem/")
            await call.message.answer("3. Intel Core i5-11400\nЦена: 14 499 руб.\nСсылка: https://www.dns-shop.ru/product/3e2d489416f5ed20/processor-intel-core-i5-11400-oem/")
            await call.message.answer("4. Intel Core i7-11700K\nЦена: 28 999 руб.\nСсылка: https://www.dns-shop.ru/product/c10a4c342773ed20/processor-intel-core-i7-11700k-oem/")
            await call.message.answer("5. Ryzen 9 5900X\nЦена: 32 799 руб.\nСсылка: https://www.dns-shop.ru/product/b4db283bfccbed20/processor-amd-ryzen-9-5900x-oem/")
            await call.message.answer("6. Intel Core i9-11900K\nЦена: 27 299 руб.\nСсылка: https://www.dns-shop.ru/product/39bb11ad280ced20/processor-intel-core-i9-11900k-oem/")
            await call.message.answer("7. Intel Core i3-10100\nЦена: 10 699 руб.\nСсылка: https://www.dns-shop.ru/product/92f0170516f3ed20/processor-intel-core-i3-10100-oem/")
            await call.message.answer("8. Ryzen 5 3600\nЦена: 8 299 руб.\nСсылка: https://www.dns-shop.ru/product/39783e4afccbed20/processor-amd-ryzen-5-3600-oem/")
            await call.message.answer("9. Intel Core i5-10400F\nЦена: 9 599 руб.\nСсылка: https://www.dns-shop.ru/product/155c08a2fd8eed20/processor-intel-core-i5-10400f-oem/")
            await call.message.answer("10. Ryzen 7 3700X\nЦена: 13 499 руб.\nСсылка: https://www.dns-shop.ru/product/4eae94861ec4ed20/processor-amd-ryzen-7-3700x-oem/")
            await call.message.answer("11. Ryzen 9 5950X\nЦена: 45 799 руб.\nСсылка: https://www.dns-shop.ru/product/58fc099217abed20/processor-amd-ryzen-9-5950x-oem/")
            await call.message.answer("12. Intel Core i7-10700F\nЦена: 24 599 руб.\nСсылка: https://www.dns-shop.ru/product/4607168e6a693332/processor-intel-core-i7-10700f-oem/")
            await call.message.answer("13. Ryzen 5 3400G\nЦена: 9 399 руб.\nСсылка: https://www.dns-shop.ru/product/5b3c1e3b90d51b80/processor-amd-ryzen-5-3400g-oem/")
            await call.message.answer("14. Intel Pentium G6400\nЦена: 7 199 руб.\nСсылка: https://www.dns-shop.ru/product/1e516fdd6a793332/processor-intel-pentium-gold-g6400-oem/")
            await call.message.answer("15. AMD Athlon 3000G\nЦена: 4 899 руб.\nСсылка: https://www.dns-shop.ru/product/0e189711fb76ed20/processor-amd-athlon-3000g-oem/")
            await call.message.answer("16. Ryzen 3 3200G\nЦена: 6 899 руб.\nСсылка: https://www.dns-shop.ru/product/588277aa3347ed20/processor-amd-ryzen-3-3200g-oem/")
            await call.message.answer("17. Intel Celeron G5905\nЦена: 3 999 руб.\nСсылка: https://www.dns-shop.ru/product/79b092912808ed20/processor-intel-celeron-g5905-oem/")
            await call.message.answer("18. Ryzen 7 3800X\nЦена: 20 999 руб.\nСсылка: https://www.dns-shop.ru/product/2426953d2777ed20/processor-amd-ryzen-7-3800x-oem/")
            await call.message.answer("Вернуться на главное меню: /start")

        elif component == "gpu":
            await call.message.answer("1. NVIDIA RTX 3060\nЦена: 33 999 руб.\nСсылка: https://www.dns-shop.ru/product/49b77a8077562eb0/videokarta-kfa2-geforce-rtx-3060-core-lhr-36nol7md1vok/")
            await call.message.answer("2. NVIDIA RTX 3070\nЦена: 41 799 руб.\nСсылка: https://www.dns-shop.ru/product/0444348ebf882ff1/videokarta-gigabyte-geforce-rtx-3070-gaming-oc-lhr-gv-n3070gaming-oc-8gd-rev20/")
            await call.message.answer("3. AMD Radeon RX 6700 XT\nЦена: 39 999 руб.\nСсылка: https://www.dns-shop.ru/product/05a26b01ee79d763/videokarta-powercolor-amd-radeon-rx-6700-xt-fighter-axrx-6700xt-12gbd6-3dh/")
            await call.message.answer("4. NVIDIA GTX 1660 Super\nЦена: 22 999 руб.\nСсылка: https://www.dns-shop.ru/product/05b2426176982eb0/videokarta-palit-geforce-gtx-1660-super-gamingpro-ne6166s018j9-1160a-1/")
            await call.message.answer("5. AMD Radeon RX 6600\nЦена: 27 999 руб.\nСсылка: https://www.dns-shop.ru/product/7c767bd1144bed20/videokarta-powercolor-amd-radeon-rx-6600-fighter-axrx-6600-8gbd6-3dh/")
            await call.message.answer("6. NVIDIA RTX 3080\nЦена: 97 499 руб.\nСсылка: https://www.dns-shop.ru/product/b91bc2d21b68ed20/videokarta-inno3d-geforce-rtx-3080-ti-x3-oc-lhr-n308t3-126xx-1810va44/")
            await call.message.answer("7. AMD Radeon RX 6900 XT\nЦена: 125 999 руб.\nСсылка: https://www.dns-shop.ru/product/4884011040603332/videokarta-gigabyte-amd-radeon-rx-6900-xt-gaming-oc-gv-r69xtgaming-oc-16gd/")
            await call.message.answer("8. NVIDIA RTX 3050\nЦена: 25 999 руб.\nСсылка: https://www.dns-shop.ru/product/f6a696bd3b11ed20/videokarta-msi-geforce-rtx-3050-ventus-2x-xs-oc-rtx-3050-ventus-2x-xs-8g-oc/")
            await call.message.answer("9. AMD Radeon RX 6500 XT\nЦена: 18 299 руб.\nСсылка: https://www.dns-shop.ru/product/fa9a78b683fded20/videokarta-asrock-amd-radeon-rx-6500-xt-phantom-gaming-d-oc-rx6500xt-pgd-4go/")
            await call.message.answer("10. NVIDIA GTX 1650\nЦена: 16 999 руб.\nСсылка: https://www.dns-shop.ru/product/30bd04fb7f63ed20/videokarta-kfa2-geforce-gtx-1650-x-black-65sql8ds93ek/")
            await call.message.answer("11. AMD Radeon RX 5500 XT\nЦена: 53 799 руб.\nСсылка: https://www.dns-shop.ru/product/3363e1421a493332/videokarta-asrock-amd-radeon-rx-5500-xt-challenger-d-oc-rx5500xt-cld-8go/")
            await call.message.answer("12. NVIDIA RTX 3090\nЦена: 89 999 руб.\nСсылка: https://www.dns-shop.ru/product/9b7e39c8ecc33332/videokarta-gigabyte-geforce-rtx-3090-gaming-oc-gv-n3090gaming-oc-24gd/")
            await call.message.answer("13. AMD Radeon RX 6800\nЦена: 62 999 руб.\nСсылка: https://www.dns-shop.ru/product/65abf2ea3da3ed20/videokarta-asrock-amd-radeon-rx-6800-xt-phantom-gaming-oc-rx6800xt-pg-16go/")
            await call.message.answer("14. NVIDIA GTX 1050 Ti\nЦена: 6 999 руб.\nСсылка: https://www.dns-shop.ru/product/f264761599c43330/videokarta-gigabyte-geforce-gtx-1050-ti-gv-n105td5-4gd/")
            await call.message.answer("15. AMD Radeon RX 5700 XT\nЦена: 60 299 руб.\nСсылка: https://www.dns-shop.ru/product/f2d0891e02051b80/videokarta-powercolor-amd-radeon-rx-5700-xt-liquid-devil-axrx-5700xt-8gbd6-wdhoc/")
            await call.message.answer("16. NVIDIA GTX 1660\nЦена: 22 999 руб.\nСсылка: https://www.dns-shop.ru/product/05b2426176982eb0/videokarta-palit-geforce-gtx-1660-super-gamingpro-ne6166s018j9-1160a-1/")
            await call.message.answer("17. AMD Radeon RX 5600 XT\nЦена: 23 899 руб.\nСсылка: https://www.dns-shop.ru/product/6f087f87d7843332/videokarta-gigabyte-amd-radeon-rx-5600-xt-windforce-rev-20-gv-r56xtwf2-6gd-rev20/")
            await call.message.answer("18. AMD Radeon RX 6700 XT\nЦена: 39 999 руб.\nСсылка: https://www.dns-shop.ru/product/05a26b01ee79d763/videokarta-powercolor-amd-radeon-rx-6700-xt-fighter-axrx-6700xt-12gbd6-3dh/")
            await call.message.answer("Вернуться на главное меню: /start")

        elif component == "ram":
            await call.message.answer("1. Corsair Vengeance 16GB\nЦена: 15 499 руб.\nСсылка: https://www.dns-shop.ru/product/6586ce61b8862714/operativnaa-pamat-corsair-vengeance-cmk32gx5m2b6000c36-32-gb/")
            await call.message.answer("2. Kingston HyperX Fury 16GB\nЦена: 5 299 руб.\nСсылка: https://www.dns-shop.ru/product/40bc1b0cc2143332/operativnaa-pamat-kingston-hyperx-fury-black-hx426c16fb3k216-16-gb/")
            await call.message.answer("3. G.Skill Ripjaws V 16GB\nЦена: 11 399 руб.\nСсылка: https://www.dns-shop.ru/product/a3ea697874b11b80/operativnaa-pamat-gskill-ripjaws-v-f4-3600c16d-32gvkc-32-gb/")
            await call.message.answer("4. Patriot Viper elite ii 16GB\nЦена: 7 399 руб.\nСсылка: https://www.dns-shop.ru/product/1950decde5f02ff2/operativnaa-pamat-patriot-viper-elite-ii-pve2432g320c8k-32-gb/")
            await call.message.answer("5. Corsair Dominator Platinum 32GB\nЦена: 20 399 руб.\nСсылка: https://www.dns-shop.ru/product/d58e4e014606ed20/operativnaa-pamat-corsair-dominator-platinum-rgb-cmt32gx5m2b5600z36-32-gb/")
            await call.message.answer("6. Kingston HyperX Predator 16GB\nЦена: 9 199 руб.\nСсылка: https://www.dns-shop.ru/product/4ab4e9f708393332/operativnaa-pamat-kingston-hyperx-predator-hx446c19pb3k216-16-gb/")
            await call.message.answer("7. G.Skill Trident Z5 RGB 32GB\nЦена: 12 799 руб.\nСсылка: https://www.dns-shop.ru/product/c6ac4ce2bbcded20/operativnaa-pamat-gskill-trident-z5-rgb-f5-6000j3040f16gx2-tz5rk-32-gb/")
            await call.message.answer("8. Team group T-Force Vulcan Z 32GB\nЦена: 7 499 руб.\nСсылка: https://www.dns-shop.ru/product/57a67f634b093332/operativnaa-pamat-team-group-t-force-vulcan-z-tlzgd432g3200hc16fdc01-32-gb/")
            await call.message.answer("9. Corsair Vengeance LPX 64GB\nЦена: 21 299 руб.\nСсылка: https://www.dns-shop.ru/product/da37ea0c2feaed20/operativnaa-pamat-corsair-vengeance-lpx-cmk64gx4m2e3200c16-64-gb/")
            await call.message.answer("10. G.Skill Ripjaws V 64GB\nЦена: 18 499 руб.\nСсылка: https://www.dns-shop.ru/product/3cefb83c74b11b80/operativnaa-pamat-gskill-ripjaws-v-f4-3200c16d-64gvk-64-gb/")
            await call.message.answer("11. Kingston HyperX Fury 32GB\nЦена: 16 399 руб.\nСсылка: https://www.dns-shop.ru/product/a44837d5c2163332/operativnaa-pamat-kingston-hyperx-fury-black-hx432c16fb3k232-32-gb/")
            await call.message.answer("12. Patriot Viper venom 64GB\nЦена: 24 299 руб.\nСсылка: https://www.dns-shop.ru/product/192f7352907ded20/operativnaa-pamat-patriot-viper-venom-pvv564g560c40k-64-gb/")
            await call.message.answer("13. Corsair Dominator Platinum 64GB\nЦена: 20 399 руб.\nСсылка: https://www.dns-shop.ru/product/c3e004fc2febed20/operativnaa-pamat-corsair-dominator-platinum-rgb-cmt64gx4m2c3600c18-64-gb/")
            await call.message.answer("Вернуться на главное меню: /start")

        elif component == "ssd":
            await call.message.answer("1. Samsung 970 Evo Plus 500GB\nЦена: 7 999 руб.\nСсылка: https://www.dns-shop.ru/product/96b2aefbf765ed20/500-gb-ssd-m2-nakopitel-samsung-970-evo-plus-mz-v7s500bw/")
            await call.message.answer("2. WD Black SN850X 1TB\nЦена: 13 499 руб.\nСсылка: https://www.dns-shop.ru/product/33bc9721ec277c6e/1000-gb-ssd-m2-nakopitel-wd-black-sn850x-wds100t2x0e/")
            await call.message.answer("3. Kingston sxs2000 500GB\nЦена: 6 999 руб.\nСсылка: https://www.dns-shop.ru/product/ee5f2c3ee792ed20/500-gb-vnesnij-ssd-kingston-sxs2000-sxs2000500g/")
            await call.message.answer("4. Crucial P3 Plus 1TB\nЦена: 9 999 руб.\nСсылка: https://www.dns-shop.ru/product/37167e56e563ed20/1000-gb-ssd-m2-nakopitel-crucial-p3-plus-ct1000p3pssd8/")
            await call.message.answer("5. Samsung 980 Pro 1TB\nЦена: 13 499 руб.\nСсылка: https://www.dns-shop.ru/product/e5bc121a1873ed20/1000-gb-ssd-m2-nakopitel-samsung-980-pro-mz-v8p1t0bw/")
            await call.message.answer("6. WD Blue SN570 1TB\nЦена: 10 199 руб.\nСсылка: https://www.dns-shop.ru/product/805813ea1870ed20/1000-gb-ssd-m2-nakopitel-wd-blue-sn570-wds100t3b0c/")
            await call.message.answer("7. Kingston NV2 1TB\nЦена: 6 999 руб.\nСсылка: https://www.dns-shop.ru/product/1815ac731eaa42ae/1000-gb-ssd-m2-nakopitel-kingston-nv2-snv2s1000g/")
            await call.message.answer("8. Crucial MX500 1TB\nЦена: 9 199 руб.\nСсылка: https://www.dns-shop.ru/product/79e926852f57ed20/1000-gb-25-sata-nakopitel-crucial-mx500-ct1000mx500ssd1/")
            await call.message.answer("9. Samsung 870 Evo 1TB\nЦена: 11 799 руб.\nСсылка: https://www.dns-shop.ru/product/49172afd28f9ed20/1000-gb-25-sata-nakopitel-samsung-870-evo-mz-77e1t0bweu/")
            await call.message.answer("10. WD Black SN750 SE 1TB\nЦена: 12 199 руб.\nСсылка: https://www.dns-shop.ru/product/c0a6dfd021aded20/1000-gb-ssd-m2-nakopitel-wd-black-sn750-se-wds100t1b0e/")
            await call.message.answer("11. Corsair MP600 PRO XT 1TB\nЦена: 14 199 руб.\nСсылка: https://www.dns-shop.ru/product/afbc03b46bcced20/1000-gb-ssd-m2-nakopitel-corsair-mp600-pro-xt-cssd-f1000gbmp600pxt/")
            await call.message.answer("12. ADATA XPG SX8200 Pro 1TB\nЦена: 7 499 руб.\nСсылка: https://www.dns-shop.ru/product/ce8e128ce9651b80/1000-gb-ssd-m2-nakopitel-adata-xpg-sx8200-pro-asx8200pnp-1tt-c/")
            await call.message.answer("13. WD Green SN550 1TB\nЦена: 8 699 руб.\nСсылка: https://www.dns-shop.ru/product/81dea72c31ebed20/1000-gb-ssd-m2-nakopitel-wd-green-sn350-wds100t3g0c/")
            await call.message.answer("14. Crucial BX500 1TB\nЦена: 7 999 руб.\nСсылка: https://www.dns-shop.ru/product/4017fd9d2f57ed20/1000-gb-25-sata-nakopitel-crucial-bx500-ct1000bx500ssd1/")
            await call.message.answer("15. Kingston KC3000 1TB\nЦена: 10 999 руб.\nСсылка: https://www.dns-shop.ru/product/d843b8c700d5ed20/1024-gb-ssd-m2-nakopitel-kingston-kc3000-skc3000s1024g/")
            await call.message.answer("16. Intel 670p series 1TB\nЦена: 9 199 руб.\nСсылка: https://www.dns-shop.ru/product/b4db8bb89f842ff4/1000-gb-ssd-m2-nakopitel-intel-670p-series-ssdpeknu010tzx1-99a39p/")
            await call.message.answer("17. Samsung 970 Evo plus 1TB\nЦена: 10 799 руб.\nСсылка: https://www.dns-shop.ru/product/60dd5734f76bed20/1000-gb-ssd-m2-nakopitel-samsung-970-evo-plus-mz-v7s1t0bw/")
            await call.message.answer("18. Patriot P300 1TB\nЦена: 8 699 руб.\nСсылка: https://www.dns-shop.ru/product/8fd41a7d5c183332/1000-gb-ssd-m2-nakopitel-patriot-p300-p300p1tbm28/")
            await call.message.answer("Вернуться на главное меню: /start")

        elif component == "mtp":
            await call.message.answer("1. ASUS ROG Strix B550-F Gaming\nЦена: 24 299 руб.\nСсылка: https://www.dns-shop.ru/product/afd5377da6df3332/materinskaa-plata-asus-rog-strix-b550-f-gaming/")
            await call.message.answer("2. MSI MAG B650 TOMAHAWK WIFI\nЦена: 26 999 руб.\nСсылка: https://www.dns-shop.ru/product/69e396144e03ed20/materinskaa-plata-msi-mag-b650-tomahawk-wifi/")
            await call.message.answer("3. Gigabyte B550M AORUS ELITE\nЦена: 12 499 руб.\nСсылка: https://www.dns-shop.ru/product/c44cd14acc801b80/materinskaa-plata-gigabyte-b550m-aorus-elite/")
            await call.message.answer("4. ASRock B550 PRO4\nЦена: 13 999 руб.\nСсылка: https://www.dns-shop.ru/product/01e7c50d9bc91b80/materinskaa-plata-asrock-b550-pro4/")
            await call.message.answer("5. MSI MPG B550 GAMING PLUS\nЦена: 15 199 руб.\nСсылка: https://www.dns-shop.ru/product/232aa9f9b9a11b80/materinskaa-plata-msi-mpg-b550-gaming-plus/")
            await call.message.answer("6. ASUS TUF Gaming B550-PLUS\nЦена: 16 999 руб.\nСсылка: https://www.dns-shop.ru/product/3123221ab1d71b80/materinskaa-plata-asus-tuf-gaming-b550-plus/")
            await call.message.answer("7. GIGABYTE B650 AORUS PRO AX\nЦена: 27 699 руб.\nСсылка: https://www.dns-shop.ru/product/ab8082764510ed20/materinskaa-plata-gigabyte-b650-aorus-pro-ax/")
            await call.message.answer("8. MSI MAG B550 TOMAHAWK\nЦена: 16 499 руб.\nСсылка: https://www.dns-shop.ru/product/b9a4575dafa61b80/materinskaa-plata-msi-mag-b550-tomahawk/")
            await call.message.answer("9. ASRock B450 Steel Legend\nЦена: 11 299 руб.\nСсылка: https://www.dns-shop.ru/product/caa062e235a43332/materinskaa-plata-asrock-b450-steel-legend/")
            await call.message.answer("10. ASUS ROG CROSSHAIR X670E HERO\nЦена: 72 999 руб.\nСсылка: https://www.dns-shop.ru/product/044fa65c49c4ed20/materinskaa-plata-asus-rog-crosshair-x670e-hero/")
            await call.message.answer("11. MSI B550-A PRO\nЦена: 14 499 руб.\nСсылка: https://www.dns-shop.ru/product/232aa9fbb9a11b80/materinskaa-plata-msi-b550-a-pro/")
            await call.message.answer("12. Gigabyte Z790 AORUS MASTER X\nЦена: 44 999 руб.\nСсылка: https://www.dns-shop.ru/product/82477c146412ed20/materinskaa-plata-gigabyte-z790-aorus-master-x/")
            await call.message.answer("13. ASUS TUF Gaming B450-PLUS II\nЦена: 12 499 руб.\nСсылка: https://www.dns-shop.ru/product/ae7e7f949e762ff1/materinskaa-plata-asus-tuf-gaming-b450-plus-ii/")
            await call.message.answer("14. Gigabyte B550I AORUS PRO AX\nЦена: 17 799 руб.\nСсылка: https://www.dns-shop.ru/product/4f3c4a329c061b80/materinskaa-plata-gigabyte-b550i-aorus-pro-ax/")
            await call.message.answer("15. ASUS PRIME X670E-PRO WIFI\nЦена: 45 499 руб.\nСсылка: https://www.dns-shop.ru/product/0a70426749c4ed20/materinskaa-plata-asus-prime-x670e-pro-wifi/")
            await call.message.answer("16. MSI MAG B550M MORTAR MAX WIFI\nЦена: 16 999 руб.\nСсылка: https://www.dns-shop.ru/product/c0b7dc3cfcefed20/materinskaa-plata-msi-mag-b550m-mortar-max-wifi/")
            await call.message.answer("17. ASUS TUF Gaming X570-PLUS\nЦена: 9 199 руб.\nСсылка: https://www.dns-shop.ru/product/b7e9075010193332/materinskaa-plata-asus-tuf-gaming-x570-plus/")
            await call.message.answer("Вернуться на главное меню: /start")

    @dp.message(Command("select_ready_builds"))
    async def select_ready_builds(message: types.Message):
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="Игры", callback_data="games"))
        builder.add(types.InlineKeyboardButton(text="Офис", callback_data="office"))
        builder.add(types.InlineKeyboardButton(text="Рендеринг", callback_data="rendering"))
        builder.add(types.InlineKeyboardButton(text="Бюджетный", callback_data="budget"))
        await message.answer("Выберите сферу использования:", reply_markup=builder.as_markup())
        await message.answer("Вернуться на главное меню: /start")

    @dp.callback_query(F.data.in_(['games', 'office', 'rendering', 'budget']))
    async def handle_ready_builds(call: CallbackQuery):
        category = call.data
        components = ready_builds[category]
        result = format_build(components)
        await call.message.answer(result)
        await call.message.answer("Вернуться на главное меню: /start")

    @dp.message(Command("custom_build_request"))
    async def custom_build_request(message: types.Message):
        await message.answer("Опишите ваши пожелания по сборке (бюджет, цель использования, важные компоненты):")

    @dp.message()
    async def handle_custom_request(message: types.Message):
        user_request = message.text
        await message.answer(f"Ваш запрос на сборку принят:\n{user_request}\nМы предложим вам лучшие варианты.")
        await message.answer("Вернуться на главное меню: /start")