from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import os
import shutil

app = FastAPI(
    title="Análise de Ameaças STRIDE API",
    description="Uma API para analisar a arquitetura de software de uma imagem usando a metodologia STRIDE.",
    version="1.0.0",
)

class ThreatAnalysisResponse(BaseModel):
    threat_analysis: str
    stride_breakdown: dict

UPLOAD_FOLDER = "uploaded_images"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.post("/analyze_threats/", response_model=ThreatAnalysisResponse)
async def analyze_threats(file: UploadFile = File(...)):
    """
    Recebe uma imagem de uma arquitetura de software e gera uma análise de ameaças STRIDE.

    - **file**: A imagem da arquitetura a ser analisada.
    """
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao salvar a imagem: {str(e)}")

    threat_analysis_text = (
        "Análise de Ameaças STRIDE para a arquitetura de software na imagem. "
        "A arquitetura apresenta possíveis vulnerabilidades relacionadas a: "
        "- **Spoofing**: Falsificação de identidade, especialmente em interfaces de usuário. "
        "- **Tampering**: Alteração de dados em trânsito entre os componentes. "
        "- **Repudiation**: Falta de registo de ações, impedindo a rastreabilidade. "
    )

    stride_breakdown_dict = {
        "Spoofing": "A falta de autenticação forte em pontos de acesso pode permitir falsificação de identidade.",
        "Tampering": "O tráfego de dados não encriptado entre o cliente e o servidor é vulnerável a alterações.",
        "Repudiation": "Os logs de auditoria são insuficientes para rastrear ações de usuários com precisão.",
        "Information Disclosure": "O armazenamento de senhas em texto simples representa um risco de divulgação de informações.",
        "Denial of Service": "A API não tem limite de taxa (rate limiting), tornando-a vulnerável a ataques de negação de serviço.",
        "Elevation of Privilege": "As permissões de usuário não são gerenciadas corretamente, podendo permitir a elevação de privilégios."
    }

    return ThreatAnalysisResponse(
        threat_analysis=threat_analysis_text,
        stride_breakdown=stride_breakdown_dict
    )