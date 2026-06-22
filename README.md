## Run the code

1. Create and activate a virtual environment:
   - Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI app with Uvicorn:

```bash
uvicorn main:app --reload
```

4. Open the app in your browser:

```text
http://127.0.0.1:8000
```

## Available Routes

- `GET /`
  - Returns a welcome message from the root endpoint.
- `POST /auth/login`
  - Returns a login success message.
- `POST /auth/register`
  - Returns a user registration success message.
- `POST /auth/update-password`
  - Accepts JSON with an `email` field and returns a password update message.

## Execute Python Scripts from `basics`

1. Open a command prompt or terminal in the `basics` folder.
2. Run a script with:

```bash
python filename.py
```
