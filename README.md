# Smart Display Dashboard

A modern, high-contrast, zero-scroll always-on smart display kiosk dashboard designed for phones and tablets.

- **📱 Phone Edition (OPPO A3 ~20:9 landscape)**: [`index.html`](https://chanchunfong1111.github.io/smart-dashboard/)
- **🍎 Tablet Edition (iPad 4:3 All-in-One)**: [`ipad.html`](https://chanchunfong1111.github.io/smart-dashboard/ipad.html)

![Dashboard Preview](https://img.shields.io/badge/Display-Always--On%20Kiosk-sky?style=flat-square)
![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20TailwindCSS%20%7C%20Vanilla%20JS-amber?style=flat-square)
![Weather](https://img.shields.io/badge/Weather-Open--Meteo%20API-emerald?style=flat-square)

---

## 🍎 iPad Edition (`ipad.html`)

Designed specifically for Apple iPad and Android tablet 4:3 / 16:10 screens:

1. **All-in-One Tablet Layout**:
   - Digital Clock, Today's Weather, 5-Day Forecast, Family Notes, and Full Agenda are **all visible simultaneously** without switching tabs or scrolling.
2. **Universal Calendar Support (100% Client-Side Privacy)**:
   - **Google Calendar**: Paste your secret `.ics` feed URL.
   - **Apple iCloud Calendar**: Native support for `webcal://` share links.
   - **National Holidays**: Built-in 1-tap toggles for Japan 🇯🇵, Malaysia 🇲🇾, Singapore 🇸🇬, United States 🇺🇸, and United Kingdom 🇬🇧.
   - **Direct .ics Import**: Import `.ics` calendar files directly from iPad Files or iCloud Drive.
   - **Local Custom Events**: Add one-off or recurring events directly on the iPad screen.
3. **iPad Kiosk Optimization**:
   - Safari PWA support: Tap **Share** → **Add to Home Screen** to run full-screen without Safari toolbars.
   - iOS **Guided Access** compatible for 24/7 locked bedside or desk dock display.
   - Native Screen Wake Lock to prevent iPad display sleep while docked.
   - Bedside amber-red nightstand mode to eliminate blue light at night.

---

## 📱 OPPO A3 Phone Edition (`index.html`)

Tailored for ultra-wide ~20:9 phone displays (800×360 CSS px):
- Ultra-wide 2-column compact bento grid.
- End-to-end AES-256-GCM encrypted background Google Calendar sync via GitHub Actions.
- Solid pitch-black OLED background to conceal display burn-in and kiosk watermarks.
- Anti-burn-in periodic subpixel shift.

---

## 🚀 How to Use / Share

### For Your Friend on iPad:
1. Open Safari on the iPad and visit:
   ```
   https://chanchunfong1111.github.io/smart-dashboard/ipad.html
   ```
2. Tap the **Share** button (box with upward arrow) → tap **Add to Home Screen**.
3. Open the new "Smart Display" icon from the iPad home screen.
4. Tap **Calendars** to link their own Google or Apple iCloud calendar, or pick their national holidays!

---

## 📄 License
MIT License. Free to customize, share, and deploy.
