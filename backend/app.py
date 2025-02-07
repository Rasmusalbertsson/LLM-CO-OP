from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn


app = FastAPI(title=' ')

# Modell för textgenerering request
class Textrequest(BaseModel):
    prompt:str


class WEB_CO_OP:
    def __init__(self, api_key:str, prompt):
        self.api_key = api_key
        self.prompt = prompt

    def verify_api_key(self):
        if self.api_key != "Your secret api key":
            raise HTTPException(status_code=401, detail="Unmatched api key")
        

    @app.post('/generated_text')
    async def generate_text(request: Textrequest, api_key:str = Depends(verify_api_key)):
        generate_text = f"Generated answer for : {request.prompt}"
        return JSONResponse(content={"result": generate_text})
    
    @app.post('/upload_pdf')
    async def upload_pdf(self,file: UploadFile=File(...), api_key:str = Depends(verify_api_key)):
        try:
            contents = await file.read()
        # Spara PDF:en i minnet eller bearbeta direkt
        # Här kan du implementera din logik med pdfplumber eller PyPDF2
            pdf_text = contents.decode("utf-8", errors="ignore")  # förenklad hantering
            return JSONResponse(content={"pdf_text": pdf_text})
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)