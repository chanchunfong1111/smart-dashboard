# Smart Display Dashboard (OPPO A3 Edition)

A modern, high-contrast, always-on smart display kiosk dashboard designed to fit phone and tablet aspect ratios (specifically tailored for the **OPPO A3 ~20:9 landscape** dock view, ~802×360 CSS px) with **zero vertical scrolling**.

![Dashboard Preview](https://img.shields.io/badge/Display-Always--On%20Kiosk-sky?style=flat-square)
![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20TailwindCSS%20%7C%20Vanilla%20JS-amber?style=flat-square)
![Weather](https://img.shields.io/badge/Weather-Open--Meteo%20API-emerald?style=flat-square)

---

## 📱 Features

### 1. High-Contrast, Zero-Scroll 2-Column Bento Layout
- **Watermark-Proof Solid Dark Palette**: Built with deep, opaque surfaces (`#000000` and `#0b0b0f`) so background kiosk watermarks do not bleed through.
- **Large, Legible Typography**: Viewport-scaled fonts designed for clear reading from across the room.
- **Zero Page Scroll**: Everything fits comfortably on one screen locked to `100dvh`.
- **20:9 OPPO A3 Simulator**: Built-in preview toggle in Settings for testing at 800×360 on desktop screens.

### 2. Pre-Configured Google Calendar Agenda
- **Direct Integration**: Pre-configured with your Google Calendar iCal (`.ics`) feed with automatic sync and local repository fallback.
- **Automated GitHub Action**: Runs every 4 hours in `.github/workflows/update-calendar.yml` to refresh calendar events directly from Google Calendar with zero CORS friction.
- **Smart Color-Coding**: Events automatically receive color badges and left accent bars based on title keywords (e.g. Work/Office in Sky, Urgent/Medical in Rose, Fitness in Orange, Family in Violet).
- **Date Grouping & Live Badges**: Events grouped under Today / Tomorrow / Day headings, plus real-time `NOW` and `in Xm` countdown indicators.

### 3. Open-Meteo Weather Center
- **Zero API Key Required**: Live weather fetched from Open-Meteo.
- **Large Readouts**: Big temperature hero, condition description, feels-like, and today's high/low.
- **4 Key Metrics**: Humidity, wind speed, rain probability (next 3 hours peak), and UV index.
- **Full Forecast Tab**: 8 two-hour forecast slots plus a 5-day daily outlook with proportional temperature range bars.
- **Location Picker & GPS**: Search any city worldwide or use device GPS.

### 4. Digital Clock & Date
- Large, bold time display with AM/PM indicator and live seconds.
- Day of the week, full date, week number (`Week 43`), and sunrise/sunset times.
- 12-hour and 24-hour toggle in Settings.

### 5. Quick Notes Checklist
- In-memory and `localStorage`-backed checklist for quick reminders.
- Toggle completed status or delete items with one tap.

### 6. Hardware & Kiosk Display Features
- **Screen Wake Lock API**: Keeps the display on without sleeping or dimming.
- **OLED Anti-Burn-In Protection**: Subtly shifts pixels every 2 minutes by random subpixel offsets (-2px to +2px) to prevent static element burn-in.
- **Bedside / Nightstand Mode**: Replaces the entire UI with a low-glare, dark red/amber monochrome palette (`#f97316` / `#9a3412`) for eye comfort at night.
- **Auto-Cycle Panels**: Optional setting to automatically rotate between Agenda, Forecast, and Notes every 30 seconds.
- **Fullscreen API**: Tap the maximize icon to hide browser address bars and system navigation.

---

## 🚀 Getting Started

No build step or Node.js required.

1. Clone the repository:
   ```bash
   git clone https://github.com/chanchunfong1111/smart-dashboard.git
   cd smart-dashboard
   ```
2. Open `index.html` in your browser:
   ```bash
   start index.html
   ```

### Deploying to GitHub Pages
1. In your GitHub repository: **Settings** → **Pages**.
2. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
3. Select branch **`main`** and folder **`/ (root)`**, then click **Save**.
4. Open your GitHub Pages URL on your OPPO A3 browser:
   `https://chanchunfong1111.github.io/smart-dashboard/`
