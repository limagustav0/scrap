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
            'https://www.mercadolivre.com.br/shampoo-higienizando-widi-care-a-juba-500ml-limpeza-inteligente/p/MLB19860817/s',
            'https://www.amazon.com.br/Acidificando-Juba-Acidificante-Widi-500ml/dp/B0D389WN7Z/?_encoding=UTF8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d',
            'https://www.amazon.com.br/Widicare-Encaracolando-Juba-Creme-Pentear/dp/B0BGJ5RB67/ref=sr_1_1?rdc=1&s=beauty&sr=1-1',
            'https://www.mercadolivre.com.br/cadiveu-plastica-dos-fios-selagem-termica-passo-2/p/MLB20549848/s',
            
        ]
        await process_urls(combined_urls)
    except Exception as e:
        print(f'Erro ao executar scrape_combined_crawl4ai.py: {e}')

if __name__ == '__main__':
    asyncio.run(run_combined_crawler())
