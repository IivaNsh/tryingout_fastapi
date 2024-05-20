from typing import Union, Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from utils import get_datatime_str as GetDate, split_filename as SplitFilename



app = FastAPI()

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

@app.post("/save_file/")
async def save_upload_file(file: UploadFile):
    contents = await file.read()
    
    file_name, file_ext = SplitFilename(file.filename)
    save_name = f"{file_name}{GetDate()}{file_ext}"

    with open(f"saved_files/{save_name}", "wb") as f:
        f.write(contents)

    return {"file_saved": save_name}
