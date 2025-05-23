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
            # 'https://www.mercadolivre.com.br/cadiveu-plastica-dos-fios-selagem-termica-passo-2/p/MLB20549848/s',
            # 'https://www.mercadolivre.com.br/wella-mascara-oil-reflections-500ml/p/MLB19512787/s?pdp_filters=item_id%3AMLB4395639466',
            'https://www.belezanaweb.com.br/cadiveu-professional-acai-oil-oleo-de-tratamento-60ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/kit-cadiveu-professional-plastica-dos-fios-alinhamento-profissional-3-produtos/ofertas-marketplace',
            'https://www.belezanaweb.com.br/cadiveu-professional-essentials-bye-bye-frizz-gradual-smoothing-mist-spray-protetor-termico-200ml/ofertas-marketplace',    
            'https://www.belezanaweb.com.br/cadiveu-essentials-quartzo-shine-by-boca-rosa-hair-oleo-capilar-quartzo-liquido-65ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/deva-curl-one-condition-condicionador-355ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/cadiveu-professional-nutri-glow-mascara-capilar-200ml/ofertas-marketplace',
            'https://www.belezanaweb.com.br/deva-curl-heaven-in-hair-mascara-capilar-250g/ofertas-marketplace',
            'https://www.belezanaweb.com.br/deva-curl-supercream-creme-modelador-250g/ofertas-marketplace',
            'https://www.belezanaweb.com.br/cadiveu-essentials-quartzo-shine-leavein-protetor-termico-200ml/ofertas-marketplace',
        ]
        await process_urls(combined_urls)
    except Exception as e:
        print(f'Erro ao executar scrape_combined_crawl4ai.py: {e}')

if __name__ == '__main__':
    asyncio.run(run_combined_crawler())
