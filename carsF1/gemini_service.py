import google.generativeai as genai
from django.conf import settings
from .models import Car

# Configura a API do Gemini com a chave do settings.py
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
except AttributeError:
    # Lida com o caso onde a chave não está configurada, para não quebrar o app
    print("AVISO: A chave da API do Gemini não foi encontrada nas configurações.")
    genai = None

def generate_car_bio(car: Car) -> str:
    """
    Gera uma bio para um carro usando a API do Gemini.
    """
    if not genai:
        return "Serviço de IA indisponível. Chave não configurada."

    # Define o modelo a ser usado
    model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

    # Cria o prompt para a IA
    prompt = f"Crie uma descrição de marketing curta e empolgante, em um parágrafo, para um carro da marca {car.brand.name}, modelo {car.model}, fabricado em {car.factory_year}. Foque em um tom que atraia colecionadores e entusiastas de carros contendo no máx 251 caracteres."

    try:
        # Chama a API
        response = model.generate_content(prompt)
        # Retorna o texto gerado
        return response.text
    except Exception as e:
        # Em caso de erro na API, retorna uma mensagem padrão
        print(f"Erro ao chamar a API do Gemini: {e}")
        return f"Descrição para {car.model} indisponível no momento."
