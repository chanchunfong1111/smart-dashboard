# Smart Display Dashboard (OPPO A3 Edition)

A modern, standalone, always-on smart display kiosk dashboard designed to fit ultra-wide phone and tablet aspect ratios (specifically tailored for the **OPPO A3 ~20:9 landscape** dock view, ~802×360 CSS px) with **zero vertical scrolling**.

![Dashboard Preview](https://img.shields.io/badge/Display-Always--On%20Kiosk-sky?style=flat-square)
![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20TailwindCSS%20%7C%20Vanilla%20JS-amber?style=flat-square)
![Weather](https://img.shields.io/badge/Weather-Open--Meteo%20API-emerald?style=flat-square)

---

## 📱 Features

### 1. Zero-Scroll 20:9 Landscape Bento Layout
- Designed for 20:9 landscape devices (such as the OPPO A3 on a desk or nightstand dock).
- Locked to `100dvh` (`overflow: hidden`) so all widgets fit simultaneously on a single screen without vertical scrolling.
- Includes a **`20:9 A3` simulator toggle** to preview the exact phone frame when viewing on a desktop monitor.

### 2. Google Calendar Color-Coded Agenda
- **iCal (`.ics`) Sync**: Plug in your Google Calendar *"Secret address in iCal format (`.ics`)"* or import `.ics` files directly.
- **6-Color Coding Palette**: Assign custom colors (Sky, Emerald, Amber, Rose, Violet, Orange) to different calendar feeds.
- **Smart Auto-Color Inference**: Automatically assigns colors based on keywords in event titles (e.g. *Meeting/Work* in Sky, *Urgent/Exam/Flight* in Rose, *Gym/Fitness* in Orange, *Family/Dinner* in Violet).
- **Category Filter Pills**: Quick filter bar at the top of the agenda widget.
- **Imminent Badges**: Automatic `NOW` and `in Xm` relative countdown badges.
- **Local Event Quick Add**: Tap `+` to add local events directly to the agenda.

### 3. Open-Meteo Weather Center
- **Zero API Key Required**: Powered by Open-Meteo's free REST API.
- **Current Conditions**: Large temperature readout, condition description, feels-like, and today's high/low.
- **4 Key Metrics**: Live humidity, wind speed, rain probability, and UV index.
- **Tabbed Forecast View**: Seamlessly switch between **Hourly 24h Outlook** and **5-Day Daily Outlook** with proportional temperature range bars.
- **Location Picker & GPS**: Search any city worldwide or use device GPS geolocation with one tap.

### 4. Digital Clock & Date
- Large typography with JetBrains Mono.
- Live seconds display and 12-hour (AM/PM) or 24-hour time format toggle.
- Formatted date, week number (`W43`), day of year, and astronomical sunrise/sunset indicators.

### 5. Quick Notes Checklist
- In-memory and `localStorage`-backed checklist for quick reminders.
- Toggle completed status or delete items with one tap.

### 6. Hardware & Kiosk Display Features
- **Screen Wake Lock API**: Keeps the display on without sleeping or dimming.
- **OLED Anti-Burn-In Protection**: Subtly shifts pixels every 2 minutes by random subpixel offsets (-2px to +2px) to prevent static element burn-in on OLED/AMOLED screens.
- **Bedside / Nightstand Mode**: Replaces the entire UI with a low-glare, dark red/amber monochrome palette (`#ea580c`) to protect eyes and prevent blue light emission at night.
- **Fullscreen API**: Tap the maximize icon to hide browser address bars and system navigation.

---

## 🚀 Getting Started

No build step, Node.js, or complex installation is required.

1. Clone the repository:
   ```bash
   git clone https://github.com/chanchunfong1111/smart-dashboard.git
   cd smart-dashboard
   ```
2. Open `index.html` in your browser (e.g., Chrome, Edge, Safari):
   ```bash
   # On Windows
   start index.html
   ```

### Deploying to GitHub Pages
1. Go to your repository settings on GitHub: **Settings** → **Pages**.
2. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
3. Select `main` branch and `/ (root)` folder, then click **Save**.
4. Open the generated GitHub Pages URL on your phone or tablet browser and add it to your home screen!

---

## 📅 How to Connect Your Google Calendar

1. On a desktop browser, open [Google Calendar](https://calendar.google.com).
2. Click the gear icon (**Settings**) in the top right.
3. In the left sidebar, click on the calendar you want to sync under **Settings for my calendars**.
4. Scroll down to the **Integrate calendar** section.
5. Copy the URL from **Secret address in iCal format** (`https://calendar.google.com/calendar/ical/.../basic.ics`).
6. In this Smart Dashboard, tap **Sync** on the Agenda widget, paste the URL, pick a color, and click **+ Add Feed**.
