# F1 GridScope

## Live URL
https://noorfatimaavyn.pythonanywhere.com

## GitHub
https://github.com/NoorFatima-avyn/f1-gridscope

## What it does
A comprehensive Formula 1 data explorer covering seasons 2021–2026.

### Features
- Season archive with driver standings and constructor standings
- Full driver grid with real headshot photos from OpenF1 API
- Race calendar with podium results on click
- Circuit archive with historical winners (2021–2026)
- Circuit detail pages per circuit
- F1 car technical breakdown per season with Wikipedia images
- AI race predictor powered by Gemini AI
- F1 AI chatbox (F1-only responses)

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python 3 + Flask |
| Frontend | HTML + CSS + JavaScript |
| Database | Firebase Firestore |
| F1 Data | Jolpica F1 API + OpenF1 API |
| Car/Circuit Images | Wikipedia REST API |
| AI | Google Gemini API |
| Hosting | PythonAnywhere (free tier) |
| Version Control | GitHub |

## Data Sources
- Jolpica F1 API — race results, standings, drivers, circuits (free, no key)
- OpenF1 API — driver headshots
- Wikipedia API — car and circuit images
- Google Gemini — AI predictions and chatbox
- Firebase Firestore — cached driver, race, standings data