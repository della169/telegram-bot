import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# AMBIL TOKEN DARI ENVIRONMENT VARIABLE (AMAN)
TOKEN = os.getenv("BOT_TOKEN")

# URL BANNER
BANNER_URL = "https://victorycool.com/slidervivatogel1.webp"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    nama = user.first_name or "BOSKU"

    text = (
        f"Halo {nama}! 👋\n\n"
        "🔥 SELAMAT DATANG DI BOT VIVATOGEL 🔥\n\n"
        "✅ Situs Resmi & Terpercaya\n"
        "🎰 Pasaran Togel Lengkap\n"
        "🎮 Provider Slot Populer\n\n"
        "🔥 PROMO TERPANAS:\n"
        "💰 Bonus New Member 20%\n"
        "💰 Bonus Rollingan Slot 0.5%\n"
        "💰 Mega Turnover Slot\n"
        "💰 Bonus Cashback Slot 3%\n"
        "💰 Bonus Cashback E-Lottery 5%\n"
        "💰 Bonus Referral Slot 0.1%\n"
        "💰 Bonus Cashback Casino hingga 15%\n"
        "💰 Bonus Cashback Live Casino Pragmatic hingga 15%\n"
        "💰 Bonus Cashback Arcade 5%\n"
        "💰 Bonus Deposit Harian 2%\n"
        "💰 Bonus Prize 2 dan Prize 3\n\n"
        "⚡ Akses Cepat: klik menu di bawah 👇"
    )

    keyboard = [
        [InlineKeyboardButton("🔴 Link Daftar Vivatogel", url="https://goid.cc/vivaterpercaya")],
        [InlineKeyboardButton("🔗 Link Alternatif Vivatogel", url="https://goid.cc/apkvivatogel")],
        [InlineKeyboardButton("💬 Livechat Vivatogel", url="https://secure.livechatenterprise.com/licence/15579411/v2/open_chat.cgi")],
        [InlineKeyboardButton("📘 Facebook Vivatogel", url="https://www.facebook.com/vivatogel303/")],
        [InlineKeyboardButton("🔥 RTP Terupdate Vivatogel", url="https://rtpvivaprox.it.com/")],
        [InlineKeyboardButton("🎁 Promo & Bonus Vivatogel", url="https://goid.cc/vivapromo")],
        [InlineKeyboardButton("🚀 Prediksi Vivatogel", url="https://goid.cc/rtpviva")],
    ]

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=BANNER_URL,
        caption=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN belum diset di Environment Variable")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()


