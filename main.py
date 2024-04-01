from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import cv2
from PIL import Image
import io
import face_recognition
import os
from typing import List


class Data(BaseModel):
    data_single: str
    data_list: List[str]

app = FastAPI()
origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/verifica-presenca")
async def CadastroImagem( data: Data):
    known_faces = []

    for image in data.data_list:
        lista = []
        imgCad = base64.b64decode(image)
        imagCad = Image.open(io.BytesIO(imgCad))
        imagCad.convert('RGB')
        imagCad.save("imagem.jpg")
        img2Cad = cv2.imread("imagem.jpg")
        rgb_imgCad = cv2.cvtColor(img2Cad, cv2.COLOR_BGR2RGB)
        img_encodingCad = face_recognition.face_encodings(rgb_imgCad)[0]
        os.remove("imagem.jpg")
        lista.append(img_encodingCad)
        known_faces.append(lista)
    imgRec = base64.b64decode(data.data_single)
    imagRec = Image.open(io.BytesIO(imgRec))
    imagRec.convert('RGB')
    imagRec.save("imagem.jpg")
    img2Rec = cv2.imread("imagem.jpg")
    rgb_img2Rec = cv2.cvtColor(img2Rec, cv2.COLOR_BGR2RGB)
    img_encoding2Rec = face_recognition.face_encodings(rgb_img2Rec)[0]
    os.remove("imagem.jpg")
    print(known_faces)

    i=0
    while(i<len(known_faces)):
        result = face_recognition.compare_faces([known_faces[i][0]], img_encoding2Rec)
        if(result[0]):
            return {"message": "presente",
          
                    }
            
    
        i+=1
    if not result[0]:
        return {"message": "nao esta presente"}


 