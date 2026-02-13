FROM python:3.10-slim

WORKDIR /app

# Install system dependencies 
# rembg uses opencv-python-headless which doesn't require GUI libs usually.
# If issues arise, we can add: apt-get install -y ffmpeg libsm6 libxext6

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the u2net model to avoid timeout on first request or runtime downloads
# This creates the .u2net directory. We can also use a volume mapping in docker-compose.
# For now, let's rely on volume mapping or let it download once.
# To bake it in: RUN python -c "from rembg.session_factory import new_session; new_session('u2net')"

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
