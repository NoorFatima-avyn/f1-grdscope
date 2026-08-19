

## August 12 2026
- Installed Git 2.55.0
- Created project folder f1-gridscope
- Set up Python virtual environment
- Installed: flask, requests, anthropic



**August 13**
- Connected project to GitHub
- Repo live at: github.com/NoorFatima-avyn/f1-grdscope
- Ready to start writing code
- Flask app running on port 5000
- Connected to Jolpica F1 API
- /api/seasons/2024 returns live F1 driver data ✅
- - All seasons API endpoints working ✅
- /api/seasons/2024/drivers ✅
- /api/seasons/2024/races ✅  
- /api/seasons/2024/driver-standings ✅
- - Homepage UI designed and implemented ✅
- F1 red/black theme, driver cards, stats row, season selector
- Ready to connect to real API data
- - Driver headshots connected from OpenF1 API ✅
- Real photos showing on driver cards
- Some drivers missing photos (abbreviation mismatch - fix later)
- Wrote `app.py` Flask entry point
- Wrote `seasons.py`, `drivers.py`, `races.py`, `teams.py`, `chat.py` blueprints
- Wrote `jolpica.py` — connected to Jolpica F1 API
- First API call working: `/api/seasons/2024/drivers` returning real F1 data
- Homepage UI designed using — F1 red/black theme
- Driver grid connected to real API data
- Commit: `feat: Flask app running, Jolpica API connected`
- Commit: `feat: seasons routes complete, all endpoints returning F1 data`
- Commit: `feat: homepage UI complete, F1 dark theme`

**August 14**

- Connected OpenF1 API for driver headshots
- Real driver photos showing on driver cards
- Firebase Firestore database set up
- All seasons 2021-2025 synced to Firebase (drivers, races, standings)
- Gemini AI chatbox implemented and working
- Commit: `feat: real driver photos loading from OpenF1 API`
- Commit: `feat: Firebase Firestore connected, all seasons synced`
- Commit: `feat: AI chatbox working with Gemini API`

**August 15**

- Rebuilt homepage UI 
- Max hero video section added
- Max trophy photo section added
- Season selector with FINAL/LIVE tags
- Race calendar with round numbers and flags
- Podium results on race click
- Cars page created with technical specs per team per season
- Wikipedia API connected for car images
- Commit: `feat: homepage UI redesigned, Max hero video`
- Commit: `feat: cars page added, race results route`
- Commit: `feat: car images from Wikipedia, race podium results on click`

**August 16**

- Circuit archive page created (tracks.html)
- Circuit images from Wikipedia API
- Winners per circuit 2021-2025
- AI race predictor built with Gemini
- Date-aware predictions (upcoming vs completed races)
- Commit: `feat: circuits page with winners per track 2021-2025`
- Commit: `feat: AI race predictor powered by Gemini`
- Commit: `feat: AI race predictor with date-aware predictions`

**August 17**

- Circuit detail pages created (circuit.html)
- Circuit cards now clickable → opens detail page
- Historical winners 2021-2026 per circuit
- Upcoming race detection (shows "Upcoming" not fake winner)
- Fixed app.py duplicate routes
- README.md added
- Commit: `feat: circuit detail pages with historical winners`
- Commit: `docs: add README`
- Commit: `fix: clean app.py indentation`

**August 18**

- Railway deployment attempted (multiple failures)
- Switched to PythonAnywhere
- Fixed Firebase key to load from environment variable
- Updated all API URLs for production
- Site successfully deployed on PythonAnywhere
- Commit: `fix: Firebase key from environment variable`
- Commit: `fix: update API URLs for production`
- Commit: `feat: F1 GridScope fully deployed on PythonAnywhere`

August 19 

- ERD diagram created
- System architecture diagram created
- Documentation written
- Total commits: **28+**