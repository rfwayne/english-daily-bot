import os
import urllib.request
import urllib.parse
import json
from datetime import date

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Fixed start date -> day counter used to pick level & paragraph.
START_DATE = date(2026, 7, 4)

PARAGRAPHS = [
    # ---- Level 1 (very simple) ----
    {
        "level": 1,
        "text": "My name is Sara. I live in a small city. I have a brother and a sister. We are happy together. Every day, I wake up early and drink tea.",
        "vocab": {
            "wake up": "بیدار شدن",
            "together": "با هم",
            "small": "کوچک"
        },
        "translation": "اسم من ساراست. من در یک شهر کوچک زندگی می‌کنم. یک برادر و یک خواهر دارم. ما با هم خوشحالیم. هر روز، زود بیدار می‌شوم و چای می‌نوشم."
    },
    {
        "level": 1,
        "text": "I like coffee in the morning. My friend likes tea. We usually meet at a cafe near my house. The weather today is sunny and warm.",
        "vocab": {
            "usually": "معمولا",
            "meet": "دیدن (کسی)",
            "sunny": "آفتابی"
        },
        "translation": "من صبح‌ها قهوه دوست دارم. دوستم چای دوست دارد. ما معمولا در یک کافه نزدیک خانه‌ام همدیگر را می‌بینیم. هوای امروز آفتابی و گرم است."
    },
    {
        "level": 1,
        "text": "This is my room. It is not big, but I love it. I have a bed, a desk, and many books. At night, I read a book before I sleep.",
        "vocab": {
            "desk": "میز کار",
            "before": "قبل از",
            "sleep": "خوابیدن"
        },
        "translation": "این اتاق من است. بزرگ نیست، ولی من عاشقش هستم. یک تخت، یک میز و کتاب‌های زیادی دارم. شب‌ها قبل از خواب یک کتاب می‌خوانم."
    },
    # ---- Level 2 ----
    {
        "level": 2,
        "text": "Last weekend, I decided to visit my grandmother. She lives in a quiet village outside the city. The trip took almost two hours, but it was worth it because her food is amazing.",
        "vocab": {
            "decided": "تصمیم گرفتم",
            "quiet": "آرام",
            "worth it": "ارزشش را داشت"
        },
        "translation": "آخر هفته گذشته، تصمیم گرفتم به دیدن مادربزرگم بروم. او در روستایی آرام بیرون از شهر زندگی می‌کند. سفر تقریبا دو ساعت طول کشید، اما ارزشش را داشت چون غذایش فوق‌العاده است."
    },
    {
        "level": 2,
        "text": "Learning a new language can be difficult at first, but it becomes easier with practice. The key is to speak every day, even if you make mistakes.",
        "vocab": {
            "at first": "در ابتدا",
            "practice": "تمرین",
            "mistake": "اشتباه"
        },
        "translation": "یاد گرفتن یک زبان جدید ممکن است در ابتدا سخت باشد، اما با تمرین راحت‌تر می‌شود. نکته کلیدی این است که هر روز صحبت کنی، حتی اگر اشتباه کنی."
    },
    {
        "level": 2,
        "text": "My favorite season is autumn. The leaves change color, and the weather becomes cooler. I enjoy walking in the park and taking photos of the trees.",
        "vocab": {
            "season": "فصل",
            "leaves": "برگ‌ها",
            "cooler": "خنک‌تر"
        },
        "translation": "فصل مورد علاقه من پاییز است. برگ‌ها رنگ عوض می‌کنند و هوا خنک‌تر می‌شود. من از قدم زدن در پارک و عکس گرفتن از درخت‌ها لذت می‌برم."
    },
    # ---- Level 3 ----
    {
        "level": 3,
        "text": "Many people believe that success comes from talent alone, but in reality, consistency plays a much bigger role. Those who keep working, even when progress feels slow, usually achieve their goals eventually.",
        "vocab": {
            "consistency": "پشتکار/ثبات",
            "eventually": "در نهایت",
            "achieve": "به دست آوردن"
        },
        "translation": "خیلی‌ها فکر می‌کنند موفقیت فقط از استعداد می‌آید، اما در واقعیت، پشتکار نقش خیلی بزرگ‌تری دارد. کسانی که به کار کردن ادامه می‌دهند، حتی وقتی پیشرفت کند به نظر می‌رسد، معمولا در نهایت به اهدافشان می‌رسند."
    },
    {
        "level": 3,
        "text": "The city has changed a lot over the past ten years. New buildings have replaced old houses, and traffic has become much worse. Still, some neighborhoods have kept their original charm.",
        "vocab": {
            "replaced": "جایگزین کرد",
            "traffic": "ترافیک",
            "charm": "جذابیت"
        },
        "translation": "شهر در ده سال گذشته خیلی تغییر کرده. ساختمان‌های جدید جای خانه‌های قدیمی را گرفته‌اند و ترافیک خیلی بدتر شده. با این حال، بعضی محله‌ها جذابیت اصلی خودشان را حفظ کرده‌اند."
    },
    {
        "level": 3,
        "text": "Before making a big decision, it helps to write down the advantages and disadvantages. This simple habit can prevent a lot of regret later, because it forces you to think clearly.",
        "vocab": {
            "advantages": "مزایا",
            "disadvantages": "معایب",
            "regret": "پشیمانی"
        },
        "translation": "قبل از گرفتن یک تصمیم بزرگ، نوشتن مزایا و معایب کمک‌کننده است. این عادت ساده می‌تواند بعدا از خیلی پشیمانی جلوگیری کند، چون تو را مجبور می‌کند واضح فکر کنی."
    },
    # ---- Level 4 ----
    {
        "level": 4,
        "text": "Economic sanctions often have unintended consequences that extend far beyond their original target. While policymakers design them to pressure governments, ordinary citizens frequently bear the heaviest burden through inflation and limited access to global markets.",
        "vocab": {
            "unintended": "ناخواسته",
            "burden": "بار (سنگین)",
            "inflation": "تورم"
        },
        "translation": "تحریم‌های اقتصادی اغلب پیامدهای ناخواسته‌ای دارند که فراتر از هدف اصلی‌شان می‌روند. در حالی که سیاست‌گذاران آن‌ها را برای فشار به دولت‌ها طراحی می‌کنند، شهروندان عادی اغلب سنگین‌ترین بار را از طریق تورم و دسترسی محدود به بازارهای جهانی متحمل می‌شوند."
    },
    {
        "level": 4,
        "text": "Entrepreneurship requires more than a good idea; it demands resilience, adaptability, and the willingness to learn from repeated failure. Most successful founders will admit that their early attempts looked nothing like their eventual, thriving businesses.",
        "vocab": {
            "resilience": "تاب‌آوری",
            "adaptability": "انعطاف‌پذیری",
            "thriving": "رو به رشد/موفق"
        },
        "translation": "کارآفرینی به چیزی بیشتر از یک ایده خوب نیاز دارد؛ به تاب‌آوری، انعطاف‌پذیری و تمایل به یادگیری از شکست‌های مکرر نیاز دارد. اکثر بنیان‌گذاران موفق اعتراف می‌کنند که تلاش‌های اولیه‌شان هیچ شباهتی به کسب‌وکار موفق نهایی‌شان نداشت."
    },
]

def get_paragraph_for_today():
    day_index = (date.today() - START_DATE).days
    if day_index < 0:
        day_index = 0
    level = min(day_index // 3 + 1, 4)
    same_level = [p for p in PARAGRAPHS if p["level"] == level]
    chosen = same_level[day_index % len(same_level)]
    return chosen, level, day_index

def build_message(p, level, day_index):
    vocab_lines = "\n".join([f"• {w} = {m}" for w, m in p["vocab"].items()])
    msg = (
        f"📅 روز {day_index + 1} | سطح {level}\n\n"
        f"📖 پاراگراف امروز:\n{p['text']}\n\n"
        f"🆕 لغات جدید:\n{vocab_lines}\n\n"
        f"🇮🇷 معنی کامل پاراگراف:\n{p['translation']}"
    )
    return msg

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text}).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        return response.read()

if __name__ == "__main__":
    paragraph, level, day_index = get_paragraph_for_today()
    message = build_message(paragraph, level, day_index)
    send_telegram_message(message)
    print("Message sent.")
