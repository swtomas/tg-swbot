import aiohttp
import dict

async def request(text, model):
    url = "soon"
    payload = {
        "model": model, 
        "messages": [
            {"role": "system", "content": dict.promt},
            {"role": "user", "content": text}
        ],
        "seed": 101
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as response:
                response.raise_for_status()
                result = await response.json()
                answer = result['choices'][0]['message']['content']
                return answer
    except aiohttp.ClientError as e:
        return f"ошибка API: {e}"