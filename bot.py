from
 telethon import TelegramClient, events
import asyncio

api_id = 22308891
api_hash = "00cc5f4ac21c96cd144c93572e18c8da"

client = TelegramClient("session", api_id, api_hash)

# ► LISTA GRUP ŹRÓDŁOWYCH
SOURCE_CHATS = [
    "WWASTYLEMARKET",
    "gm2lmarket",
    "wwa420",
    "top1legitni",
    "Mefedronowe_lowe",
    "warszawaitrawa",
    "CentrumBHP",
    "warszawaweb",
    "wwabazarek",
    "brodno_mef_polak",
    "hustlaswwa",
    "warszawa_sobie_radzi",
    "legiaWwaWtsWtb",
    "warszawaanoca",
    "DRAGSPAM",
    "wtswtbwwa"
]

# ► GRUPA DOCELOWA
TARGET_CHAT = "https://t.me/+9dhlw8x4_7A3NDY0"


@client.on(events.NewMessage(chats=SOURCE_CHATS))
async def handler(event):
    msg = (event.message.message or "").lower()

    # ──────────────────────────────────────
    # TU WKLEJ SWOJE FRAZY KTÓRE OZNACZAJĄ "SZUKAM"
    trigger = [
        "kto ma",
    "ktoś ma",
    "ktos ma",
    "kto posiada",
    "kto ogarnia",
    "ktoś ogarnia",
    "ktos ogarnia",
    "szukam",
    "kupie",
    "kupię",
    "wtb",
    "need",
    "nvm?",
    "poszukuje",
    "ogarnie ktoś",
    "ogarnie ktos",
    "ogarnia ktoś",
    "ogarnia ktos"
         "wtb",
        "ktos",
        "ktoś",
        "kupie",
        "kupię",
        "szukam"   # ← możesz dopisywać po przecinku
    ]
    # ──────────────────────────────────────

    # ──────────────────────────────────────
    # TU WKLEJ SWOJE FRAZY KTÓRE OZNACZAJĄ "CZEGO SZUKA"
    words = [
       "mef",
"m3f",
"m33f",
"mati",
"mateusz",
"xan",
"x@n",
"oksykodon",
"zan",
"ox",
"0x",
"0ks",
"oks",
"oksa",
"okulary",
"klony",
"clon",
"cl0n",
"klon",
"kl0n",
"jablka",
"jabłka",
"pomarancze",
"pomarańcze",
"kry",
"mefistofeles",
"kamlot",
"m€f",
"krykiet",
"kapusta",
"cebula",
"mat",
"m@t",
"buch",
"buszek",
"buszido",
"busz3k",
"bubu",
"ziolo",
"zioło",
"palenie",
"jaranie",
"kamyk",
"weed",
"w33d",
"w3ed",
"kris",
"krystian",
"magda",
"madzia",
"4mmc",
"3mmc",
"4cmc",
"3cmc",
"kamien",
"kmk",
"marihuana",
"buszido",
"bu$zido",
"eufo",
"speed",
"euf0",
"sp33d",
"szkło",
"szklo",
"coco",
"c0c0",
"coc0",
"c0co",
"koka",
"k0ka",
"flex",
"boliwia",
"ameryka",
"🥥",
"🥦",
"💎",
"snieg",
"śnieg",
"busz",
         "mef",
        "m3f",
        "koka",
        "koks",
        "xtc",
        "md",
        "trawa",
        "zioło",
        "grzyby"
        # ← tu dopisuj swoje słowa
    ]
    # ──────────────────────────────────────

    # jeśli wiadomość nie pasuje → pomiń
    if not any(t in msg for t in trigger):
        return
    if not any(w in msg for w in words):
        return

    try:
        await client.forward_messages(TARGET_CHAT, event.message)
        print(f"✅ Forward poszedł: {msg[:50]}")
    except:
        sender = await event.get_sender()
        uname = sender.username if sender.username else "brak_nicku"
        text = (event.message.message or "") + "\n@" + uname

        if event.message.media:
            try:
                await client.send_file(TARGET_CHAT, event.message.media, caption=text)
                print(f"📎 Wysłano jako plik + tekst: {msg[:50]}")
                return
            except:
                pass

        await client.send_message(TARGET_CHAT, text)
        print(f"✏️ Wysłano jako tekst: {msg[:50]}")


async def main():
    await client.start()
    print("BOT WYSTARTOWAŁ ✅ (multi-grupy + anty-blokada)")
    await client.run_until_disconnected()

asyncio.run(main())

#test