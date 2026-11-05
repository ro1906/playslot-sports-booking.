# PlaySlot Animated Streamlit Project

This ZIP includes the latest PlaySlot website source, with the updated navy/orange/ivory palette and subtle animations.

## Run locally in VS Code (Windows)

1. Extract this ZIP.
2. Open the extracted `PlaySlot_Animated_Streamlit` folder in VS Code.
3. Select Terminal → New Terminal.
4. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the app:

   ```bash
   python -m streamlit run app.py
   ```

6. Open the local URL Streamlit prints, usually http://localhost:8501.

If an old Streamlit app is running, stop it first using Ctrl+C in that terminal.

## Deploy when ready

Upload `app.py`, `index.html`, and `requirements.txt` to a GitHub repository. In Streamlit Community Cloud, create an app from that repository and set the main file path to `app.py`.

## Demo limitations

Venue listings are sample data. Bookings and favourites are stored in the browser's localStorage; there is no shared backend/database, login system, or real payment processing.
