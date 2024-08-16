from fastapi import APIRouter, Header, HTTPException, Form, UploadFile, File

formdata_router = APIRouter(prefix="/formdata")


@formdata_router.post("/submit/")
def submit_form(name: str = Form(...), age: int = Form(20)):
    return {"name": name, "age": age}


@formdata_router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
    }
