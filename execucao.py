import time
import asyncio
import requests
from datetime import datetime
from scrape_combined_crawl4ai import process_urls


async def run_combined_crawler():

    print(f'Executando scrape_combined_crawl4ai.py às {datetime.now()}')
    try:

        combined_urls = [
            'https://www.belezanaweb.com.br/wella-professionals-invigo-color-brilliance-shampoo-1-litro/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-invigo-color-brilliance-condicionador-1-litro/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-invigo-color-brilliance-mascara-capilar-500ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-invigo-nutrienrich-shampoo-1-litro/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-invigo-nutrienrich-condicionador-1-litro/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-invigo-nutrienrich-mascara-capilar-500ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-oil-reflections-luminous-reveal-shampoo-1-litro/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-oil-reflections-luminous-reboost-mascara-500ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-oil-reflections-oleo-capilar-100ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/wella-professionals-oil-reflections-light-oleo-capilar-100ml/ofertas-marketplace',
        ]
        await process_urls(combined_urls)
    except Exception as e:
        print(f'Erro ao executar scrape_combined_crawl4ai.py: {e}')

if __name__ == '__main__':
    asyncio.run(run_combined_crawler())
