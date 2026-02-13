from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
from rembg import remove, new_session
import io

app = FastAPI(title="RemoveBG Microservice")

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Initialize session with u2net (standard model, most robust)
model_name = "u2net"
session = new_session(model_name)

@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    # Relaxed content-type check because curl/Windows might send application/octet-stream
    # We will let PIL/rembg attempt to open it. If it fails, it catches the exception below.
    # if not file.content_type.startswith("image/"):
    #     print(f"Warning: Content-Type is {file.content_type}, but proceeding.")
    
    try:
        # Read image data
        image_data = await file.read()
        
        # Process with rembg using standard u2net and alpha matting
        # Final config: u2net + alpha matting with erosion to clean artifacts
        output_data = remove(
            image_data,
            session=session,
            alpha_matting=True,
            alpha_matting_foreground_threshold=240,
            alpha_matting_background_threshold=20,
            alpha_matting_erode_size=15
        )
        
        # Return as PNG
        return Response(content=output_data, media_type="image/png")
        
    except Exception as e:
        print(f"Error processing image: {e}")
        raise HTTPException(status_code=500, detail="Failed to process image")
